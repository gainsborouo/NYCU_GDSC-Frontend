# FastAPI 後端架設與 API 教學

## 現代網頁應用的前後端分工

### 前端（Frontend）

- 執行環境：使用者的瀏覽器
- 功能與角色：
  - 負責呈現網頁的**視覺介面**
  - 提供與使用者互動的功能（如表單、按鈕、動畫等）
  - 使用 HTML、CSS、JavaScript、前端框架（如 Vue.js、React 等）開發
- 資訊來源：
  - 所有資料皆來自後端提供的 API 回應

### 後端（Backend）

- 執行環境：伺服器（本機或雲端）
- 功能與角色
  - 接收前端發出的請求（如 GET/POST 等）
  - 處理商業邏輯（如會員登入、資料驗證、計算等）
  - 存取資料庫（讀取或寫入資料）
  - 回傳處理結果給前端（通常為 JSON 格式）
- 常見技術

  - 開發框架如 FastAPI、Django、Express 等
  - 資料庫如 PostgreSQL、MySQL、MongoDB 等

- 三大組成部分
  1. **伺服器**：處理與用戶端的連線與資料傳輸（如 HTTP 請求）
  2. **應用程式**：負責實際的業務邏輯與處理流程
  3. **資料庫**：用來儲存應用程式的持久性資料

### 典型的前後端互動流程

1. 使用者在前端點擊按鈕或提交表單
2. 前端透過 HTTP 向後端發送請求（Request）
3. 後端接收請求並執行對應邏輯
4. 後端將結果打包成回應（Response）並回傳給前端
5. 前端接收到回應後進行更新畫面或顯示訊息等操作

## API 在前後端溝通中的角色

### API 是什麼？

- 全名為 Application Programming Interface，應用程式介面
- 提供一組定義好的「**端點（Endpoint）**」供外部程式呼叫
- 前端透過這些端點向後端要求資料或動作

### Web API 的特性與運作方式

- 每個 API 通常對應一個 URL，如 `/api/users` 或 `/api/login`
- 支援多種 HTTP 方法，如：
  - `GET`：取得資料
  - `POST`：新增資料
  - `PUT/PATCH`：更新資料
  - `DELETE`：刪除資料
- 回傳格式通常為 JSON，易於前端解析與使用

### API 的好處

- 將後端邏輯**封裝**起來，前端只需使用定義好的介面
- 可重複使用、易於維護與測試
- 同一組 API 可同時供多種客戶端（Web、Mobile、其他服務）使用

## RESTful API 的概念與設計原則

REST（Representational State Transfer）是一種設計 API 的架構風格，遵循此架構風格所建立的 API 即稱為 RESTful API。

RESTful API 定義了一組清晰、統一且易懂的原則，讓 API 更容易被開發者理解、使用和維護。

### RESTful API 的核心原則

1. 資源導向（Resource-Based）

   - 所有資料或功能都視為資源，以 URL 表示。
   - URL 應直觀且可讀，例如：
     - `/users` 表示使用者集合資源
     - `/items/123` 表示 ID 為 123 的單一商品資源

2. 統一介面（Uniform Interface）
   - 使用 HTTP 方法（GET、POST、PUT、DELETE 等）表示不同的操作。
   - 每個 HTTP 方法都有固定的語義（如 GET 為讀取、POST 為新增等）。
3. 無狀態（Stateless）

   - 每個請求皆獨立且完整，伺服器不會儲存任何客戶端狀態。
   - 用戶端須透過每次請求完整提供所有必要的資訊（例如授權 Token 等）。

4. 回傳資源的表現形式（Representation）

   - 資源透過特定格式呈現，如 JSON 或 XML，JSON 為目前最廣泛採用。

### RESTful API 設計範例

一個良好設計的 RESTful API 通常依據「資源類型」設計 URL 路徑，搭配 HTTP 方法來對應操作：

| 方法   | 路徑         | 說明                    |
| ------ | ------------ | ----------------------- |
| GET    | `/users`     | 取得所有使用者          |
| POST   | `/users`     | 新增使用者              |
| GET    | `/users/123` | 取得 ID 為 123 的使用者 |
| PUT    | `/users/123` | 更新 ID 為 123 的使用者 |
| DELETE | `/users/123` | 刪除 ID 為 123 的使用者 |

使用上述設計方式可大幅提高 API 可讀性，降低開發與維護的難度。

## 常見的 HTTP 方法與 Web API 操作

Web API 通常是基於 **HTTP 通訊協定**設計的。最常用的四種 HTTP 方法分別為：

### GET

- 用途：取得（讀取）伺服器上的指定資源資訊
- 特性：
  - 不會修改伺服器資料
  - 多次發送相同請求，應該得到相同結果
- 範例：
  - `GET /users`：取得所有使用者資料列表
  - `GET /users/123`：取得 ID 為 123 的使用者資訊

### POST

- 用途：創建新的資源或提交資料進行處理
- 特性：
  - 有可能對伺服器狀態造成改變
  - 多次重複相同 POST 可能會產生多筆資料
- 範例：
  - `POST /orders`：新增一筆訂單
  - 請求主體（Body）會包含新增所需的資料（如 JSON 格式）

### PUT

- 用途：更新（取代）伺服器上的指定資源內容
- 特性：
  - 傳送的資料通常會**完整覆蓋**原本資源
  - 重複相同 PUT 請求不會造成額外副作用
  - 某些實作中，若資源不存在會**創建新資源**
- 範例：
  - `PUT /users/123`：將 ID 為 123 的使用者資料完整替換成新內容

### DELETE

- 用途：刪除指定的資源
- 特性：
  - 刪除動作應在重複執行時也不應出錯
  - 刪除成功後，資源即不再存在
- 範例：
  - `DELETE /users/123`：刪除 ID 為 123 的使用者資料

### 對應 CRUD 操作

| CRUD 操作 | HTTP 方法 | 說明     |
| --------- | --------- | -------- |
| Create    | POST      | 新增資源 |
| Read      | GET       | 讀取資源 |
| Update    | PUT       | 更新資源 |
| Delete    | DELETE    | 刪除資源 |

### 補充：其他 HTTP 方法

除了上述四種常用方法，HTTP/1.1 還定義了其他操作方法，例如：

- HEAD：取得與 GET 相同的回應，但不包含主體（Body）
- OPTIONS：查詢資源支援哪些 HTTP 方法
- PATCH：部分更新資源（與 PUT 相比為「局部更新」）
- CONNECT、TRACE：較少見，多用於底層網路操作或除錯

## 測試 API 的常見方法

在開發或使用後端 API 時，經常需要進行測試，以確保端點正確回應並符合預期功能。以下介紹三種常見的 API 測試工具與使用情境：

### 瀏覽器

- 適用情境：測試不需參數或主體的簡單 `GET` 請求
- 使用方式：
  - 在瀏覽器地址列輸入 API 的 URL，如：
    ```
    http://localhost:8000/api/status
    ```
  - 瀏覽器會自動發出 GET 請求並顯示回應（通常為 JSON 或純文字）
- 限制：
  - 僅支援 GET 請求，無法發送 POST、PUT、DELETE 等
  - 無法自訂請求標頭或主體（如設定 JSON 或 Token）

### cURL

- 適用情境：進階測試、腳本化操作、自動化流程
- 特點：
  - 支援所有 HTTP 方法（GET、POST、PUT、DELETE、PATCH…）
  - 可設定標頭、主體、Cookie、授權等資訊
  - 可寫入 Shell 腳本中自動執行
- 使用範例：

  - 發送 GET 請求

    ```bash
    curl http://localhost:8000/api/status
    ```

  - 發送 POST 請求（含 JSON 資料）

    ```bash
    curl -X POST "http://localhost:8000/api/items" \
        -H "Content-Type: application/json" \
        -d '{"name": "Apple", "price": 5.99}'
    ```

  - 發送 PUT 或 DELETE 請求

    ```bash
    curl -X PUT "http://localhost:8000/api/items/123" \
        -H "Content-Type: application/json" \
        -d '{"name": "Banana", "price": 3.50}'

    curl -X DELETE "http://localhost:8000/api/items/123"
    ```

- 優點
  - 輕量、無 GUI，可快速操作
  - 方便整合到測試腳本或 CI/CD 流程中
  - 易於重現與分享測試命令

### Postman

- 適用情境：需要多次手動測試、建構複雜請求、多人協作
- 特點：
  - 圖形化介面，直覺設定請求內容（URL、方法、標頭、主體）
  - 支援各種身份驗證機制（Token、Basic Auth、OAuth…）
  - 可檢視格式化的 JSON 回應、狀態碼、延遲時間等
  - 支援：
    - 建立請求集合（Collections）
    - 撰寫測試腳本
    - 匯出並分享測試案例
- 使用方式：

  - 建立新請求 → 選擇方法（如 GET）
  - 輸入 URL，例如：
    ```
    http://localhost:8000/api/status
    ```
  - 點擊 Send → 檢視伺服器回應

- 優點：
  - 友善易用，適合初學者與團隊使用
  - 適合測試複雜結構與需要驗證的 API
  - 可持久化測試資料與流程，提升重用性

## FastAPI 介紹與比較

FastAPI 是一個現代化的 Python Web 框架，專門用來打造高性能的 Web API。

### 核心優勢

#### 高性能

- FastAPI 從設計上即追求與 Node.js、Go 等高效能框架媲美的效能。
- 採用：
  - 非同步 async/await 支援
  - 事件迴圈驅動的 Uvicorn ASGI 伺服器
  - Starlette 底層架構
- 適合：
  - 高併發、高請求量的 API
  - 與 Flask 等 WSGI 架構相比，FastAPI 在大量連線時表現更穩定。

#### 型別註解與自動驗證

- 利用 Python 3 的 Type Hints 搭配 Pydantic：
  - 自動轉換請求參數類型
  - 自動進行資料驗證與錯誤處理
- 範例：
  ```python
  @app.get("/items/{item_id}")
  def read_item(item_id: int):
      return {"item_id": item_id}
  ```
  - 若傳入非整數，FastAPI 自動回傳 422 錯誤，提示類型不符。
- 效果：
  - 提升開發安全性
  - 降低模板驗證程式碼需求

#### 自動生成互動式 API 文件

- FastAPI 內建兩種 API 文件介面，符合 OpenAPI 規範：
  - `/docs`：使用 Swagger UI
  - `/redoc`：使用 ReDoc
- 功能：
  - 自動列出所有路由、參數、模型
  - 可直接線上測試 API 請求
  - 無需額外撰寫文件

#### 進階功能整合

- 安全性支援
  - 提供 OAuth2、JWT 等常見認證機制的建構工具
- 擴充性與生態系統
  - 可與 SQLAlchemy、Tortoise ORM、MongoDB 等整合
  - 適合構建微服務或資料科學應用

## 綜合實作

接下來，我們透過一個簡單的商品管理範例，實作一個具有基本 CRUD 功能的 RESTful API。

### API 規格

- `POST /items`：新增商品
- `GET /items`：取得所有商品清單
- `GET /items/{id}`：取得指定 ID 的商品
- `PUT /items/{id}`：更新指定商品
- `DELETE /items/{id}`：刪除指定商品

### 安裝套件

```bash
python3 -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
```

### main.py 完整程式碼

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# 商品資料模型
class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float

# 模擬資料庫
items_db = {}
current_id = 0

# 建立商品
@app.post("/items")
def create_item(item: Item):
    global current_id
    current_id += 1
    items_db[current_id] = item
    return {"id": current_id, **item.dict()}

# 取得所有商品
@app.get("/items")
def list_items():
    return [{"id": item_id, **item.dict()} for item_id, item in items_db.items()]

# 取得單一商品
@app.get("/items/{item_id}")
def get_item(item_id: int):
    if item_id in items_db:
        return {"id": item_id, **items_db[item_id].dict()}
    raise HTTPException(status_code=404, detail="Item not found")

# 更新商品
@app.put("/items/{item_id}")
def update_item(item_id: int, new_item: Item):
    if item_id in items_db:
        items_db[item_id] = new_item
        return {"id": item_id, **new_item.dict()}
    raise HTTPException(status_code=404, detail="Item not found")

# 刪除商品
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if item_id in items_db:
        del items_db[item_id]
        return {"detail": "Item deleted"}
    raise HTTPException(status_code=404, detail="Item not found")
```

### 啟動伺服器

```bash
uvicorn main:app --reload
```

伺服器啟動後將在 `http://127.0.0.1:8000` 提供 API，並可訪問：

- `http://127.0.0.1:8000/docs`：Swagger UI
- `http://127.0.0.1:8000/redoc`：ReDoc 文件

### 測試 API

#### 新增商品

```bash
curl -X POST "http://127.0.0.1:8000/items" \
     -H "Content-Type: application/json" \
     -d '{"name": "Apple", "description": "Red fruit", "price": 5.99}'
```

回應

```json
{ "id": 1, "name": "Apple", "description": "Red fruit", "price": 5.99 }
```

#### 取得所有商品

```bash
curl http://127.0.0.1:8000/items
```

回應

```json
[{ "id": 1, "name": "Apple", "description": "Red fruit", "price": 5.99 }]
```

#### 更新商品

```bash
curl -X PUT "http://127.0.0.1:8000/items/1" \
     -H "Content-Type: application/json" \
     -d '{"name": "Green Apple", "description": "Bright Green fruit", "price": 6.5}'
```

回應

```json
{
  "id": 1,
  "name": "Green Apple",
  "description": "Bright Green fruit",
  "price": 6.5
}
```

#### 刪除商品

```bash
curl -X DELETE http://127.0.0.1:8000/items/1
```

回應

```json
{ "detail": "Item deleted" }
```
