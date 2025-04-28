# Nginx 架設與反向代理教學

## 反向代理 (Reverse Proxy) 介紹

反向代理是一種伺服器端的中介，它坐落在客戶端與後端伺服器之間，接受客戶端請求，再將請求轉發給內部的真實伺服器群組；最後將真實伺服器的回應回傳給客戶端。

### 運作流程

![img01](img/img01.png)

1. 客戶端（瀏覽器）發出 HTTP 請求到反向代理
2. 反向代理根據規則（例如 URL 路徑、負載平衡策略）選擇一台或多台後端伺服器
3. 反向代理將請求轉發至後端伺服器，接收回應後再統一回傳給客戶端

### 主要功能與好處

1. 安全性隔離：隱藏內網伺服器真實 IP、避免直接攻擊
2. 負載平衡：依輪詢（round robin）、IP hash、least connections 等策略分散流量
3. SSL 終端：在反向代理端集中管理 HTTPS 憑證
4. 快取加速：靜態資源或 API 回應可緩存於代理層，減少後端負擔
5. 壓縮與優化：可在傳送給客戶端前，進行 Gzip 壓縮、圖片優化等

## 什麼是 Nginx

- 高效能的 HTTP/反向代理與負載平衡伺服器
- 採用非同步事件驅動與 Master/Worker 架構

### 應用場景

- 靜態檔案伺服
- 反向代理（Proxy → FastAPI、Node.js...）
- 負載平衡（簡易輪詢、IP hash）
- SSL 終端（HTTPS 憑證管理）

### 指令介紹

| 指令                          | 用途                               |
| :---------------------------- | :--------------------------------- |
| `nginx -v`                    | 顯示 Nginx 版本                    |
| `nginx -t`                    | 測試設定檔語法正確性               |
| `sudo systemctl start nginx`  | 啟動 Nginx 服務                    |
| `sudo systemctl stop nginx`   | 停止 Nginx 服務                    |
| `sudo systemctl reload nginx` | 重新載入設定                       |
| `nginx -s reload`             | 直接向 master process 發送重載信號 |

### 檔案結構與設定檔介紹

```bash
/etc/nginx/
├─ nginx.conf # 主設定檔：包含 Main、Events、HTTP 區塊
├─ conf.d/ # 可放額外 .conf 做模組化管理
├─ sites-available/ # 虛擬主機設定檔存放處
└─ sites-enabled/ # 已啟用的虛擬主機（符號連結）
```

#### nginx.conf

- main 區塊：工作程序數量、檔案限制
- events 區塊：連線相關設定（worker_connections）
- http 區塊：MIME、Gzip、全域快取、引入 `conf.d/*.conf`

```bash
user www-data;
worker_processes auto;
pid /run/nginx.pid;
include /etc/nginx/modules-enabled/*.conf;

events {
        worker_connections 768;
        # multi_accept on;
}

http {

        ##
        # Basic Settings
        ##

        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;

        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;

        include /etc/nginx/mime.types;
        default_type application/octet-stream;

        ##
        # SSL Settings
        ##

        ssl_protocols TLSv1 TLSv1.1 TLSv1.2 TLSv1.3; # Dropping SSLv3, ref: POODLE
        ssl_prefer_server_ciphers on;

        ##
        # Logging Settings
        ##

        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;

        ##
        # Gzip Settings
        ##

        gzip on;

        # gzip_vary on;
        # gzip_proxied any;
        # gzip_comp_level 6;
        # gzip_buffers 16 8k;
        # gzip_http_version 1.1;
        # gzip_types text/plain text/css application/json application/javascript text/xml application/xml application/xml+rss text/javascript;

        ##
        # Virtual Host Configs
        ##

        include /etc/nginx/conf.d/*.conf;
        include /etc/nginx/sites-enabled/*;
}


#mail {
#       # See sample authentication script at:
#       # http://wiki.nginx.org/ImapAuthenticateWithApachePhpScript
#
#       # auth_http localhost/auth.php;
#       # pop3_capabilities "TOP" "USER";
#       # imap_capabilities "IMAP4rev1" "UIDPLUS";
#
#       server {
#               listen     localhost:110;
#               protocol   pop3;
#               proxy      on;
#       }
#
#       server {
#               listen     localhost:143;
#               protocol   imap;
#               proxy      on;
#       }
#}
```

#### Server & Location

- server 區塊
  - `listen`：指定監聽的埠號與協定。
  - `server_name`：根據 HTTP Request 中的 Host Header 決定匹配的 server。
- location 區塊
  - 支援不同的路徑匹配方式（前綴匹配、正則表達式匹配）。
  - `root` 與 `alias`：設定靜態檔案目錄，使用方式略有差異。
  - 常用指令包括 `proxy_pass`、`try_files`，用來做反向代理或檔案處理。

## 綜合實作

本次實作將模擬一個完整的前後端專案架構，並在 GitHub Codespaces 上部署：

1. 靜態檔案服務：使用 Nginx 提供 React App 的 HTML、CSS、JS。

2. API 反向代理：將 `/api` 開頭的 HTTP 請求轉發到後端 FastAPI。

### 功能項目

1. 靜態檔案服務

   - Nginx 直接提供 `frontend/dist` 目錄下的靜態檔案。

2. API 反向代理

   - `GET /api/health`：回傳後端健康狀態。
   - `GET /api/greet?name=…`：示範帶參數的 GET 請求。
   - `POST /api/post`：示範接收 JSON 的 POST 請求。

### 環境準備

1.  開啟 Codespace

    - 點擊此 [GitHub Repo](https://github.com/gainsborouo/nginx-tutorial) 連結。
    - 在 GitHub Repo 頁面點擊 `「Code」→「Codespaces」→「Create codespace on main」`。
    - 等待 Codespace 環境建立完成。

2.  建置前端並啟動後端服務

    打開 Codespace 的 Terminal，依序執行以下指令：

    ```bash
    cd frontend
    npm install
    npm run build
    cd ..

    nohup uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload > /dev/null 2>&1 &
    ```

    - 前端會被建置到 `/workspaces/nginx-tutorial/frontend/dist`。
    - 後端使用 `uvicorn` 啟動 FastAPI Server。

3.  Nginx 設定

    打開 `nginx/default.conf`，修改以下 TODO 處的設定

    ```bash
    server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        # TODO: 填寫靜態檔案服務設定
        location / {

        }

        # TODO: 填寫 REST API 反向代理設定
        location /api/ {

        }
    }
    ```

    - 修改重點
      - location `/`：設定 `root` 指向靜態檔案資料夾，並用 `try_files` 支援前端路由。
      - location `/api/`：透過 `proxy_pass` 將請求轉發至 FastAPI。

4.  重載 Nginx 設定

    完成設定後，執行以下指令：

    ```bash
    sudo ln -sf /workspaces/nginx-tutorial/nginx/default.conf /etc/nginx/sites-enabled/default
    sudo nginx -t
    sudo service nginx start
    # sudo service nginx restart
    ```

### 驗證流程

1. 在 VS Code 的「Ports」分頁找到 80 Port 對應的 Forwarded Address。
2. 開啟網址（通常是 `https://<codespace-name>-80.app.github.dev/`）。
3. 功能測試

   - Health Check 應顯示 OK。
   - 測試 GET `/api/greet`。
   - 測試 POST `/api/post`。
