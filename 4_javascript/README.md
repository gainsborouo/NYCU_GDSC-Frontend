# JavaScript 基礎入門教學

## 什麼是 JavaScript

JavaScript（簡稱 JS）是一種高級、解釋型的程式語言，廣泛應用於網頁開發中。它主要用於增加網頁的互動性和動態效果，使得網頁不僅僅是靜態的內容展示。JavaScript 可以在用戶端（瀏覽器）運行，也可以在伺服器端（如 Node.js）運行。

- 動態性：可以根據用戶的操作動態修改網頁內容。
- 互動性：實現用戶與網頁之間的交互，如表單驗證、動畫效果等。
- 多功能性：不僅限於前端開發，還可用於後端、桌面應用、移動應用等。

### JavaScript 的主要用途

- 表單驗證：在用戶提交表單前檢查輸入資料是否符合要求。
- 動態內容更新：無需刷新頁面即可更新部分內容，如即時搜尋、數據加載等。
- 動畫效果：創建視覺上吸引人的動畫和過渡效果。
- 與伺服器通信：使用 AJAX 技術與伺服器進行數據交換，實現更流暢的用戶體驗。

## JavaScript 基本語法

JavaScript 的基本語法包括變數宣告、數據類型、運算符、控制結構、函數等。了解這些基礎知識是學習 JavaScript 的第一步。

### 如何在 HTML 中使用 JavaScript

有三種方式將 JavaScript 應用到 HTML 中：

1. 內聯腳本（Inline Script）：直接在 HTML 元素的 `onclick`、`onchange` 等事件屬性中編寫 JavaScript 代碼。

   ```html
   <button onclick="alert('Hello, World!')">點擊我</button>
   ```

2. 內部腳本（Internal Script）：在 HTML 文件的 `<head>` 或 `<body>` 區域內使用 `<script>` 標籤定義 JavaScript 代碼。

   ```html
   <head>
     <script>
       function greet() {
         alert("Hello from internal script!");
       }
     </script>
   </head>
   <body>
     <button onclick="greet()">點擊我</button>
   </body>
   ```

3. 外部腳本（External Script）：將 JavaScript 代碼存放在獨立的 `.js` 文件中，並在 HTML 文件中使用 `<script>` 標籤引用。

   ```html
   <head>
     <script src="script.js"></script>
   </head>
   <body>
     <button onclick="greet()">點擊我</button>
   </body>
   ```

   ```javascript
   // script.js
   function greet() {
     alert("Hello from external script!");
   }
   ```

### 基本範例

以下是一個簡單的 JavaScript 範例，當用戶點擊按鈕時，會彈出一個提示框：

#### 範例 1（[JavaScript 基本範例](https://gainsborouo.github.io/NYCU_GDSC-Frontend/4_javascript/example/ex01.html)）

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <title>JavaScript 基本範例</title>
    <script>
      function showMessage() {
        alert("歡迎學習 JavaScript！");
      }
    </script>
  </head>
  <body>
    <button onclick="showMessage()">點擊我</button>
  </body>
</html>
```

### 變數與數據類型

#### 變數宣告

變數用於存儲數據，JavaScript 提供了三種關鍵字來宣告變數：

- `var`：ES5 之前的變數宣告方式，具有函數作用域。
- `let`：ES6 引入的變數宣告方式，具有塊級作用域。
- `const`：ES6 引入的常數宣告方式，一旦賦值後不能更改。

```javascript
// 使用 var
var name = "Alice";
console.log(name); // 輸出: Alice

// 使用 let
let age = 25;
console.log(age); // 輸出: 25

// 使用 const
const PI = 3.14159;
console.log(PI); // 輸出: 3.14159
```

### 數據類型

JavaScript 有多種數據類型，主要分為原始類型和複合類型。

#### 原始類型

- Number：數字類型，包括整數和浮點數。
- String：字符串類型，用於表示文本。
- Boolean：布林類型，只有 `true` 和 `false` 兩個值。
- Undefined：未定義類型，表示變數已宣告但尚未賦值。
- Null：空類型，表示變數沒有值。
- Symbol（ES6）：獨一無二的標識符。
- BigInt（ES2020）：用於表示非常大的整數。

#### 複合類型

- Object：對象類型，用於存儲多個值和複雜的數據結構。
- Array：陣列類型，用於存儲有序的數據集合。
- Function：函數類型，用於封裝可重複使用的代碼。

```javascript
// Number
let score = 100;
let temperature = -5.5;

// String
let greeting = "Hello, World!";
let name = "John Doe";

// Boolean
let isActive = true;
let isCompleted = false;

// Undefined
let address;
console.log(address); // 輸出: undefined

// Null
let selectedItem = null;

// Object
let person = {
  name: "Alice",
  age: 30,
  isStudent: false,
};

// Array
let colors = ["red", "green", "blue"];

// Function
function add(a, b) {
  return a + b;
}
```

### 運算符

運算符用於執行各種操作，如數學計算、比較、邏輯運算等。JavaScript 提供了豐富的運算符。

#### 算術運算符

- `+`：加法
- `-`：減法
- `*`：乘法
- `/`：除法
- `%`：取餘數
- `**`：指數運算

```javascript
let a = 10;
let b = 3;

console.log(a + b); // 13
console.log(a - b); // 7
console.log(a * b); // 30
console.log(a / b); // 3.333...
console.log(a % b); // 1
console.log(a ** b); // 1000
```

#### 比較運算符

- `==`：等於（值相等）
- `===`：全等於（值和類型都相等）
- `!=`：不等於
- `!==`：不全等於
- `>` ：大於
- `>` <：小於
- `>=`：大於等於
- `<=`：小於等於

```javascript
let x = 5;
let y = "5";

console.log(x == y); // true
console.log(x === y); // false
console.log(x != y); // false
console.log(x !== y); // true
console.log(x > 3); // true
console.log(x < 10); // true
```

#### 邏輯運算符

- `&&`：邏輯與（AND）
- `||`：邏輯或（OR）
- `!`：邏輯非（NOT）

```javascript
let isLoggedIn = true;
let hasPermission = false;

console.log(isLoggedIn && hasPermission); // false
console.log(isLoggedIn || hasPermission); // true
console.log(!isLoggedIn); // false
```

#### 其他運算符

- 賦值運算符 ：`=`, `+=`, `-=`, `*=`, `/=`, `%=` 等。

  ```javascript
  let count = 10;
  count += 5; // count = 15
  count -= 3; // count = 12
  ```

- 條件（三元）運算符：`condition ? exprIfTrue : exprIfFalse`

  ```javascript
  let age = 18;
  let status = age >= 18 ? "成年人" : "未成年人";
  console.log(status); // 成年人
  ```

## 控制結構

控制結構用於控制程式的執行流程，包括條件判斷和迴圈等。

### 條件判斷

#### if...else

根據條件執行不同的代碼塊。

```javascript
let score = 85;

if (score >= 90) {
  console.log("優秀");
} else if (score >= 70) {
  console.log("良好");
} else {
  console.log("及格");
}
// 輸出: 良好
```

#### switch

根據變數的不同值執行不同的代碼塊。

```javascript
let day = "星期一";

switch (day) {
  case "星期一":
    console.log("今天是星期一");
    break;
  case "星期二":
    console.log("今天是星期二");
    break;
  default:
    console.log("未知的星期");
}
// 輸出: 今天是星期一
```

#### 迴圈

- for 迴圈  
  重複執行代碼塊一定次數。

  ```javascript
  for (let i = 0; i < 5; i++) {
    console.log("數字：" + i);
  }
  // 輸出: 數字：0 到 數字：4
  ```

- while 迴圈  
  在條件為真時重複執行代碼塊。

  ```javascript
  let i = 0;
  while (i < 5) {
    console.log("數字：" + i);
    i++;
  }
  // 輸出: 數字：0 到 數字：4
  ```

- do...while 迴圈
  至少執行一次代碼塊，然後根據條件判斷是否繼續。

  ```javascript
  let i = 0;
  do {
    console.log("數字：" + i);
    i++;
  } while (i < 5);
  // 輸出: 數字：0 到 數字：4
  ```

- for...of 迴圈
  遍歷可迭代對象（如陣列、字符串）。

  ```javascript
  let colors = ["紅色", "綠色", "藍色"];

  for (let color of colors) {
    console.log(color);
  }
  // 輸出: 紅色、綠色、藍色
  ```

- for...in 迴圈
  遍歷對象的屬性。

  ```javascript
  let person = {
    name: "Alice",
    age: 30,
    city: "台北",
  };

  for (let key in person) {
    console.log(key + ": " + person[key]);
  }
  // 輸出: name: Alice、age: 30、city: 台北
  ```

### 函數

函數是可重複使用的代碼塊，用於執行特定的任務。JavaScript 支援多種定義函數的方式。

#### 函數宣告

- 函數聲明（Function Declaration）

```javascript
function greet(name) {
  return "Hello, " + name + "!";
}

console.log(greet("Alice")); // 輸出: Hello, Alice!
```

#### 函數表達式（Function Expression）

```javascript
const greet = function (name) {
  return "Hello, " + name + "!";
};

console.log(greet("Bob")); // 輸出: Hello, Bob!
```

#### 箭頭函數（Arrow Function）

```javascript
const greet = (name) => {
  return "Hello, " + name + "!";
};

console.log(greet("Charlie")); // 輸出: Hello, Charlie!
```

#### 參數與返回值

函數可以接受參數並返回結果。

```javascript
function add(a, b) {
  return a + b;
}

let sum = add(5, 3);
console.log(sum); // 輸出: 8
```

#### 函數作用域

函數內部定義的變數具有函數作用域，外部無法訪問。

```javascript
function testScope() {
  let message = "Hello, World!";
  console.log(message); // 輸出: Hello, World!
}

testScope();
console.log(message); // 錯誤: message 未定義
```

#### 高階函數

高階函數是接受函數作為參數或返回函數的函數。

```javascript
function greet(callback) {
  let message = callback("Alice");
  console.log(message);
}

greet(function (name) {
  return "Hello, " + name + "!";
});
// 輸出: Hello, Alice!
```

### 物件（Objects）

物件是 JavaScript 的核心概念，用於存儲相關數據和功能。物件由屬性和方法組成。

#### 創建物件

```javascript
let person = {
  name: "Alice",
  age: 30,
  greet: function () {
    console.log("Hello, " + this.name + "!");
  },
};

console.log(person.name); // 輸出: Alice
person.greet(); // 輸出: Hello, Alice!
```

#### 修改物件屬性

```javascript
person.age = 31;
person.city = "台北";

console.log(person.age); // 輸出: 31
console.log(person.city); // 輸出: 台北
```

### 方法（Methods）

物件內的函數稱為方法，用於操作物件的數據。

```javascript
let calculator = {
  add: function (a, b) {
    return a + b;
  },
  subtract: function (a, b) {
    return a - b;
  },
};

console.log(calculator.add(10, 5)); // 輸出: 15
console.log(calculator.subtract(10, 5)); // 輸出: 5
```

### this 關鍵字

`this` 指向物件本身，用於訪問物件的屬性和方法。

```javascript
let person = {
  name: "Alice",
  greet: function () {
    console.log("Hello, " + this.name + "!");
  },
};

person.greet(); // 輸出: Hello, Alice!
```

### 陣列（Arrays）

陣列用於存儲有序的數據集合。JavaScript 的陣列是動態且可以存儲不同類型的數據。

#### 創建陣列

```javascript
let fruits = ["蘋果", "香蕉", "橙子"];
console.log(fruits[0]); // 輸出: 蘋果
```

#### 常用陣列方法

- `push()`：在陣列末尾添加元素。

```javascript
fruits.push("葡萄");
console.log(fruits); // ["蘋果", "香蕉", "橙子", "葡萄"]
```

- `pop()`：移除並返回陣列末尾的元素。

```javascript
let lastFruit = fruits.pop();
console.log(lastFruit); // 葡萄
console.log(fruits); // ["蘋果", "香蕉", "橙子"]
```

- `shift()`：移除並返回陣列開頭的元素。

```javascript
let firstFruit = fruits.shift();
console.log(firstFruit); // 蘋果
console.log(fruits); // ["香蕉", "橙子"]
```

- `unshift()`：在陣列開頭添加元素。

```javascript
fruits.unshift("草莓");
console.log(fruits); // ["草莓", "香蕉", "橙子"]
```

- `forEach()`：遍歷陣列並對每個元素執行回調函數。

```javascript
fruits.forEach(function (fruit) {
  console.log(fruit);
});
// 輸出: 草莓、香蕉、橙子
```

- `map()`：創建一個新陣列，元素為回調函數的返回值。

```javascript
let upperFruits = fruits.map(function (fruit) {
  return fruit.toUpperCase();
});
console.log(upperFruits); // ["草莓", "香蕉", "橙子"]
```

- `filter()`：創建一個新陣列，包含所有通過回調函數測試的元素。

```javascript
let longFruits = fruits.filter(function (fruit) {
  return fruit.length > 2;
});
console.log(longFruits); // ["草莓", "香蕉", "橙子"]
```

- `find()`：返回第一個符合條件的元素。

```javascript
let foundFruit = fruits.find(function (fruit) {
  return fruit === "香蕉";
});
console.log(foundFruit); // 香蕉
```

#### 多維陣列

```javascript
let matrix = [
  [1, 2, 3],
  [4, 5, 6],
  [7, 8, 9],
];

console.log(matrix[1][2]); // 6
```

## DOM 操作（Document Object Model）

DOM 是表示 HTML 和 XML 文件的結構化表示，JavaScript 可以通過 DOM 操作來動態修改網頁內容和結構。

### 選取 DOM 元素

- `document.getElementById()`：根據 ID 選取元素。

  ```javascript
  let title = document.getElementById("title");
  ```

- `document.getElementsByClassName()`：根據類名選取元素。

  ```javascript
  let buttons = document.getElementsByClassName("btn");
  ```

- `document.getElementsByTagName()`：根據標籤名選取元素。

  ```javascript
  let paragraphs = document.getElementsByTagName("p");
  ```

- `document.querySelector()`：使用 CSS 選擇器選取第一個符合條件的元素。

  ```javascript
  let firstButton = document.querySelector(".btn");
  ```

- `document.querySelectorAll()`：使用 CSS 選擇器選取所有符合條件的元素。
  ```javascript
  let allButtons = document.querySelectorAll(".btn");
  ```

### 修改元素內容

- `innerHTML`：設置或獲取元素的 HTML 內容。

  ```javascript
  let content = document.getElementById("content");
  content.innerHTML = "<strong>這是加粗的文字。</strong>";
  ```

- `textContent`：設置或獲取元素的純文本內容。

  ```javascript
  let message = document.getElementById("message");
  message.textContent = "這是純文本內容。";
  ```

### 修改元素屬性

- `setAttribute()`：設置元素的屬性值。

  ```javascript
  let link = document.getElementById("myLink");
  link.setAttribute("href", "https://www.example.com");
  ```

- `getAttribute()`：獲取元素的屬性值。

  ```javascript
  let src = image.getAttribute("src");
  console.log(src);
  ```

- `classList`：添加、移除或切換元素的類名。

  ```javascript
  let box = document.getElementById("box");
  box.classList.add("active");
  box.classList.remove("hidden");
  box.classList.toggle("highlight");
  ```

### 創建和刪除元素

- `createElement()`：創建新元素。

  ```javascript
  let newDiv = document.createElement("div");
  newDiv.textContent = "這是一個新創建的 div。";
  document.body.appendChild(newDiv);
  ```

- `removeChild()`：刪除子元素。

  ```javascript
  let parent = document.getElementById("parent");
  let child = document.getElementById("child");
  parent.removeChild(child);
  ```

### 修改元素樣式

可以通過 style 屬性直接修改元素的 CSS 樣式。

```javascript
let box = document.getElementById("box");
box.style.backgroundColor = "#4caf50";
box.style.width = "200px";
box.style.height = "200px";
```

## 事件處理

事件是用戶與網頁互動的方式，如點擊、鍵盤輸入、鼠標移動等。JavaScript 可以監聽和處理這些事件，從而實現互動功能。

### 常見事件類型

- 點擊事件（click）：當用戶點擊元素時觸發。
- 滑鼠事件（mouseover, mouseout）：當滑鼠移入或移出元素時觸發。
- 鍵盤事件（keydown, keyup）：當用戶按下或鬆開鍵盤按鍵時觸發。
- 表單事件（submit, change）：當用戶提交表單或更改表單元素的值時觸發。
- 窗口事件（load, resize, scroll）：當窗口加載、調整大小或滾動時觸發。

### 添加事件監聽器

使用 `addEventListener()` 方法來添加事件監聽器。

```javascript
let button = document.getElementById("myButton");
button.addEventListener("click", function () {
  alert("按鈕被點擊了！");
});
```

### 事件處理函數

事件處理函數可以接受一個事件對象作為參數，該對象包含事件的相關信息。

```javascript
let input = document.getElementById("myInput");
input.addEventListener("keyup", function (event) {
  console.log("按下的鍵是：" + event.key);
});
```

### 事件委託

事件委託是一種利用事件冒泡機制來處理動態添加的元素事件的方法。

#### 範例 2（[JavaScript 點擊清單項目](https://gainsborouo.github.io/NYCU_GDSC-Frontend/4_javascript/example/ex02.html)）

```html
<ul id="myList">
  <li>項目 1</li>
  <li>項目 2</li>
</ul>
```

```javascript
let list = document.getElementById("myList");
list.addEventListener("click", function (event) {
  if (event.target && event.target.nodeName === "LI") {
    console.log("點擊了：" + event.target.textContent);
  }
});
```

## 綜合實作

現在，我們將延伸上次的 HTML 表單，為其添加更多 JavaScript 功能，使表單更加易用。
![img02](https://gainsborouo.github.io/NYCU_GDSC-Frontend/4_javascript/img/img01.png)

### 目標

1. 增加表單的即時驗證功能，確保用戶輸入的資料符合要求。
2. 提升頁面的互動性和使用者體驗。
3. 簡化表單提交過程，提高表單的可靠性。

### 實作步驟

1. 創建 CSS 文件  
   建立一個名為 `script.js` 的文件，並在 HTML 文件的 `<head>` 區域引入。

   ```html
   <head>
     <title>個人資訊表單</title>
     <link rel="stylesheet" href="styles.css" />
     <script src="script.js" defer></script>
   </head>
   ```

2. 添加基本驗證功能  
   在 JavaScript 文件中，添加代碼以驗證用戶輸入是否符合要求。例如，確保姓名不為空，電子郵件格式正確，年齡為正數等。

3. 處理表單提交事件  
   使用 JavaScript 監聽表單的提交事件，阻止不符合要求的表單提交，並顯示相應的錯誤訊息。

4. 增加交互效果  
   使用 JavaScript 增加一些簡單的交互效果，例如當用戶選擇某些選項時，顯示或隱藏相關的表單欄位。

5. 整合與測試  
   將 JavaScript 與現有的 HTML 和 CSS 進行整合，並測試表單的各項功能是否正常運作。
