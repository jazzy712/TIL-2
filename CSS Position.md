## CSS Position

- css layout
  
  - 각 요소의 **위치와 크기를 조정**하여 웹 페이지의 디자인 결정
  - display, position, flexbox ...

- css position
  
  - 요소를 normal flow에서 제거하여 다른 위치로 배치하는 것
  
  - 다른 요소 위에 올리기, 화면의 특정 위치에 고정시키기 ...

- position 목적
  
  - 전체 페이지에 대한 레이아웃을 구성하는 것보다는 **페이지 특정 항목의 위치 조정**

- position 이동 방향

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-09-37-39-image.png" title="" alt="" data-align="center">

## Position 유형

- position
  
  - static
  
  - relative
  
  - absolute
  
  - fixed
  
  - sticky

- position 활용

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-09-38-35-image.png" title="" alt="" data-align="center">

```css
 * {
      box-sizing: border-box;
    }

    body {
      height: 1500px;
    }

    .container {
      position: relative;
      height: 300px;
      width: 300px;
      border: 1px solid black;
    }

    .box {
      height: 100px;
      width: 100px;
      border: 1px solid black;
    }

    .static {
      position: static;
      background-color: lightcoral;
    }

    /* 본인의 원래 위치를 버리고 이동 */
    .absolute {
      position: absolute;
      background-color: lightgreen;
      top: 100px;
      left: 100px;
    }

    /* 본인의 원래 위치에서 이동 */
    .relative {
      position: relative;
      background-color: lightblue;
      /* top에 100의 값을 주는 것은 위에 100만큼의 여백을 주는 것이기에 아래로 간다 */
      top: 100px;
      left: 100px;
    }

    /* 화면이 바뀌더라도 위치 고정 */
    .fixed {
      position: fixed;
      background-color: gray;
      top: 0;
      right: 0;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box static">Static</div>
    <div class="box absolute">Absolute</div>
    <div class="box relative">Relative</div>
    <div class="box fixed">Fixed</div>
  </div>
```

- position 유형별 특징
  
  - static
    
    - 요소를 normal flow에 따라 배치
    
    - top, right, bottom, left 속성이 적용되지 않음
    
    - 기본 값
  
  - relative
    
    - 요소를 normal flowd에 따라 배치
    
    - 자신의 원래 위치(static)을 기준으로 이동
    
    - top, right, bottom, left 속성으로 위치 조정
    
    - 다른 요소의 레이아웃에 영향을 주지 않음(요소가 차지하는 공간은 static일 때와 같음)
  
  - absolute
    
    - 요소를 normal flow에서 제거
    
    - 가장 가까운 relative 부모 요소를 기준으로 이동
      
      - 만족하는 부모 요소가 없다면 body 태그를 기준
    
    - top, right, bottom, left 속성으로 위치 조정
    
    - 문서에서 요소가 차지하는 공간 없어짐
  
  ```css
     .card {
        position: relative;
        width: 300px;
        height: 200px;
        border: 1px solid black;
      }
  
      .card-content {
        padding: 10px;
      }
  
      .badge {
        position: absolute;
        top: 0;
        right: 0;
        background-color: red;
        color: white;
        padding: 5px 10px;
      }
    </style>
  </head>
  
  <body>
    <div class="card">
      <div class="card-content">
        <h3>Card Title</h3>
        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>
        <span class="badge">New</span>
      </div>
    </div>
  ```
  
  - fixed
    
    - 요소를 normal flow에서 제거
    
    - 현재 화면영역(viewport)를 기준으로 이동
    
    - 스크롤해도 항상 같은 위치에 유지
    
    - top, right, bottom, left 속성으로 위치 조정
    
    - 문서에서 요소가 차지하는 공간 없어짐
  
  - sticky
    
    - relative와 fixed 특성 결합한 속성
    
    - 스크롤 위치가 임계점에 도달하기 전에는 relative처럼 동작
    
    - 스크롤이 특정 임계점에 도달하면 fixed처럼 동작하여 화면에 고정
    
    - 만약 다음 sticky 요소가 나오면 다음 sticky 요소가 이전 sticky 요소의 자리를 대체
      
      - 이전 sticky 요소가 고정되어 있던 위치와 다음 sticky 요소가 고정되어야 할 위치가 겹치게 되기 때문
  
  ```css
   body {
        height: 1500px;
      }
  
      .sticky {
        position: sticky;
        top: 0;
        background-color: lightblue;
        padding: 20px;
        border: 2px solid black;
      }
    </style>
  </head>
  
  <body>
    <h1>Sticky positioning</h1>
    <div>
      <div class="sticky">첫 번째 Sticky</div>
      <div>
        <p>내용1</p>
        <p>내용2</p>
        <p>내용3</p>
      </div>
      <div class="sticky">두 번째 Sticky</div>
      <div>
        <p>내용4</p>
        <p>내용5</p>
        <p>내용6</p>
      </div>
      <div class="sticky">세 번째 Sticky</div>
      <div>
        <p>내용7</p>
        <p>내용8</p>
        <p>내용9</p>
      </div>
    </div>
  ```

## Z-Index

- z-index
  
  - 요소의 쌓임  순서(stack order)를 정의하는 속성
  
  - 정수 값을 사용해 z축 순서를 지정
  
  - 값이 클수록 요소가 위에 쌓이게 됨
  
  - static이 아닌 요소에만 적용

- 특징
  
  - 기본값은 auto
  
  - 부모 요소의 z-index 값에 영향을 받음
  
  - 같은 부모 내에서만 z-index 값을 비교
  
  - 부모의 z-index 가 낮으면 자식의 z-index가 아무리 높아도 부모보다 위로 올라갈 수 없음
  
  - z-index 값이 같으면 HTML 문서 순서대로 쌓임

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-10-12-42-image.png" title="" alt="" data-align="center">

```css
  .container {
      position: relative;
    }

    .box {
      position: absolute;
      width: 100px;
      height: 100px;
    }

    .red {
      background-color: red;
      top: 50px;
      left: 50px;
      z-index: 3;
    }

    .green {
      background-color: green;
      top: 100px;
      left: 100px;
      z-index: 2;
    }

    .blue {
      background-color: blue;
      top: 150px;
      left: 150px;
      z-index: 1;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="box red">z-index: 3</div>
    <div class="box green">z-index: 2</div>
    <div class="box blue">z-index: 1</div>
  </div>
```

## Margin Collapsing(마진 상쇄)

- 두 block 타입 요소의 margin top과 bottom이 만나 더 큰 margin으로 결합되는 현상

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-10-58-09-image.png" title="" alt="" data-align="center">

- 이유
  
  - 복잡한 레이아웃에서 요소 간 간격을 일관되게 유지하게 위함
  
  - 요소 간의 간격을 더 예측 가능하고 관리하기 쉽게 만듦
  
  - 일관성, 단순화

- 예시
  
  - 두 요소 모두 margin 20px 이지만 실제 두 요소의 상/하 공간은 40이 아닌 20으로 상쇄
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-11-00-36-image.png" title="" alt="" data-align="center">

## Box 타입 별 수평 정렬

- block 요소의 수평 정렬

- margin : auto 사용
  
  - 블록 요소의 너비를 지정하고 좌우 margin을 auto로 설정
  
  ```css
  .box {
        width: 100px;
        height: 100px;
        background-color: crimson;
        border: 1px solid black;
      }
  
      .margin-auto {
        margin: 0 auto;
      }
  ```

- text-align 사용
  
  - 부모 요소에 적용
  
  ```css
  .text-center {
        text-align: center;
      }
  ```
  
  ```css
  <div class="text-center">
      <span>inline 요소</span>
    </div>
  ```

- inline-block 요소의 수평 정렬
  
  - text align 사용
    
    - 부모 요소에 적용
  
  ```css
  .text-center {
        text-align: center;
      }
  
      .inline-block {
        display: inline-block;
      }
  ```
  
  ```css
  <div class="text-center">
      <div class="box inline-block"></div>
    </div>
  ```

## 실제 Position 활용 예시 - absolute

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-11-04-06-image.png" title="" alt="" data-align="center">

## 실제 Position 활용 예시 - fixed

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-11-04-29-image.png" title="" alt="" data-align="center">

## 실제  Position 활용 예시 - sticky

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-25-11-04-54-image.png" title="" alt="" data-align="center">
