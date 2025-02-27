# React 基礎入門教學

## 什麼是 React

React 是由 Facebook 開發和維護的一個開源 JavaScript 函式庫，用於構建用戶界面（UI）。它特別適用於構建單頁應用（SPA），並且以其高效、靈活和組件化的特性而聞名。

- 組件化：React 將 UI 分解為可重用的組件，每個組件都有自己的狀態和邏輯。
- 虛擬 DOM：React 使用虛擬 DOM 來高效地更新和渲染變更，提升性能。
- 單向數據流：數據在 React 中是單向流動的，這使得應用的數據管理更加簡單和可預測。
- JSX 語法：React 使用 JSX（JavaScript XML）來描述 UI，讓 HTML 和 JavaScript 更加緊密結合。

### React 的主要用途

- 構建單頁應用（SPA）：例如 Facebook、Instagram 等現代網頁應用。
- 開發移動應用：使用 React Native，可以構建跨平台的移動應用。
- 創建複雜的用戶界面：如儀表板、表單、數據展示等。

## React 基本概念

在開始編寫 React 程式碼之前，我們需要了解一些基本概念和工具。

### 什麼是組件

組件是 React 的核心概念。每個組件都是一個獨立的、可重用的 UI 單位，並且可以包含自己的狀態和邏輯。組件可以分為兩種類型：

- 函數組件（Function Components）：使用 JavaScript 函數來定義。
- 類組件（Class Components）：使用 ES6 類來定義（推薦使用函數組件和 Hooks）。

## JSX 語法

JSX 是一種 JavaScript 的擴展語法，允許你在 JavaScript 代碼中編寫類似 HTML 的標記。這使得編寫和理解 UI 組件更加直觀。

```jsx
const element = <h1>Hello, World!</h1>;
```

### Props 和 State

Props（屬性）：用於向組件傳遞數據，類似於函數的參數。Props 是只讀的，不能在組件內部修改。
State（狀態）：用於管理組件內部的數據和狀態。State 是可變的，可以通過 setState（類組件）或 Hooks（函數組件）來更新。

## 開發環境設置

要開始使用 React，我們需要安裝一些工具和依賴。最簡單的方法是使用 Create React App 來初始化一個新的 React 項目。

### 安裝 Node.js 和 npm

首先，確保你的電腦已經安裝了 Node.js 和 npm。你可以從 Node.js 官方網站 下載並安裝最新的 LTS 版本。

檢查安裝是否成功：

```sh
node -v
npm -v
```

### 創建 React 應用

使用 Create React App 創建一個新的 React 項目：

```sh
npx create-react-app my-react-app
cd my-react-app
npm start
```

這將啟動開發伺服器，並在瀏覽器中打開 http://localhost:3000，你將看到 React 的歡迎頁面。

### 文件結構

創建的 React 項目包含以下主要文件和資料夾：

- `public/`：包含靜態資源，如 `index.html`。
- `src/`：包含 React 組件和應用程式的源代碼。
- `App.jsx`：主應用組件。
- `main.jsx`：應用的入口點。

## React 基本語法

### 建立函數組件

函數組件是一種用 JavaScript 函數定義的 React 組件。它接收 props 作為參數，並返回 JSX。

```jsx
// src/components/Greeting.jsx
import React from "react";

function Greeting(props) {
  return <h1>Hello, {props.name}!</h1>;
}

export default Greeting;
```

### 使用組件

在主應用組件中使用 Greeting 組件：

```jsx
// src/App.jsx
import React from "react";
import Greeting from "./components/Greeting";

function App() {
  return (
    <div className="App">
      <Greeting name="Alice" />
      <Greeting name="Bob" />
    </div>
  );
}

export default App;
```

### JSX 語法詳解

JSX 允許你在 JavaScript 中編寫類似 HTML 的標記。以下是一些 JSX 的基本規則：

- 標籤必須閉合：所有的元素必須有閉合標籤。

  ```jsx
  <img src="image.png" alt="圖片" />
  ```

- 使用大寫字母開頭的組件名稱：React 會區分內建的 HTML 元素和自定義的組件。

  ```jsx
  <Greeting />
  ```

- 表達式嵌入：可以在 JSX 中使用 {} 包含 JavaScript 表達式。

  ```jsx
  <h1>{`Hello, ${name}!`}</h1>
  ```

### 狀態管理（State）

在函數組件中使用 Hook 來管理狀態。`useState` 是最常用的 Hook，用於在函數組件中添加狀態。

```jsx
// src/components/Counter.jsx
import React, { useState } from "react";

function Counter() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>當前計數：{count}</p>
      <button onClick={() => setCount(count + 1)}>增加</button>
      <button onClick={() => setCount(count - 1)}>減少</button>
    </div>
  );
}

export default Counter;
```

在 `App.jsx` 中使用 `Counter` 組件：

```jsx
// src/App.jsx
import React from "react";
import Counter from "./components/Counter";

function App() {
  return (
    <div className="App">
      <Counter />
    </div>
  );
}

export default App;
```

## 處理事件

React 使用合成事件來處理用戶交互。合成事件的行為類似於瀏覽器的原生事件，但具有跨瀏覽器的一致性。

### 事件處理範例

```jsx
// src/components/ClickButton.jsx
import React from "react";

function ClickButton() {
  const handleClick = () => {
    alert("按鈕被點擊了！");
  };

  return <button onClick={handleClick}>點擊我</button>;
}

export default ClickButton;
```

在 `App.jsx` 中使用 `ClickButton` 組件：

```jsx
// src/App.jsx
import React from "react";
import ClickButton from "./components/ClickButton";

function App() {
  return (
    <div className="App">
      <ClickButton />
    </div>
  );
}

export default App;
```

### 傳遞事件對象

事件處理函數可以接收一個事件對象，該對象包含事件的相關信息。

```jsx
// src/components/InputHandler.jsx
import React, { useState } from "react";

function InputHandler() {
  const [value, setValue] = useState("");

  const handleChange = (event) => {
    setValue(event.target.value);
    console.log("輸入的值是：", event.target.value);
  };

  return (
    <div>
      <input type="text" value={value} onChange={handleChange} />
      <p>當前輸入：{value}</p>
    </div>
  );
}

export default InputHandler;
```

在 `App.jsx` 中使用 `InputHandler` 組件：

```jsx
// src/App.jsx
import React from "react";
import InputHandler from "./components/InputHandler";

function App() {
  return (
    <div className="App">
      <InputHandler />
    </div>
  );
}

export default App;
```

## 管理表單

表單是用戶輸入數據的重要途徑。在 React 中，我們可以使用受控組件來管理表單數據。

### 建立受控表單組件

以下是一個簡單的個人資訊表單，包含姓名、電子郵件和年齡的輸入欄位，並進行基本驗證。

```jsx
// src/components/InfoForm.jsx
import React, { useState } from "react";
import "./InfoForm.css"; // 引入樣式

function InfoForm() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    age: "",
    gender: "",
    hobbies: [],
    bio: "",
  });

  // ...
}

export default InfoForm;
```

### 樣式文件（CSS）

為了讓表單美觀，我們可以使用 CSS 來設計樣式。以下是與之前提供的 CSS 類似的樣式，但在 React 中，我們將其放在獨立的 CSS 文件中。

```css
/* src/components/InfoForm.css */
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

.container {
  max-width: 600px;
  margin: 20px auto;
  background-color: #ffffff;
  padding: 30px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

/* ... */
```

### 使用表單組件

將 `InfoForm` 組件添加到 `App.jsx` 中：

```jsx
// src/App.jsx
import React from "react";
import InfoForm from "./components/InfoForm";

function App() {
  return (
    <div className="App">
      <InfoForm />
    </div>
  );
}

export default App;
```

## 使用 React Router 進行頁面導航

在現代應用中，頁面導航是不可或缺的。React Router 是一個強大的路由庫，幫助我們在 React 應用中實現客戶端路由。

### 安裝 React Router

使用 npm 安裝 React Router：

```sh
npm install react-router-dom
```

### 設置路由

以下是一個簡單的路由設置範例，包含首頁和表單頁面：

```jsx
// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import InfoForm from "./components/InfoForm";
import Home from "./components/Home";

function App() {
  return (
    <Router>
      <nav>
        <ul>
          <li>
            <Link to="/">首頁</Link>
          </li>
          <li>
            <Link to="/form">個人資訊表單</Link>
          </li>
        </ul>
      </nav>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/form" element={<InfoForm />} />
      </Routes>
    </Router>
  );
}

export default App;
```

### 建立首頁組件

```jsx
// src/components/Home.jsx
import React from "react";

function Home() {
  return (
    <div className="container">
      <h1>歡迎來到 React 教學</h1>
      <p>這是一個簡單的 React 應用範例。</p>
    </div>
  );
}

export default Home;
```

### 更新樣式

為了讓導航欄更美觀，我們可以在 `InfoForm.css` 中添加一些樣式，或者創建一個新的 CSS 文件。例如：

```css
/* src/components/Nav.css */
nav {
  background-color: #4caf50;
  padding: 10px;
}

nav ul {
  list-style: none;
  display: flex;
  justify-content: center;
}

/* ... */
```

在 `App.jsx` 中引入導覽列樣式：

```jsx
// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import InfoForm from "./components/InfoForm";
import Home from "./components/Home";
import "./App.css";
import "./components/Nav.css"; // 引入導覽列樣式

// ...
```

現在你應該可以在導航欄之間切換不同的頁面。

## 使用狀態管理庫

當應用變得更加複雜時，管理狀態可能會變得困難。React 提供了多種狀態管理方案，如 Context API 和 Redux。在這裡，我們將簡要介紹 Context API。

### 使用 Context API

Context API 允許我們在組件樹中共享數據，而無需手動通過每一層的 props 傳遞。

#### 創建 Context

```jsx
// src/context/UserContext.jsx
import React, { createContext, useState } from "react";

export const UserContext = createContext();

export function UserProvider({ children }) {
  const [user, setUser] = useState(null);

  return (
    <UserContext.Provider value={{ user, setUser }}>
      {children}
    </UserContext.Provider>
  );
}
```

#### 使用 Context

```jsx
// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import InfoForm from "./components/InfoForm";
import Home from "./components/Home";
import { UserProvider } from "./context/UserContext";
import "./App.css";
import "./components/Nav.css";

function App() {
  return (
    <UserProvider>
      <Router>
        <nav>
          <ul>
            <li>
              <Link to="/">首頁</Link>
            </li>
            <li>
              <Link to="/form">個人資訊表單</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/form" element={<InfoForm />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
```

在組件中使用 Context：

```jsx
// src/components/Home.jsx
import React, { useContext } from "react";
import { UserContext } from "../context/UserContext";

function Home() {
  const { user } = useContext(UserContext);

  return (
    <div className="container">
      <h1>歡迎{user ? " " + user.name + " " : ""}來到 React 教學</h1>
      <p>這是一個簡單的 React 應用範例。</p>
    </div>
  );
}

export default Home;
```

在 `InfoForm` 組件中設置用戶信息：

```jsx
// src/components/InfoForm.jsx
import React, { useState, useContext } from "react";
import "./InfoForm.css";
import { UserContext } from "../context/UserContext";

function InfoForm() {
  const { setUser } = useContext(UserContext);
  // ...

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (validationErrors.length > 0) {
      setErrors(validationErrors);
    } else {
      setErrors([]);
      // 設置用戶信息
      setUser({
        name: formData.name,
        email: formData.email,
        age: formData.age,
        gender: formData.gender,
        hobbies: formData.hobbies,
        bio: formData.bio,
      });
      alert("表單提交成功！");
      console.log(formData);
    }
  };

  // ...
}

export default InfoForm;
```

如此一來，提交表單後首頁就會顯示用戶的姓名。

## 使用效果（useEffect）

useEffect Hook 允許你在函數組件中執行副作用，例如數據抓取、訂閱或手動 DOM 操作。

### 基本使用

```jsx
// src/components/DataFetcher.jsx
import React, { useState, useEffect } from "react";

function DataFetcher() {
  const [data, setData] = useState(null);

  useEffect(() => {
    // 模擬數據抓取
    setTimeout(() => {
      setData("這是從伺服器抓取的數據。");
    }, 2000);
  }, []); // 空依賴陣列表示只在組件掛載時執行一次

  return (
    <div className="container">
      <h1>數據抓取範例</h1>
      {data ? <p>{data}</p> : <p>加載中...</p>}
    </div>
  );
}

export default DataFetcher;
```

在 `App.jsx` 中使用 `DataFetcher` 組件：

```jsx
// src/App.jsx
import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import InfoForm from "./components/InfoForm";
import Home from "./components/Home";
import DataFetcher from "./components/DataFetcher";
import { UserProvider } from "./context/UserContext";
import "./App.css";
import "./components/Nav.css";

function App() {
  return (
    <UserProvider>
      <Router>
        <nav>
          <ul>
            <li>
              <Link to="/">首頁</Link>
            </li>
            <li>
              <Link to="/form">個人資訊表單</Link>
            </li>
            <li>
              <Link to="/data">數據抓取</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/form" element={<InfoForm />} />
          <Route path="/data" element={<DataFetcher />} />
        </Routes>
      </Router>
    </UserProvider>
  );
}

export default App;
```

訪問 `/data` 路徑，你將看到數據抓取的範例。

## React 的核心觀念

### 虛擬 DOM

虛擬 DOM（Virtual DOM） 是 React 最重要的特性之一。它是一個輕量級的 JavaScript 對象，模擬了真實 DOM 的結構。React 使用虛擬 DOM 來提高應用的性能，具體工作原理如下：

- 初始渲染：當 React 組件首次渲染時，會創建虛擬 DOM 的表示，並將其轉換為真實 DOM。
- 更新狀態：當組件的狀態或屬性（props）發生改變時，React 會重新渲染虛擬 DOM。
- 比較差異：React 會將新的虛擬 DOM 與之前的虛擬 DOM 進行比較，找出需要更新的部分。
- 批量更新：React 最後僅更新那些必要的真實 DOM 節點，減少不必要的操作，提高性能。

![img01](https://gainsborouo.github.io/NYCU_GDSC-Frontend/5_react/img/img01.png)

### 組件生命週期

組件生命週期是指一個 React 組件從創建到銷毀的過程。雖然在函數組件中，生命週期管理主要通過 Hooks 實現，但了解類組件的生命週期方法對於理解 React 的運作仍然非常有幫助。

主要生命週期方法：

1. 掛載階段（Mounting）

   - `constructor()`: 初始化組件狀態。
   - `componentDidMount()`: 組件掛載後立即調用，適合進行數據抓取或訂閱等操作。

2. 更新階段（Updating）

   - `shouldComponentUpdate()`: 判斷是否需要重新渲染組件。
   - `componentDidUpdate()`: 組件更新後調用，可以進行 DOM 操作或數據更新。

3. 卸載階段（Unmounting）

   - `componentWillUnmount()`: 組件卸載前調用，用於清理訂閱或計時器等資源。

在函數組件中，`useEffect` Hook 可用於模擬這些生命週期方法。

### 數據流與單向數據流

單向數據流（Unidirectional Data Flow） 是 React 的核心概念之一。數據在 React 中是單向流動的，從父組件流向子組件。這使得應用的數據管理更加簡單和可預測。

數據流示意圖：

```
父組件
↓
子組件
↓
孫組件
```

在這個模型中，子組件無法直接修改父組件的狀態。若需要子組件影響父組件的狀態，通常會通過回調函數來實現。

雙向數據流（如在某些其他框架中常見的）允許數據在組件之間雙向流動，但這可能會導致數據難以追蹤和管理。React 的單向數據流有助於保持應用的可維護性和穩定性。

## 單頁應用（SPA）概述

### SPA 與 MPA 的比較

單頁應用（Single Page Application, SPA） 和 多頁應用（Multi-Page Application, MPA） 是現代網頁應用的兩種主要架構。

| **特點**         | **SPA**                                     | **MPA**                                    |
| ---------------- | ------------------------------------------- | ------------------------------------------ |
| **頁面切換方式** | 客戶端路由，不刷新整個頁面                  | 伺服器路由，每次切換刷新整個頁面           |
| **用戶體驗**     | 更流暢，類似桌面應用                        | 類似傳統網站，頁面切換時有刷新感           |
| **初始加載時間** | 較長（載入所有必要的資源）                  | 較短（僅載入當前頁面的資源）               |
| **SEO 支援**     | 需要額外配置（如伺服器端渲染）              | 天生支援 SEO                               |
| **開發複雜度**   | 更高，需要處理客戶端路由和狀態管理          | 較低，傳統的頁面結構較為簡單               |
| **數據抓取**     | 通常使用 AJAX 或 Fetch API 進行動態數據抓取 | 每個頁面由伺服器直接渲染，數據抓取相對簡單 |

### SPA 的優點與挑戰

#### 優點

1. 流暢的用戶體驗：由於頁面不需要重新加載，用戶體驗更為流暢。
2. 高效的資源利用：只需載入一次應用的基本資源，後續的頁面切換僅需更新必要的數據。
3. 豐富的互動性：更容易實現複雜的用戶交互和動畫效果。
4. 前後端分離：前端和後端可以獨立開發，提高開發效率。

#### 挑戰

1. SEO 優化：由於內容主要由 JavaScript 渲染，搜索引擎可能無法正確索引內容。解決方案包括使用伺服器端渲染（SSR）或靜態站點生成（SSG）。
2. 初始加載時間：由於需要加載更多的 JavaScript 資源，初始加載時間可能較長。可通過代碼分割和懶加載來優化。
3. 瀏覽器兼容性：需要確保應用在不同瀏覽器上的兼容性。
4. 路由管理：需要妥善管理客戶端路由，避免路由衝突和錯誤。

### SPA 示意圖

![img02](https://gainsborouo.github.io/NYCU_GDSC-Frontend/5_react/img/img02.png)

## React 的性能優化

在構建 React 應用時，性能優化是不可忽視的一環。以下是幾種常見的性能優化方法：

### Code Splitting

代碼分割（Code Splitting） 是指將應用的代碼拆分成更小的塊，按需載入，從而減少初始加載時間。

實現方式：

使用 `React.lazy` 和 `Suspense` 來實現組件的懶加載。

```jsx
import React, { Suspense, lazy } from "react";

const LazyComponent = lazy(() => import("./LazyComponent"));

function App() {
  return (
    <div>
      <Suspense fallback={<div>Loading...</div>}>
        <LazyComponent />
      </Suspense>
    </div>
  );
}

export default App;
```

### Memoization

Memoization 是指緩存組件的渲染結果，避免不必要的重新渲染。React 提供了 `React.memo` 和 `useMemo` 來實現這一功能。

使用 `React.memo`：

```jsx
const MyComponent = React.memo(function MyComponent(props) {
  /* 組件內容 */
});
```

使用 `useMemo`：

```jsx
Copy code
const memoizedValue = useMemo(() => computeExpensiveValue(a, b), [a, b]);
```

### Lazy Loading

懶加載（Lazy Loading） 是指按需載入資源，如圖片或其他媒體文件，提升應用的加載速度。

實現方式：

可以使用瀏覽器的原生 `loading="lazy"` 屬性，或使用第三方庫如 `react-lazyload`。

```jsx
<img src="image.jpg" alt="描述" loading="lazy" />
```

## React 與其他框架的比較

| **特點**     | **React**                               | **Angular**                  | **Vue**                       |
| ------------ | --------------------------------------- | ---------------------------- | ----------------------------- |
| **類型**     | 函式庫                                  | 完整框架                     | 框架                          |
| **開發者**   | Facebook                                | Google                       | Evan You（前 Google 工程師）  |
| **語言**     | JavaScript（支持 TypeScript）           | TypeScript                   | JavaScript（支持 TypeScript） |
| **虛擬 DOM** | 是                                      | 否（直接操作 DOM）           | 是                            |
| **學習曲線** | 中等（基礎容易，進階需要理解 Hooks 等） | 陡峭（功能豐富，概念複雜）   | 緩和（文檔友好，概念簡單）    |
| **生態系統** | 廣泛（豐富的庫和工具）                  | 廣泛（內建豐富功能）         | 快速增長（良好的生態系統）    |
| **使用場景** | 靈活，適用於各種應用                    | 大型企業應用，需全面解決方案 | 中小型應用，快速開發          |

### 選擇建議

- React：適合需要高度自定義和靈活性的應用，並且有豐富的第三方庫支持。
- Angular：適合大型企業應用，需全面的框架解決方案，內建強大的功能。
- Vue：適合中小型應用，學習曲線相對平緩，易於上手。
