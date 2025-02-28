## Bootstrap

- 정의
  
  - CSS 프론트엔드 프레임워크(Toolkit)
  
  - 미리 만들어진 다양한 디자인 요소들을 제공하여 웹 사이트를 빠르고 쉽게 개발할 수 있도록 함

- CDN(Content Delivery Network)
  
  - 지리적 제약 없이 빠르고 안전하게 콘텐츠를 전송할 수 있는 전송 기술
  
  - 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간 최소화(웹 페이지 로드 속도 높임)
  
  - 지리적으로 사용자와 가까운 CDN 서버에 콘텐츠를 저장해서 사용자에게 전달

- 기본 사용법
  
  - mt - 5 : {property}{sides}-{size}

```css
<p class="mt-5">Hello, world!</p>
```

- 클래스 이름으로 spacing 표현 방법

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-26-09-26-37-image.png" title="" alt="" data-align="center">

- 특정한 규칙이 있는 클래스 이름으로 스타일 및 레이아웃이 미리 작성되어 있음



## Reset CSS

- bootstrap 적용 전/후 비교

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-26-09-33-39-image.png" title="" alt="" data-align="center">

- reset CSS
  
  - 모든 HTML 요소 스타일을 일관된 기준으로 재설정하는 간결하고 압축된 규칙 세트
  
  - HTML Element, Table, List 등의 요소들에 일관성 있게 스타일을 적용시키는 기본 단계
  
  - 사용 배경
    
    - 모든 브라우저는 각자의 'user agent stylesheet'를 가지고 있음
      
      - 웹 사이트를 보다 읽기 편하게 하기 위해
    
    - 문제는 이 설정이 브라우저마다 상이하다는 것
    
    - 모든 브라우저에서 웹 사이트를 동일하게 보이게 만들어야 하는 개발자에겐 골치 아픈 일...
    
    - 모두 똑같은 스타일 상태로 만들고 스타일 개발을 시작하자!

- user-agent stylesheets
  
  - 모든 문서에 기본 스타일을 제공하는 기본 스타일 시트
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-26-09-37-57-image.png" title="" alt="" data-align="center">

- normalize CSS
  
  - reset CSS 방법 중 대표적인 방법
  
  - 웹 표준 기준으로 브라우저 중 하나가 불일치 한다면 차이가 있는 브라우저를 수정하는 방법
    
    - 경우에 따라 IE 또는 EDGE 브라우저는 표준에 따라 수정할 수 없는 경우도 있는데, 이 경우 IE 또는 EDGE의 스타일을 나머지 브라우저에 적용시킴

- bootstrap에서의 reset CSS
  
  - bootstrap은 bootstrap-reboot.css 라는 파일명으로 normalize.css 를 자체적으로 커스텀해서 사용하고 있음
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-26-09-42-17-image.png" title="" alt="" data-align="center">

## Bootstrap 활용

- typography
  
  - 제목, 본문 텍스트, 목록 등

- display headings
  
  - 기존 heading보다 더 눈에 띄는 제목이 필요할 경우(더 크고 약간 다른 스타일)
  
  ```css
  <!-- Display Heading -->
  <h1 class="display-1">Display 1</h1>
  <h1 class="display-2">Display 2</h1>
  <h1 class="display-3">Display 3</h1>
  <h1 class="display-4">Display 4</h1>
  <h1 class="display-5">Display 5</h1>
  <h1 class="display-6">Display 6</h1>
  ```

- Inline text elements
  
  - HTML inline 요소에 대한 스타일
  
  ```css
  <!-- Inline text elements -->
  <p>You can use the mark tag to <mark>highlight</mark> text.</p>
  <p><del>This line of text is meant to be treated as deleted text.</del></p>
  <p><s>This line of text is meant to be treated as no longer accurate.</s></p>
  <p><ins>This line of text is meant to be treated as an addition to the document.</ins></p>
  <p><u>This line of text will render as underlined.</u></p>
  <p><small>This line of text is meant to be treated as fine print.</small></p>
  <p><strong>This line rendered as bold text.</strong></p>
  <p><em>This line rendered as italicized text.</em></p>
  ```

- Lists
  
  - HTML list 요소에 대한 스타일
  
  ```css
  <!-- Lists -->
  <ul class="list-unstyled">
    <li>This is a list.</li>
    <li>It appears completely unstyled.</li>
    <li>Structurally, it's still a list.</li>
    <li>However, this style only applies to immediate child elements.</li>
    <li>Nested lists:
      <ul>
        <li>are unaffected by this style</li>
        <li>will still show a bullet</li>
        <li>and have appropriate left margin</li>
      </ul>
    </li>
    <li>This may still come in handy in some situations.</li>
  </ul>
  ```



## Colors

- bootstrap color system
  
  - bootstrap이 지정하고 제공하는 색상 시스템

- colors
  
  - text, border, background 및 다양한 요소에 사용하는 bootstrap의 색상 키워드
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-26-10-05-44-image.png" title="" alt="" data-align="center">
  
  ```css
  <!-- text colors -->
  <p class="text-primary">.text-primary</p>
  <p class="text-primary-emphasis">.text-primary-emphasis</p>
  <p class="text-secondary">.text-secondary</p>
  <p class="text-secondary-emphasis">.text-secondary-emphasis</p>
  <p class="text-success">.text-success</p>
  <p class="text-success-emphasis">.text-success-emphasis</p>
  <p class="text-danger">.text-danger</p>
  ```

- background colors
  
  ```css
  <!-- background colors -->
  <div class="p-3 mb-2 bg-primary text-white">.bg-primary</div>
  <div class="p-3 mb-2 bg-primary-subtle text-primary-emphasis">.bg-primary-subtle</div>
  <div class="p-3 mb-2 bg-secondary text-white">.bg-secondary</div>
  <div class="p-3 mb-2 bg-secondary-subtle text-secondary-emphasis">.bg-secondary-subtle</div>
  <div class="p-3 mb-2 bg-success text-white">.bg-success</div>
  <div class="p-3 mb-2 bg-success-subtle text-success-emphasis">.bg-success-subtle</div>
  <div class="p-3 mb-2 bg-danger text-white">.bg-danger</div>
  ```



## Component

- bootstrap component
  
  - bootstrap에서 제공하는 UI 관련 요소
    
    - 버튼, 네비게이션 바, 카드, 폼, 드롭다운 등
  
  - 대표 component
    
    - alerts, badges, buttons, **cards, navbar** 
    
    - carousel 설정 시 **위 id와 밑 data-bs-target 일치 시켜야 작동**
    
    - 여러 carousel 설정 시 id와 data-bs-target 세트 다른 이름으로 하면 각각 작동
    
    - modal도 마찬가지로 **위 data-bs-target와 밑 id 일치 시켜야 작동**
    
    - 여러 modal 설정 시 id와 data-bs-target 세트 다른 이름으로 하면 각각 작동
    
    - modal의 본문은 굳이 버튼과 함께 위치하지 않아도 된다. 보통 modal은 코드의 최하단에 몰아둠

- 이점
  
  - 일관된 디자인을 제공하여 웹 사이트의 구성 요소를 구축하는 데 유용하게 활용



## Semantic Web

- 정의
  
  - 웹 데이터를 의미론적으로 구조화된 형태로 표현하는 방식

- semantic in HTML
  
  - HTML 요소가 의미를 가진다는 것<<<<<<![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-26-10-53-20-image.png)


