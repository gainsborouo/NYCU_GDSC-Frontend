# CSS 基礎入門教學

## 什麼是 CSS

CSS 是「Cascading Style Sheets」（層疊樣式表）的縮寫，它是用來控制網頁外觀和佈局的樣式語言。通過 CSS，我們可以美化 HTML 元素，使網頁更加吸引人和易於閱讀。

- 層疊 (Cascading)：指的是樣式可以從多個來源應用到元素上，並按照一定的優先順序進行合併和覆蓋。
- 樣式表 (Style Sheets)：指的是定義樣式規則的文件或區塊，這些規則決定了 HTML 元素的外觀。

### CSS 的主要作用

- 控制佈局：決定元素在頁面中的位置和排列方式，例如使用彈性盒模型（Flexbox）或網格系統（Grid）來構建響應式佈局。
- 設置樣式：包括顏色、字體、間距、邊框、背景等，使網頁具有吸引力和一致性。
- 響應式設計：根據不同設備和屏幕大小調整樣式，確保網頁在各種設備上都能良好顯示。

## CSS 基本語法

CSS 的基本語法由選擇器（Selector）和聲明（Declaration）組成。選擇器用來指定要應用樣式的 HTML 元素，聲明則定義具體的樣式屬性和值。

### 選擇器

選擇器用來選擇 HTML 元素，常見的選擇器包括：

- 元素選擇器：選擇所有指定的 HTML 標籤，例如 `p` 選擇所有段落。
- 類選擇器：選擇具有特定類別的元素，使用 `.` 符號，例如 `.container`。
- ID 選擇器：選擇具有特定 ID 的元素，使用 `#` 符號，例如 `#header`。
- 組合選擇器：可以組合多個選擇器來選擇特定的元素，例如 `div p` 選擇所有在 `div` 內的 `p` 元素。
- 偽類選擇器：選擇處於特定狀態的元素，例如 `:hover`, `:nth-child(n)`。
- 屬性選擇器：選擇具有特定屬性的元素，例如 `[type="text"]`。

### 聲明

聲明由屬性和屬性值組成，使用冒號 `:` 分隔，並以分號 `;` 結尾。例如：

```css
color: blue;
font-size: 16px;
```

### 範例

```css
/* 元素選擇器 */
p {
  color: blue;
  font-size: 16px;
}

/* 類選擇器 */
.container {
  width: 80%;
  margin: 0 auto;
}

/* ID 選擇器 */
#header {
  background-color: #f0f0f0;
  padding: 20px;
}

/* 組合選擇器 */
div p {
  line-height: 1.5;
}

/* 偽類選擇器 */
a:hover {
  color: red;
}

/* 屬性選擇器 */
input[type="text"] {
  border: 1px solid #ccc;
}
```

### 如何在 HTML 中使用 CSS

有三種方式將 CSS 應用到 HTML 中：

1. 內聯樣式（Inline Styles）：直接在 HTML 元素的 `style` 屬性中定義樣式。
   ```html
   <p style="color: red;">這是一個紅色的段落。</p>
   ```
2. 內部樣式表（Internal Style Sheet）：在 HTML 文件的 `<head>` 區域內使用 `<style>` 標籤定義樣式。

   ```html
   <head>
     <style>
       p {
         color: green;
       }
     </style>
   </head>
   ```

3. 外部樣式表（External Style Sheet）：將 CSS 定義在獨立的 `.css` 文件中，並在 HTML 文件中使用 `<link>` 標籤引用。
   ```html
   <head>
     <link rel="stylesheet" href="styles.css" />
   </head>
   ```
   ```css
   /* styles.css */
   p {
     color: purple;
   }
   ```

## 基本樣式屬性介紹

### 字體與文字

1. 顏色（`color`）

   - 用來設置文字的顏色，可以使用多種表示方式，例如十六進位（`#RRGGBB`）、RGB（`rgb(r, g, b)`）、RGBA（`rgba(r, g, b, a)`）、HSL（`hsl(h, s%, l%)`）等。
   - 支援關鍵字（如 `red`, `blue`, `green`）來快速指定基本顏色。
   - 範例 1（[CSS 基本顏色應用](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex01.html)）

     ```css
     p {
       color: #333333; /* 深灰色文字 */
     }

     h1 {
       color: rgb(70, 130, 180); /* 鋼藍色文字 */
     }

     h2 {
       color: rgba(255, 0, 0, 0.7); /* 半透明紅色文字 */
     }
     h3 {
       color: hsl(120, 100%, 50%); /* 綠色文字 */
     }

     a {
       color: blue; /* 關鍵字顏色 */
     }
     ```

2. 字體系列（`font-family`）

   - 指定文字顯示的字體系列，通常建議列出多個字體，以便瀏覽器選擇可以呈現的字體。
   - 可以使用系統默認字體系列（如 `serif`, `sans-serif`, `monospace`）作為備選。
   - 支援自定義字體，透過 `@font-face` 引入外部字體。
   - 範例 2（[CSS 指定字體](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex02.html)）

     ```css
     body {
       font-family: "Arial", sans-serif;
     }

     h1 {
       font-family: "Times New Roman", serif;
     }

     p.custom-font {
       font-family: "Courier New", monospace;
     }
     ```

3. 字體大小（`font-size`）

   - 指定文字的大小，支持多種單位，如：
     - 絕對單位：`px`, `pt`, `cm`。
     - 相對單位：`em`, `rem`, `%`。
     - 關鍵字：`small`, `medium`, `large`。
   - 使用相對單位有助於提升網頁的響應式設計和無障礙性。
   - 範例 3（[CSS 不同字體大小](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex03.html)）

     ```css
     p {
       font-size: 16px; /* 絕對單位 */
     }

     h1 {
       font-size: 2em; /* 相對單位，相對於父元素字體大小 */
     }

     h2 {
       font-size: 150%; /* 相對單位，相對於父元素字體大小 */
     }

     h3 {
       font-size: large; /* 關鍵字 */
     }
     ```

4. 字體粗細（`font-weight`）

   - 用於調整文字的粗細，可接受以下值：
     - 關鍵字：`normal`（400）, `bold`（700）。
     - 數值：從 `100`（極細）到 `900`（極粗）。
   - 範例 4（[CSS 不同字體粗細](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex04.html)）

     ```css
     .strong-text {
       font-weight: bold;
     }

     .light-text {
       font-weight: 300;
     }

     .normal-text {
       font-weight: normal;
     }

     .heavy-text {
       font-weight: 900;
     }
     ```

5. 文字對齊（`text-align`）

   - 設置文字的對齊方式。
     - left：左對齊（默認）。
     - right：右對齊。
     - center：居中對齊。
     - justify：兩端對齊，文字間距自動調整以填滿行。
   - 範例 5（[CSS 不同對齊方式](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex05.html)）

     ```css
     .left-align {
       text-align: left;
     }

     .center-align {
       text-align: center;
     }

     .right-align {
       text-align: right;
     }

     .justify-align {
       text-align: justify;
     }
     ```

### 盒模型（Box Model）

![img01](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/img/img01.png)

CSS 盒模型描述了元素在頁面中的佈局，包括內容區（Content）、內邊距（Padding）、邊框（Border）和外邊距（Margin）。

- Content：元素的實際內容，如文字或圖片。
- Padding：內容區與邊框之間的空間。
- Border：圍繞內容和內邊距的邊框。
- Margin：元素與其他元素之間的空間。

### 佈局與間距

1. 外邊距（`margin`）

   - 設置元素的外邊距，用於控制元素之間的間距。

     - 單一值：`margin: 10px;` 四周均設置 10px 的外邊距。
     - 雙值：`margin: 10px 20px;` 上下 10px，左右 20px。
     - 四值：`margin: 5px 10px 15px 20px;` 上、右、下、左依序設置。

   - 範例 6（[CSS 不同外邊距設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex06.html)）

     ```css
     .no-margin {
       margin: 0;
     }

     .small-margin {
       margin: 10px;
     }

     .large-margin {
       margin: 30px;
     }

     .symmetric-margin {
       margin: 20px 40px; /* 上下20px，左右40px */
     }

     .custom-margin {
       margin: 5px 10px 15px 20px; /* 上5px，右10px，下15px，左20px */
     }
     ```

2. 內邊距（`padding`）

   - 設置元素的內邊距，用於控制內容與邊框之間的空間。
     - 單一值：`padding: 10px;` 四周均設置 10px 的內邊距。
     - 雙值：`padding: 10px 20px;` 上下 10px，左右 20px。
     - 四值：`padding: 5px 10px 15px 20px;` 上、右、下、左依序設置。
   - 範例 7（[CSS 不同內邊距設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex07.html)）

     ```css
     .no-padding {
       padding: 0;
     }

     .small-padding {
       padding: 10px;
     }

     .large-padding {
       padding: 30px;
     }

     .symmetric-padding {
       padding: 20px 40px; /* 上下20px，左右40px */
     }

     .custom-padding {
       padding: 5px 10px 15px 20px; /* 上5px，右10px，下15px，左20px */
     }
     ```

3. 邊框（`border`）

   - 設置元素的邊框，包括邊框的寬度、樣式和顏色。
     - 邊框寬度：如 `1px`, `2px`。
     - 邊框樣式：`solid`, `dashed`, `dotted`, `double`, `groove`, `ridge`, `inset`, `outset`。
     - 邊框顏色：可以使用顏色值或關鍵字。
   - 範例 8（[CSS 不同邊框設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex08.html)）

     ```css
     .no-border {
       border: none;
     }

     .solid-border {
       border: 2px solid #000000;
     }

     .dashed-border {
       border: 2px dashed #ff0000;
     }

     .dotted-border {
       border: 2px dotted #00ff00;
     }

     .double-border {
       border: 4px double #0000ff;
     }

     .groove-border {
       border: 3px groove #8e44ad;
     }
     ```

4. 寬度與高度（`width` & `height`）

   - 設置元素的寬度和高度。
     - 寬度（`width`）：可以使用 `px`, `%`, `em`, `rem`, `vw`（視窗寬度單位）等。
     - 高度（`height`）：同寬度，支持多種單位。
     - 自動調整：`auto` 允許元素根據內容自動調整大小。
   - 範例 9（[CSS 不同寬度和高度設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex09.html)）

     ```css
     .fixed-size {
       width: 200px;
       height: 100px;
       background-color: #d1c4e9;
     }

     .percentage-size {
       width: 50%;
       height: 150px;
       background-color: #c5cae9;
     }

     .auto-size {
       width: auto;
       height: auto;
       background-color: #bbdefb;
     }

     .vw-size {
       width: 50vw; /* 視窗寬度的 50% */
       height: 100px;
       background-color: #b3e5fc;
     }

     .em-size {
       width: 20em; /* 當前字體大小的 20 倍 */
       height: 100px;
       background-color: #81d4fa;
     }
     ```

### 背景

1. 背景顏色（`background-color`）

   - 設置元素的背景顏色。
   - 可以使用多種顏色表示方式，如 `#RRGGBB`, `rgb()`, `rgba()`, `hsl()`, 關鍵字等。
   - 範例 10（[CSS 不同背景顏色](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex10.html)）

     ```css
     .bg-white {
       background-color: #ffffff;
     }

     .bg-light {
       background-color: #f0f0f0;
     }

     .bg-dark {
       background-color: #333333;
       color: #ffffff; /* 為了對比，設置文字為白色 */
     }

     .bg-transparent {
       background-color: rgba(0, 0, 0, 0); /* 透明背景 */
     }
     ```

2. 背景圖片（`background-image`）

   - 設置元素的背景圖片。
   - 屬性：
     - `background-size`：控制背景圖片的大小，如 `cover`, `contain`, `auto`, 或具體尺寸。
     - `background-repeat`：控制背景圖片是否重複，如 `no-repeat`, `repeat`, `repeat-x`, `repeat-y`。
     - `background-position`：控制背景圖片的位置，如 `center`, `top right`, `10px 20px`。
     - `background-attachment`：控制背景圖片是否固定，如 `fixed`, `scroll`。
   - 範例 11（[CSS 不同背景圖片設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex11.html)）

     ```css
     .bg-no-image {
       background-image: none;
       background-color: #757575;
     }

     .bg-image-1 {
       background-image: url("https://via.placeholder.com/300x200.png?text=Image+1");
       background-size: cover;
       background-repeat: no-repeat;
       background-position: center;
     }

     .bg-image-2 {
       background-image: url("https://via.placeholder.com/300x200.png?text=Image+2");
       background-size: contain;
       background-repeat: repeat;
       background-position: top left;
     }

     .bg-image-fixed {
       background-image: url("https://via.placeholder.com/300x200.png?text=Fixed+Image");
       background-size: cover;
       background-repeat: no-repeat;
       background-position: center;
       background-attachment: fixed;
     }
     ```

## 其他常用屬性

1. 顯示類型（`display`）

   - 設置元素的顯示類型，決定元素如何在頁面中呈現。
   - 常用值：
     - `block`：元素作為塊級元素，獨占一行，寬度默認為父容器的 100%。
     - `inline`：元素作為行內元素，不獨占一行，僅佔據內容所需的寬度。
     - `inline-block`：元素同時具有 inline 和 block 的特性，可以設置寬高。
     - `flex`：啟用彈性盒布局，用於構建彈性和響應式佈局。
     - `grid`：啟用網格布局，用於構建複雜的網格系統。
     - `none`：元素不會被顯示，從文檔流中移除。
   - 範例 12（[CSS 不同顯示類型](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex12.html)）

     ```css
     .block-element {
       display: block;
       width: 100%;
       background-color: #ffccbc;
       padding: 10px;
     }

     .inline-element {
       display: inline;
       background-color: #dcedc8;
       padding: 10px;
     }

     .inline-block-element {
       display: inline-block;
       width: 150px;
       background-color: #c5e1a5;
       padding: 10px;
     }

     .flex-container {
       display: flex;
       justify-content: space-around;
       background-color: #b2dfdb;
       padding: 10px;
     }

     .flex-item {
       background-color: #80cbc4;
       padding: 20px;
       margin: 5px;
     }

     .grid-container {
       display: grid;
       grid-template-columns: repeat(3, 1fr);
       gap: 10px;
       background-color: #ffecb3;
       padding: 10px;
     }

     .grid-item {
       background-color: #ffe082;
       padding: 20px;
       text-align: center;
     }
     ```

2. 定位（`position`）

   - 設置元素的定位方式，決定元素在頁面中的位置及其相對於其他元素的關係。
   - 常用值：
     - `static`：默認定位，元素按照正常文檔流排列。
     - `relative`：相對定位，元素根據其正常位置進行偏移。
     - `absolute`：絕對定位，元素相對於最近的已定位祖先元素定位，脫離文檔流。
     - `fixed`：固定定位，元素相對於視窗定位，保持在視窗固定位置。
     - `sticky`：粘性定位，元素根據用戶的滾動位置在相對和固定定位之間切換。
   - 範例 13（[CSS 不同定位方式](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex13.html)）

     ```css
     .static-element {
       position: static;
       background-color: #ffab91;
       padding: 10px;
     }

     .relative-element {
       position: relative;
       top: 20px;
       left: 20px;
       background-color: #ff8a65;
       padding: 10px;
     }

     .absolute-element {
       position: absolute;
       top: 50px;
       right: 50px;
       background-color: #ff7043;
       padding: 10px;
     }

     .fixed-element {
       position: fixed;
       bottom: 10px;
       right: 10px;
       background-color: #ff5722;
       padding: 10px;
       color: #ffffff;
     }

     .sticky-element {
       position: sticky;
       top: 0;
       background-color: #8e44ad;
       padding: 10px;
       color: #ffffff;
     }
     ```

3. 顯示與隱藏（`visibility` & `display`）

   - 控制元素的顯示狀態。
   - `visibility`：
     - `visible`：元素可見。
     - `hidden`：元素隱藏，但仍占據空間。
   - `display`：
     - `none`：元素完全不顯示，從文檔流中移除，不占據空間。
     - `block`, `inline`, `inline-block`, 等：控制元素的顯示類型。
   - 範例 14（[CSS 顯示與隱藏](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex14.html)）

     ```css
     .visible-element {
       visibility: visible;
       background-color: #c5cae9;
       padding: 10px;
     }

     .hidden-visibility {
       visibility: hidden;
       background-color: #c5cae9;
       padding: 10px;
     }

     .hidden-display {
       display: none;
     }

     .block-element {
       display: block;
       background-color: #c5cae9;
       padding: 10px;
     }
     ```

4. 透明度與不透明度（`opacity`）

   - 設置元素的透明度，範圍從 0（完全透明）到 1（完全不透明）。
   - `opacity`：影響整個元素及其子元素的透明度。
   - `background-color` 的 `rgba` 或 `hsla`：僅影響背景顏色的透明度，不影響內容。
   - 範例 15（[CSS 不同透明度設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex15.html)）

     ```css
     .full-opacity {
       opacity: 1;
       background-color: #81c784;
       padding: 20px;
     }

     .semi-opacity {
       opacity: 0.5;
       background-color: #81c784;
       padding: 20px;
     }

     .transparent-background {
       background-color: rgba(129, 199, 132, 0.5); /* 半透明背景 */
       padding: 20px;
       color: #ffffff;
     }
     ```

5. 字體樣式（`font-style`）

   - 設置文字的樣式，如斜體、正常等。
   - 常用值：
     - `normal`：正常字體。
     - `italic`：斜體字。
     - `oblique`：傾斜字體，與 `italic` 類似但較少使用。
   - 範例 16（[CSS 不同字體樣式](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex16.html)）

     ```css
     .normal-text {
       font-style: normal;
     }

     .italic-text {
       font-style: italic;
     }

     .oblique-text {
       font-style: oblique;
     }
     ```

6. 字體間距（`letter-spacing` & `word-spacing`）

   - `letter-spacing`：設置字母之間的間距。
   - `word-spacing`：設置單詞之間的間距。
   - 範例 17（[CSS 不同字母間距設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex17.html)）

     ```css
     .default-spacing {
       letter-spacing: normal;
     }

     .tight-spacing {
       letter-spacing: -1px;
     }

     .wide-spacing {
       letter-spacing: 3px;
     }
     ```

7. 文字陰影（`text-shadow`）

   - 為文字添加陰影效果，提升文字的立體感和可讀性。
   - 語法：`text-shadow: h-offset v-offset blur color;`
     - `h-offset`：水平偏移量。
     - `v-offset`：垂直偏移量。
     - `blur`：模糊半徑。
     - `color`：陰影顏色。
   - 範例 18（[CSS 不同文字陰影設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex18.html)）

     ```css
     .no-shadow {
       text-shadow: none;
     }

     .light-shadow {
       text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
     }

     .heavy-shadow {
       text-shadow: 4px 4px 10px rgba(0, 0, 0, 0.7);
     }

     .color-shadow {
       text-shadow: 2px 2px 5px red;
     }
     ```

8. 文本裝飾（`text-decoration`）

   - 設置文字的裝飾效果，如下劃線、上劃線、刪除線等。
   - 常用值：
     - `none`：無裝飾。
     - `underline`：下劃線。
     - `overline`：上劃線。
     - `line-through`：刪除線。
     - `underline overline`：同時下劃線和上劃線。
   - 範例 19（[CSS 不同字體裝飾](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex19.html)）

     ```css
     .no-decoration {
       text-decoration: none;
     }

     .underline-text {
       text-decoration: underline;
     }

     .overline-text {
       text-decoration: overline;
     }

     .line-through-text {
       text-decoration: line-through;
     }

     .double-decoration {
       text-decoration: underline overline;
     }
     ```

9. 盒子陰影（`box-shadow`）

   - 為元素添加陰影效果，增強元素的立體感。
   - 語法：`box-shadow: h-offset v-offset blur spread color;`
     - `h-offset`：水平偏移量。
     - `v-offset`：垂直偏移量。
     - `blur`：模糊半徑。
     - `spread`：擴展半徑（可選）。
     - `color`：陰影顏色。
   - 支援多重陰影，以逗號分隔。
   - 範例 20（[CSS 不同盒子陰影設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex20.html)）

     ```css
     .no-shadow {
       box-shadow: none;
     }

     .simple-shadow {
       box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3);
     }

     .deep-shadow {
       box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.7);
     }

     .multiple-shadows {
       box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.3), -2px -2px 5px rgba(255, 255, 255, 0.5);
     }

     .color-shadow {
       box-shadow: 3px 3px 10px rgba(255, 0, 0, 0.5);
     }
     ```

10. 圓角（`border-radius`）

    - 為元素的邊框添加圓角，提升視覺效果和柔和感。
    - 語法：border-radius: radius;
      - 可以單獨設置四個角的圓角，如 `border-top-left-radius`。
      - 支援不同單位，如 `px`, `%`。
    - 範例 21（[CSS 不同圓角設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex21.html)）

      ```css
      .no-radius {
        border-radius: 0;
      }

      .small-radius {
        border-radius: 5px;
      }

      .medium-radius {
        border-radius: 15px;
      }

      .large-radius {
        border-radius: 50px;
      }

      .circular {
        border-radius: 50%;
      }

      .different-radius {
        border-top-left-radius: 10px;
        border-top-right-radius: 20px;
        border-bottom-right-radius: 30px;
        border-bottom-left-radius: 40px;
      }
      ```

11. 背景混合模式（`background-blend-mode`）

    - 設置背景圖片與背景顏色之間的混合模式，創建多樣化的視覺效果。
    - 常用值：
      - `multiply`：將背景顏色與背景圖片相乘，顏色加深。
      - `screen`：將背景顏色與背景圖片反相相乘，顏色變亮。
      - `overlay`：結合 `multiply` 和 `screen`，根據背景顏色的明暗調整。
      - `darken`：選擇較暗的顏色。
      - `lighten`：選擇較亮的顏色。
      - `color-dodge`：顏色閃亮。
      - `color-burn`：顏色變暗。
    - 範例 22（[CSS 不同背景混合模式設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex22.html)）

      ```css
      .blend-none {
        background-image: url("https://placehold.co/300x200?text=Image+1");
        background-color: #2196f3;
        background-blend-mode: normal;
        padding: 20px;
        color: #ffffff;
      }

      .blend-multiply {
        background-image: url("https://placehold.co/300x200?text=Image+2");
        background-color: #2196f3;
        background-blend-mode: multiply;
        padding: 20px;
        color: #ffffff;
      }

      .blend-screen {
        background-image: url("https://placehold.co/300x200?text=Image+3");
        background-color: #2196f3;
        background-blend-mode: screen;
        padding: 20px;
        color: #ffffff;
      }

      .blend-overlay {
        background-image: url("https://placehold.co/300x200?text=Image+4");
        background-color: #2196f3;
        background-blend-mode: overlay;
        padding: 20px;
        color: #ffffff;
      }
      ```

12. 過渡效果（`transition`）

    - 為元素的屬性變化添加過渡效果，使變化更加平滑和自然。
    - 語法：`transition: property duration timing-function delay;`
      - `property`：要添加過渡效果的 CSS 屬性。
      - `duration`：過渡效果的持續時間，如 `2s`, `500ms`。
      - `timing-function`：過渡效果的速度曲線，如 `ease`, `linear`, `ease-in`, `ease-out`, `ease-in-out`。
      - `delay`：過渡效果的延遲時間，如 `0s`, `1s`。
    - 範例 23（[CSS 不同過渡效果設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex23.html)）

      ```css
      .transition-box {
        width: 200px;
        height: 200px;
        background-color: #81c784;
        transition: background-color 2s ease, transform 1s ease-in-out;
      }

      .transition-box:hover {
        background-color: #388e3c;
        transform: rotate(45deg);
      }
      ```

13. 元素變形（`transform`）

- 對元素進行變形，如旋轉、縮放、傾斜和平移。
- 常用函數：
  - `rotate(angle)`：旋轉元素。
  - `scale(x, y)`：縮放元素。
  - `translate(x, y)`：平移元素。
  - `skew(x-angle, y-angle)`：傾斜元素。
  - `matrix(a, b, c, d, e, f)`：2D 變換矩陣。
- 範例 24（[CSS 不同變形設置](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex24.html)）

  ```css
  .rotate-box {
    transform: rotate(45deg);
    background-color: #ffab91;
    padding: 20px;
    color: #ffffff;
  }

  .scale-box {
    transform: scale(1.5);
    background-color: #81c784;
    padding: 20px;
    color: #ffffff;
  }

  .translate-box {
    transform: translate(50px, 100px);
    background-color: #2196f3;
    padding: 20px;
    color: #ffffff;
  }

  .skew-box {
    transform: skew(20deg, 10deg);
    background-color: #ff7043;
    padding: 20px;
    color: #ffffff;
  }

  .matrix-box {
    transform: matrix(1, 0.5, -0.5, 1, 0, 0);
    background-color: #4caf50;
    padding: 20px;
    color: #ffffff;
  }
  ```

## 邊距折疊（Margin Collapsing）

當垂直方向相鄰的塊級元素的外邊距相遇時，會發生邊距折疊，最終外邊距值取決於最大的邊距值，而不是相加。

- 範例 25（[CSS 邊距折疊示意](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex25.html)）

  ```css
  .parent {
    background-color: #e0f7fa;
    padding: 20px;
    border: 1px solid #00796b;
  }

  .child1 {
    margin-bottom: 30px;
    background-color: #80deea;
    padding: 10px;
  }

  .child2 {
    margin-top: 20px;
    background-color: #4dd0e1;
    padding: 10px;
  }
  ```

## CSS 選擇器的優先權

當多個 CSS 規則應用到同一個元素時，瀏覽器會根據選擇器的優先權來決定最終應用哪個樣式。優先權從高到低如下：

1. 內聯樣式（最高優先權）
2. ID 選擇器
3. 類選擇器、屬性選擇器和偽類選擇器
4. 元素選擇器和偽元素選擇器
5. 通用選擇器（最低優先權）

- 範例 26（[CSS 優先權演示](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex26.html)）

  - 第一個段落中的 `span` 使用了類選擇器 `.highlight`，因此文字顏色為綠色。
  - 第二個段落有 ID 選擇器 `#unique`，因此文字顏色為紅色。
  - 第三個段落使用內聯樣式，文字顏色為橙色，這是最高優先權。

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <style>
        /* 通用選擇器 */
        * {
          color: black;
        }

        /* 元素選擇器 */
        p {
          color: blue;
        }

        /* 類選擇器 */
        .highlight {
          color: green;
        }

        /* ID 選擇器 */
        #unique {
          color: red;
        }
      </style>
    </head>
    <body>
      <p>這是一個 <span class="highlight">普通段落</span>。</p>
      <p id="unique">這是一個具有 ID 的段落。</p>
      <p style="color: orange;">這是一個內聯樣式的段落。</p>
    </body>
  </html>
  ```

## 響應式設計

響應式設計通過使用 **媒體查詢（Media Queries）** 來根據不同的設備和屏幕大小調整樣式。例如：

```css
@media (max-width: 768px) {
  .container {
    padding: 20px;
  }

  table {
    width: 100%;
  }
}
```

這樣，當屏幕寬度小於 768 像素時，表單容器的內邊距和表格寬度將自動調整，確保在手機等小屏設備上也能良好顯示。

- 範例 27（[CSS 響應式設計演示](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex27.html)）

  - 當瀏覽器窗口寬度大於 600 像素時，容器寬度為 80%，內邊距為 40px。
  - 當瀏覽器窗口寬度小於或等於 600 像素時，容器寬度變為 100%，內邊距減少為 20px。
  - 使用過渡效果 `transition: padding 0.3s ease;` 使內邊距的變化更加平滑。

  ```html
  <!DOCTYPE html>
  <html>
    <head>
      <style>
        .container {
          width: 80%;
          margin: 0 auto;
          background-color: #f9f9f9;
          padding: 40px;
          transition: padding 0.3s ease;
        }

        @media (max-width: 600px) {
          .container {
            width: 100%;
            padding: 20px;
          }
        }
      </style>
    </head>
    <body>
      <div class="container">
        <p>這是一個響應式容器。調整瀏覽器窗口大小以查看效果。</p>
      </div>
    </body>
  </html>
  ```

### 響應式佈局：Flexbox 與 Grid

#### Flexbox

- Flexbox 是一種一維佈局模型，用於在容器中對齊和分配空間給項目，即使它們的大小是動態和未知的。
- 主要屬性：
  - `display: flex;`：啟用 Flexbox。
  - `flex-direction`：設置主軸方向（`row`, `column`）。
  - `justify-content`：沿主軸對齊項目（`flex-start`, `flex-end`, `center`, `space-between`, `space-around`）。
  - `align-items`：沿交叉軸對齊項目（`flex-start`, `flex-end`, `center`, `stretch`）。
  - `flex-wrap`：設置是否換行（`nowrap`, `wrap`, `wrap-reverse`）。
- 應用場景：
  - 創建水平或垂直的彈性佈局。
  - 對齊和分配空間給項目。
- 範例 28（[CSS Flexbox 基本應用](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex28.html)）

  ```css
  .flex-container {
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    background-color: #f1f1f1;
    padding: 20px;
  }

  .flex-item {
    background-color: #4caf50;
    color: white;
    padding: 20px;
    margin: 10px;
    flex: 1;
    text-align: center;
  }
  ```

#### Grid

- Grid 是一種二維佈局模型，用於在容器中建立行和列的網格系統，並在這些網格中放置項目。
- 主要屬性：
  - `display: grid;`：啟用 Grid。
  - `grid-template-columns`：定義列的大小和數量。
  - `grid-template-rows`：定義行的大小和數量。
  - `gap`：設置行和列之間的間距。
  - `justify-items`：沿主軸對齊網格項目。
  - `align-items`：沿交叉軸對齊網格項目。
- 應用場景：

  - 創建複雜的網格佈局。
  - 控制元素在二維空間中的位置。

- 範例 29（[CSS Grid 基本應用](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/example/ex29.html)）

  ```css
  .grid-container {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    background-color: #ffecb3;
    padding: 20px;
  }

  .grid-item {
    background-color: #ffe082;
    padding: 20px;
    text-align: center;
    font-weight: bold;
  }
  ```

## 綜合實作

現在，我們將延伸上次的 HTML 表單，為其添加更多 CSS 樣式，使表單更加美觀和易用。
![img02](https://gainsborouo.github.io/NYCU_GDSC-Frontend/3_css/img/img02.png)

### 目標

1. 美化表單的佈局和樣式。
2. 增加頁面的整體美觀度。
3. 提升表單的可用性和使用者體驗。
4. 展示多樣化的 CSS 屬性應用。

### 實作步驟

1. 創建 CSS 文件  
   建立一個名為 `styles.css` 的文件，並在 HTML 文件的 `<head>` 區域引入。

   ```html
   <head>
     <title>個人資訊表單</title>
     <link rel="stylesheet" href="styles.css" />
   </head>
   ```

2. 設計頁面佈局  
   使用 CSS 調整表單的位置和大小，並為頁面添加背景色和字體樣式。

3. 美化表單元素  
   為輸入欄位、按鈕和其他表單元素添加樣式，使其更加統一和美觀。

4. 增加交互效果  
   使用過渡和變形效果，提升使用者體驗。
