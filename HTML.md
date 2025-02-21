## World Wide Web

- 인터넷으로 연결된 컴퓨터들이 정보를 공유하는 거대한 정보 공간

## Web

- Website, Web application 등을 통해 사용자들이 정보를 검색하고 상호 작용하는 기술

## Web site

- 인터넷에서 여러 개의 **Web page** 가 모인 것으로, 사용자들에게 정보나 서비스를 제공하는 공간

## Web page

- HTML, CSS 등의 웹 기술을 이용하여 만들어진, **"Web site" 를 구성하는 하나의 요소**

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-06-12-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-06-25-image.png" title="" alt="" data-align="center">

## HTML

- Hypertext Markup Language

- 웹 페이지의 **의미**와 **구조**를 정의하는 언어

- Hypertext
  
  - 웹 페이지를 다른 페이지로 연결하는 링크
  
  - 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
  
  - 비선형성/상호연결성/사용자 주도적 탐색

- Markup Language
  
  - 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
  
  - HTML, Markdown
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-11-16-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-11-29-image.png" title="" alt="" data-align="center">
  
  ## Structure of HTML
  
  - HTML 구조
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-12-31-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-13-23-image.png" title="" alt="" data-align="center">
  
  ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>Document</title>
  </head>
  <body> 
    <p>This is my page</p>
  </body>
  </html>
  ```
  
  - 들여쓰기를 통해 하위 구조 파악(Tab이 되어 있으면 하위 구성)
  
  - 메타 데이터 : 데이터에 대한 데이터(하위 데이터)

- HTML Element(요소)
  
  - 하나의 요소는 **여는 태그**와 **닫는 태그** 그리고 그 안의 **내용**으로 구성됨
  
  - 닫는 태그는 태그 이름 앞에 슬래시가 포함
    
    - 닫는 태그가 없는 태그도 존재
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-20-18-image.png" title="" alt="" data-align="center">

- HTML Attributes(속성)
  
  - 사용자가 원하는 기준에 맞도록 요소를 설정하거나 다양한 방식으로 요소의 동작을 조절하기 위한 값
  
  - 목적
    
    - 나타내고 싶지 않지만 추가적인 기능, 내용을 담고 싶을 때 사용
    
    - CSS에서 스타일 적용을 위해 해당 요소를 선택하기 위한 값으로 활용
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-21-37-image.png" title="" alt="" data-align="center">

- HTML Attributes 작성 규칙
  
  - 속성은 요소 이름과 속성 사이에 공백이 있어야 함
  
  - 하나 이상의 속성들이 있는 경우엔 속성 사이에 공백으로 구분
  
  - 속성 값은 열고 닫는 따옴표로 감싸야 함
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-22-54-image.png" title="" alt="" data-align="center">
  
  - HTML 예시

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>문단.</p>
  <a href="https://www.naver.com/">네이버로 이동</a>
  <img src="images/sample.png" alt="컴퓨터사진">
  <img src="https://random.imagecdn.app/500/150" alt="">
</body>
</html>
```

## HTML Text structure

- **텍스트 구조와 의미** 제공

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-21-09-47-16-image.png" title="" alt="" data-align="center">

- h1 요소는 텍스트를 크게만 만드는 것이 아닌 현재 **문서의 최상위 제목** 이라는 의미 부여

- 대표적인 HTML Text structure
  
  - Heading & Paragraphs
    
    - h1~6(숫자가 높아질수록 작아짐), p
  
  - Lists
    
    - ol, ul, li
  
  - Emphasis & Importance
    
    - em, strong

- 예시

```html
<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>

<body>
  <h1>Main Heading</h1>
  <h2>Sub Heading</h2>
  <p>This is my page</p>
  <p>This is <em>emphasis</em></p>
  <p>Hi <strong>my name</strong> is Air</p>
  <ol>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ol>
  <ul>
    <li>파이썬</li>
    <li>알고리즘</li>
    <li>웹</li>
  </ul>
</body>

</html>
```

## HTML 스타일 가이드

- 대소문자 구분
  
  - HTML을 대소문자를 구분하지 않지만, 소문자 사용 강력 권장
  
  - 태그명고 속성명 모두 소문자로 작성

- 속성 따옴표
  
  - 속성 값에는 큰 따옴표(")를 사용하는 것이 일반적

- 코드 구조와 포맷팅
  
  - 일관된 들여쓰기 사용(보통 2칸 공백)
  
  - 각 요소는 한 줄에 하나씩
  
  - 중첩된 요소는 한 단계 더 들여쓰기

- 공백 처리
  
  - HTML은 연속된 공백을 하나로 처리
  
  - enter키로 줄 바꿈을 해도 브라우저에서 인식하지 않음(줄 바꿈 태그 사용)

- 에러 출력 없음
  
  - HTML은 문법 오류가 있어도 별도의 에러 메시지 출력하지 않음
