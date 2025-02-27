# HTML 基礎入門教學

## 什麼是 HTML

HTML 是「HyperText Markup Language」（超文本標記語言）的縮寫，它是用來建立網頁結構的語言。

- 超文本 (HyperText)：指的是可以包含連結（或稱超連結）的文字，這些連結可以導向其他的文件或網站。
- 標記語言 (Markup Language)：指的是使用標籤 (tags) 來標記或描述網頁中的元素。

### 概念介紹

- HTML 的主要作用

  - 它負責描述網頁的結構和內容，類似於建築中的藍圖。舉例來說，HTML 可以定義標題、段落、圖片、連結、表格等網頁元素。
  - HTML 不負責樣式 (CSS 負責網頁的美觀)，也不負責動態交互 (JavaScript 負責行為)，它專注於網頁的內容和框架。

- HTML 文件的基本概念
  - HTML 是網頁的核心骨架
    - 每個網頁都由 HTML 文件構成，這些文件是基於標籤的文本文件。
    - HTML 文件中的標籤用來告訴瀏覽器應該如何顯示每個部分。
  - 範例 1（[HTML 基本架構](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex01.html)）
    ```html
    <!DOCTYPE html>
    <html>
      <head>
        <title>HTML 基本架構</title>
      </head>
      <body>
        <h1>歡迎來到我的網頁</h1>
        <p>這是我的第一段文字。</p>
      </body>
    </html>
    ```
    - `<!DOCTYPE html>`：宣告這個文件是 HTML5 文件。這個宣告告訴瀏覽器應該用 HTML5 標準來解析該網頁。
    - `<html>`：整個 HTML 文件的根標籤，所有內容都會被放在這對標籤之內。
    - `<head>`：包含網頁的 metadata，這些信息不會顯示在頁面上，但對網頁有重要作用，比如頁面的標題。
    - `<title>`：定義了瀏覽器標籤頁上顯示的網頁名稱，在頁面上並不顯示。
    - `<body>`：網頁的主要內容，所有可見的部分，如文字、圖片、標題等，將顯示在這裡。
    - `<h1>`：標題標籤，`<h1>` 表示主標題，通常為頁面中最重要的標題。
    - `<p>`：段落標籤，用於包含一段文本。
- 問題討論
  - 為什麼我們需要用 HTML？  
    HTML 是建立和展示網頁的基本工具，透過它，我們可以組織和展示資訊給網站的訪問者。
  - 瀏覽器如何解釋 HTML？  
    當你打開一個 HTML 文件時，瀏覽器會根據標籤來理解文件中的每個部分，並將它們呈現在網頁上。例如：`<h1>` 會被解釋為大標題，而 `<p>` 會被解釋為段落。

## 基本標籤介紹

### 標題與段落

1. 標題標籤

   - HTML 中的標題：
     - HTML 提供了六種等級的標題標籤，從 `<h1>` 到 `<h6>`，`<h1>` 為最高等級的標題，通常用於網頁的主標題；而 `<h6>` 則為最小的標題，通常用於次要標題或副標題。
     - 標題會有不同的字體大小和粗細，且在語意上表達出內容的層級結構，對於 SEO 和網頁結構清晰度非常重要。
   - 範例 2（[HTML 標題標籤](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex02.html)）

     ```html
     <h1>這是主標題</h1>
     <h2>這是次標題</h2>
     <h3>這是第三層標題</h3>
     <h4>這是第四層標題</h4>
     <h5>這是第五層標題</h5>
     <h6>這是第六層標題</h6>
     ```

2. 段落標籤
   - 使用 `<p>` 標籤來定義一段文字。段落標籤會自動在文字前後添加間距，讓不同段落之間保持分離。
   - `<p>` 主要用來展示多行文本內容，是構建網頁內容的基礎。
   - 範例 3（[HTML 段落標籤](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex03.html)）
     ```html
     <p>這是一段文字，介紹 HTML 的基本概念。</p>
     <p>這是第二段文字，討論 HTML 如何標記內容。</p>
     ```

### 文字格式化

1. 粗體與斜體
   - `<strong>`：用來強調某段文字，通常會顯示為粗體。
   - `<em>`：用來標記斜體字，表示文本語氣的加重。
   - 範例 4（[HTML 粗體與斜體](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex04.html)）
     ```html
     <p>這是一個<strong>非常重要的</strong>提示。</p>
     <p>請務必注意，這是一段<em>特別強調的</em>文字。</p>
     ```
     > `<strong>` 不僅是視覺上的加粗，還有語意上的強調，同樣 `<em>` 不僅是斜體，還意味著語氣的加強。
2. 換行與水平線

   - `<br>`：用來插入換行符號，強制讓文字從下一行開始。
   - `<hr>`：插入一條水平線，用來分隔不同的內容區塊。
   - 範例 5（[HTML 換行與水平線](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex05.html)）
     ```html
     <p>這是一行文字。<br />這是第二行文字。</p>
     <hr />
     <p>這是水平線下面的一段文字。</p>
     ```

### 連結與圖片

1. 超連結標籤
   - 使用 `<a>` 標籤來創建超連結，基本結構為 `<a href="網址">連結文字</a>`，`href` 是連結的目標網址。
   - 增加 `target="_blank"` 屬性，可以讓連結在新標籤頁中打開。
   - 範例 6（[HTML 超連結標籤](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex06.html)）
     ```html
     <a href="https://www.google.com" target="_blank">Google</a>
     ```
2. 圖片標籤
   - 使用 `<img>` 標籤插入圖片。`src` 屬性指定圖片的路徑，`alt` 屬性提供圖片無法顯示時的替代文本。
   - 圖片可以來自網路 (`http://`或`https://` 開頭)，也可以來自本地文件。
   - 範例 7（[HTML 圖片標籤](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex07.html)）
     ```html
     <img
       src="https://www.w3.org/html/logo/downloads/HTML5_Badge_512.png"
       alt="HTML logo"
     />
     <hr />
     <!-- 下方為錯誤連結 -->
     <img
       src="https://www.w3.org/html/logo/downloads/HTML5_Badge_512_error.png"
       alt="HTML logo"
     />
     ```

## 列表與表格

### 列表

1. 無序列表

   - 使用 `<ul>` 標籤定義無序列表，列表項使用 `<li>` 標籤。
   - 無序列表的項目前面通常會有一個圓點或其他符號。
   - 範例 8（[HTML 無序列表](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex08.html)）
     ```html
     <ul>
       <li>蘋果</li>
       <li>香蕉</li>
       <li>櫻桃</li>
     </ul>
     ```

2. 有序列表

   - 使用 `<ol>` 標籤定義有序列表，列表項同樣使用 `<li>`。
   - 有序列表的項目會自動添加編號，如 1、2、3。
   - 範例 9（[HTML 有序列表](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex09.html)）
     ```html
     <ol>
       <li>第一步驟</li>
       <li>第二步驟</li>
       <li>第三步驟</li>
     </ol>
     ```

3. 巢狀列表
   - 列表可以嵌套使用，建立多層級的列表結構。
   - 範例 10（[HTML 巢狀列表](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex10.html)）
     ```html
     <ul>
       <li>
         水果
         <ul>
           <li>蘋果</li>
           <li>香蕉</li>
         </ul>
       </li>
       <li>
         蔬菜
         <ul>
           <li>胡蘿蔔</li>
           <li>菠菜</li>
         </ul>
       </li>
     </ul>
     ```

### 表格

1. 基本表格結構

   - 使用 `<table>` 標籤建立表格。
   - 表格的行使用 `<tr>`（table row）標籤。
   - 表格的單元格使用 `<td>`（table data）標籤。
   - 表頭使用 `<th>`（table header）標籤，通常用於表格的第一行或第一列。
   - 範例 11（[HTML 基本表格](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex11.html)）
     ```html
     <table border="1">
       <tr>
         <th>姓名</th>
         <th>年齡</th>
         <th>職業</th>
       </tr>
       <tr>
         <td>小明</td>
         <td>25</td>
         <td>工程師</td>
       </tr>
       <tr>
         <td>小華</td>
         <td>30</td>
         <td>設計師</td>
       </tr>
     </table>
     ```
   - border="1"：為表格添加邊框，數值代表邊框的寬度。
   - `<th>`：表頭單元格，文字通常會加粗並置中。

2. 合併單元格
   - colspan 屬性：合併多個列（橫向合併）。
   - rowspan 屬性：合併多個行（縱向合併）。
   - 範例 12（[HTML 合併單元格](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex12.html)）
     ```html
     <table border="1">
       <tr>
         <th colspan="2">合併兩個列</th>
       </tr>
       <tr>
         <td rowspan="2">合併兩個行</td>
         <td>單元格 1</td>
       </tr>
       <tr>
         <td>單元格 2</td>
       </tr>
     </table>
     ```

## 表單入門

1.  表單的作用

    - 表單用於收集用戶輸入的信息，並將其提交給伺服器進行處理。
    - 使用 `<form>` 標籤定義表單。

2.  表單元素

    - 輸入欄位 `<input>`

      - `type` 屬性定義輸入的類型，如 `text`、`password`、`email`、`submit` 等。
      - 範例 13（[HTML 輸入欄位](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex13.html)）

        ```html
        <form action="/submit_form" method="post">
          <label for="username">用戶名：</label>
          <input type="text" id="username" name="username" />
          <br />
          <label for="password">密碼：</label>
          <input type="password" id="password" name="password" />
          <br />
          <input type="submit" value="提交" />
        </form>
        ```

        - `action` 屬性：表單提交的目標 URL。
        - `method` 屬性：提交方法，一般為 `get` 或 `post`。
        - `<label>`：用於點擊標籤時自動聚焦到對應的輸入欄位，`for` 屬性應對應輸入欄位的 `id`。

    - 文字區域 `<textarea>`

      - 用於輸入多行文本。
      - 範例 14（[HTML 文字區域](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex14.html)）

        ```html
        <form>
          <label for="message">留言：</label><br />
          <textarea id="message" name="message" rows="4" cols="50"></textarea>
        </form>
        ```

    - 選擇列表 `<select>`

      - 提供下拉選單供用戶選擇。
      - 範例 15（[HTML 選擇列表](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex15.html)）

        ```html
        <form>
          <label for="country">選擇國家：</label>
          <select id="country" name="country">
            <option value="taiwan">台灣</option>
            <option value="japan">日本</option>
            <option value="usa">美國</option>
          </select>
        </form>
        ```

    - 複選框和單選按鈕

      - 複選框 `<input type="checkbox">`，用於多選。
      - 單選按鈕 `<input type="radio">`，用於單選。
      - 範例 16（[HTML 複選框和單選按鈕](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/example/ex16.html)）

        ```html
        <form>
          <p>選擇你喜歡的顏色：</p>
          <input type="checkbox" id="color_red" name="color" value="red" />
          <label for="color_red">紅色</label><br />
          <input type="checkbox" id="color_blue" name="color" value="blue" />
          <label for="color_blue">藍色</label><br />
          <input type="checkbox" id="color_green" name="color" value="green" />
          <label for="color_green">綠色</label><br />

          <p>選擇你的性別：</p>
          <input type="radio" id="gender_male" name="gender" value="male" />
          <label for="gender_male">男</label><br />
          <input type="radio" id="gender_female" name="gender" value="female" />
          <label for="gender_female">女</label><br />
        </form>
        ```

      - 表單提交按鈕

        - `<input type="submit">`：提交表單。
        - `<input type="reset">`：重置表單內容。

## 綜合實作

現在，請根據以下說明進行實作，製作一個包含表單的網頁。這將綜合運用我們之前學習的 HTML 元素。

![img01](https://gainsborouo.github.io/NYCU_GDSC-Frontend/2_html/img/img01.png)

- 標題與表格結構
  - 使用 `<h1>` 標籤作為頁面主標題。
  - 使用 `<table>` 來排列表單元素，使其看起來整齊。
- 表單元素
  - 姓名、電子郵件、年齡：
    - 使用 `<input>` 元素，類型分別為 `text`、`email`、`number`。
  - 性別選擇：
    - 使用單選按鈕 `<input type="radio">`，name 屬性相同，確保只能選擇一項。
  - 興趣愛好：
    - 使用複選框 `<input type="checkbox">`，允許多選。
  - 自我介紹：
    - 使用 `<textarea>` 供用戶輸入多行文本。
- 提交與重置按鈕
  - 提供提交表單的按鈕 `<input type="submit">`。
  - 提供重置表單的按鈕 `<input type="reset">`。

### 實作提示

- 使用 `<form>` 標籤包裹所有的表單元素，並適當設置 `action` 和 `method` 屬性。
- 為每個表單元素添加 `<label>`，並使用 `for` 屬性連結到對應的輸入欄位，提升表單的可用性和易用性。
- 在 `<table>` 中，使用 `<tr>` 來定義表格行，使用 `<td>` 來定義表格單元格。
- 確保網頁結構清晰，代碼縮排整齊，方便閱讀和維護。
