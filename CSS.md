## Web Styling

- CSS(Cascading Style Sheet)
  
  - 웹 페이지의 **디자인**과 **레이아웃**을 구성하는 언어
  
  - 레이아웃은 배치. 문서의 좌측 상단부터 쌓아 나감
  
  - Cascade(계단식)
    
    - 한 요소에 동일한 가중치를 가진 선택자가 적용될 때 CSS에서 마지막에 나오는 선언이 사용
    
    - 예시
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-10-34-51-image.png" title="" alt="" data-align="center">

- CSS 구문

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-10-05-30-image.png" title="" alt="" data-align="center">

```css
h1 {
    color : red;
    font-size: 30px;
}
```

- 선언의 끝에는 **세미콜론(;)** 존재 -> 선언의 종료 의미

- CSS 적용 방법
  
  - Inline Style
    
    - HTML 요소 안에 style 속성 값으로 작성
  
  ```css
  <body>
    <h1>style="color: blue; background-color: yellow;"Hello World!</h1>
  ```
  
  - Internal(내부) Style
    
    - head 태그 안에 style 태그에 작성
  
  ```css
  <!DOCTYPE html>
  <html lang="en">
  
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
      h1 {
        color : blue;
        background-color: yellow;
      }
    </style>
  </head>
  ```
  
  - External(외부) Style
    
    - 별도 CSS 파일 생성 후 HTML link 태그를 사용해 불러오기
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-10-14-42-image.png" title="" alt="" data-align="center">

## ★CSS Selectors(선택자)★

- CSS Selectors
  
  - HTML 요소를 선택하여 스타일을 적용할 수 있도록 하는 선택자

- 종류
  
  - 기본 선택자
    
    - 전체(*) 선택자
    
    - 요소(tag) 선택자
    
    - 클래스(class) 선택자
    
    - 아이디(id) 선택자
    
    - 속성(attr) 선택자
  
  - 결합자(Combinators)
    
    - 자손 결합자(" "(space)
    
    - 자식 결합자(">")

- 특징
  
  - 전체  선택자(*)
    
    - HTML 모든 요소를 선택
  
  - 요소 선택자
    
    - 지정한 모든 태그 선택
  
  - 클래스 선택자('.'(dot))
    
    - 주어진 클래스 속성을 가진 모든 요소 선택
    
    - 재사용 목적
  
  - 아이디 선택자('#')
    
    - 주어진 아이디 속성을 가진 요소 선택
    
    - 문서에는 주어진 아이디를 가진 요소가 하나만 있어야 함
  
  - 우선순위가 존재

- CSS 결합자
  
  - 특징
    
    - 자손 결합자(" "(space))
      
      - 첫 번째 요소의 자손 요소들 선택
      
      - ex) p span은 <p> 안에 있는 모든 <span>를 선택(하위 레벨 상관없이)
    
    - 자식 결합자(">")
      
      - 첫 번째 요소의 직계 자식만 선택
      
      - ex) ul > li은 <ul> 안에 있는 모든 <li>를 선택(한 단계 아래 자식들만)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    /* 전체 선택자  */
    * {
      color: red;
    }
    /* 타입 선택자 */
    h2 {
      color : orange;
    }

    h3,
    h4 {
      color: blue;
    }
    /* 클래스 선택자 */
    .green {
      color: green;
    }
    /* id 선택자 */
    #purple {
      color : purple;
    }
    /* 자식 결합자 */
    .green > span {
      font-size: 50px;
    }
    /* 자손 결합자 */
    .green li {
      color: brown;
    }
  </style>
</head>

<body>
  <!-- a 태그는 p 태그의 자식이 아님.(들여쓰기만 한다 해서 자식이 되는게 아님) -->
   <!-- html에서는 들여쓰기가 문법상 필요한게 아님. 다만 가독성을 위해 필요 -->
  <p>aaa</p>
    <a href=""></a>
  <p></p>
  <h1 class="green">Heading</h1>
  <h2>선택자</h2>
  <h3>연습</h3>
  <h4>반가워요</h4>
  <p id="purple">과목 목록</p>
  <ul class="green">
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹
      <ol>
        <li>HTML</li>
        <li>CSS</li>
        <li>PYTHON</li>
      </ol>
    </li>
  </ul>
  <p class="green">Lorem, <span>ipsum</span> dolor.</p>
</body>

</html>
```

## Specificity(명시도)

- 명시도
  
  - 결과적으로 요소에 적용할 CSS 선언을 결정하기 위한 알고리즘
  
  - CSS Selector에 가중치를 계산하여 어떤 스타일을 적용할지 결정
  
  - 동일한 요소를 가리키는 2개 이상의 CSS 규칙이 있는 경우 가장 높은 명시도를 가진 Selector가 승리하여 스타일이 적용
  
  - 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-10-35-22-image.png" title="" alt="" data-align="center">
  
  - 명시도가 높은 순
    
    - Importance
      
      - -!important
    
    - Inline 스타일
    
    - 선택자
      
      - id 선택자 > class 선택자 > 요소 선택자
    
    - 소스 코드 선언 순서
  
  - **좁은 범위의 선택일수록 명시도가 높다**
  
  - **!important**
    
    - 다른 우선순위 규칙보다 우선하여 적용하는 키워드
    
    - Cascade의 구조를 무시하고 강제로 스타일을 적용하는 방식이므로 사용 권장하지 않음

## CSS 상속

- 상속
  
  - 기본적으로 CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속해 재사용성을 높임

- 속성 2가지 분류
  
  - 상속 되는 속성
    
    - text 관련 요소(font, color, text-align), opacity, visibility
  
  - 상속 되지않는 속성
    
    - box model 관련 요소(width, height, border, box-sizing)
    
    - position 관련 요소(position, top/right/bottom/left, z-index)

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
  <style>
    .parent {
      /* 상속 O */
      color: red;

      /* 상속 X */
      border: 1px solid black;
    }
  </style>
</head>

<body>
  <ul class="parent">
    <li class="child">Hello</li>
    <li class="child">Bye</li>
  </ul>
</body>

</html>
```

## CSS Box Model

- box model
  
  - 웹 페이지의 모든 HTML 요소 감싸는 사각형 상자 모델

- box type
  
  - block box
  
  - inline box
  
  - 박스 타입에 따라 페이지에서의 배치 흐름 및 다른 박스와 관련하여 박스가 동작하는 방식이 달라짐

- box display type
  
  - outer display type
  
  - inner display type

- Outer display type
  
  - block & inline
  
  ```html
  .index {
      display : block;
  }
  ```
  
  ```html
  .index {
      display : inline;
  }
  ```
  
  -  박스가 문서 흐름에서 어떻게 동작할지 결정
  
  - block 특징
    
    - 항상 새로운 행으로 나뉨
    
    - width와 height 속성 사용 가능
    
    - padding, margin, border 로 인해 다른 요소를 상자로부터 밀어냄
    
    - width 속성을 지정하지 않으면 박스는 inline 방향으로 사용 가능한 공간 모두 차지
      
      - 상위 컨테이너 너비 100%로 채우는 것
    
    - 대표적인 block 타입 태그
      
      - h1~6, p, div
  
  - inline 특징
    
    - 새로운 행으로 넘어가지 않음
    
    - width와 height 속성 사용 불가능
    
    - 수직 방향
      
      - padding, margin, border가 적용되지만 다른 요소 밀어낼 수 없음
    
    - 수평 방향
      
      - padding, margins, borders가 적용되어 다른 요소 밀어낼 수 있음
    
    - 대표적인 inline 타입 태그
      
      - a, img, span, strong, em

- Normal flow
  
  - 일반적인 흐름 또는 레이아웃을 변경하지 않은 경우
  
  - 웹 페이지 요소가 배치되는 방식

```html
  <h1>Normal
    flow</h1>
  <p>Lorem, ipsum dolor sit amet consect explicabo</p>
  <div>
    <p>block 요소는 기본적으로 부모 요소의 너비 100%를 차지하며, 자식 콘텐츠의 최대 높이를 취한다.</p>
    <p>block 요소의 총 너비와 총 높이는 content + padding + border width/height다.</p>
  </div>
  <p>block 요소는 서로 margins로 구분된다.</p>
  <p>inline 요소는 <span>이 것처럼</span> 자체 콘텐츠의 너비와 높이만 차지한다.
    그리고 inline 요소는 <a href="#">width나 height 속성을 지정 할 수 없다.</a>
  </p>
  <p>
    물론 이미지도 <img src="#"> 인라인 요소다.
    단, 이미지는 다른 inline 요소와 달리 width나 height로 크기를 조정할 수 있다.
  </p>
  <p>
    만약 inline 요소의 크기를 제어하려면 block 요소로 변경하거나 inline-block 요소로 설정해주어야 한다.
  </p>
```

```html
    a,
    span,
    img {
      border: 3px solid red;
    }

    h1,
    p,
    div {
      border: 1px solid blue;
    }
```

- Inner display type
  
  - flexbox
  
  ```css
  .container {
     display : flex;
  }
  ```
  
  - 박스 내부의 요소들이 어떻게 배치될지 결정
  
  - 속성 
    
    - flex



## CSS 스타일 가이드

- 코드 구조와 포맷팅
  
  - 일관된 들여쓰기 사용(보통 2칸 공백)
  
  - 선택자와 속성은 각각 새 줄에 작성
  
  - 중괄호 앞에 공백 넣기
  
  - 속성 뒤에는 콜론(:)과 공백 넣기
  
  - 마지막 속성 뒤에는 세미콜론(;) 넣기

- 선택자 사용
  
  - class 선택자 우선 사용
  
  - id, 요소 선택자 등은 가능한 기피
  
  - 여러 선택자들과 함께 사용할 경우 우선순위 규칙에 따라 예기치 못한 스타일 규칙이 적용되어 전반적 유지보수가 어려워지기 때문

- 속성과 값
  
  - 속성과 값은 소문자로 작성
  
  - 0 값에는 단위를 붙이지 않음

- 명명 규칙
  
  - 클래스 이름은 의미 있고 목적 나타내는 이름으로
  
  - 케밥 케이스(kebab case) 사용
  
  - 약어보다는 전체 단어 사용

- CSS 적용 스타일
  
  - inline 스타일 되도록 사용 x
  
  - CSS와 HTML 구조 정보 혼합되어 작성되기 때문에 코드를 이해하기 어렵게 만듦

- 모든 속성은 외우는 것이 아님


