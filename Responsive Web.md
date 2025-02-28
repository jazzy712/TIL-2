## Responsive Web

- bootstrap grid system
  
  - 웹 페이지의 레이아웃을 조정하는데 사용되는 12개의 컬럼으로 구성된 시스템
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-03-43-image.png" title="" alt="" data-align="center">
  
  - 목적
    
    - 반응형 디자인을 지원해 웹 페이지를 모바일, 태블릿, 데스크탑 등 다양한 기기에서 적절하게 표시할 수 있도록 도움

- responsive web design(반응형 웹 디자인)
  
  - 디바이스 종류나 화면 크기에  상관없이, 어디서든 일관된 레이아웃 및 사용자 경험을 제공하는 디자인 기술
  
  - bootstrap grid system에서는 12개 column과 **6개 breakpoint**를 사용하여 반응형 웹 디자인 구현

## Grid system 구조

- grid system 기본 요소
  
  - container
    
    - column들을 담고 있는 공간
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-05-30-image.png" title="" alt="" data-align="center">
  
  - column
    
    - 실제 컨텐츠 포함하는 부분
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-06-06-image.png" title="" alt="" data-align="center">
  
  - gutter
    
    - 컬럼과 컬럼 사이의 여백 영역(상하좌우)
  
  <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-06-42-image.png" alt="" data-align="center">
  
  - 1개의 row안에 12개의 column 영역이 구성
    
    - 각 요소는 12개 중 몇 개를 차지할 것인지 지정
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-08-26-image.png" title="" alt="" data-align="center">
  
  ```css
    <div class="container">
      <div class="row">
        <div class="col-4"></div>
        <div class="col-4"></div>
        <div class="col-4"></div>
      </div>
    </div>
  ```

- grid system 실습
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-15-05-image.png" title="" alt="" data-align="center">
  
  ```css
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="box">col</div>
        </div>
        <div class="col">
          <div class="box">col</div>
        </div>
        <div class="col">
          <div class="box">col</div>
        </div>
      </div>
      <div class="row">
        <div class="col-4">
          <div class="box">col-4</div>
        </div>
        <div class="col-4">
          <div class="box">col-4</div>
        </div>
        <div class="col-4">
          <div class="box">col-4</div>
        </div>
      </div>
      <div class="row">
        <div class="col-2">
          <div class="box">col-2</div>
        </div>
        <div class="col-8">
          <div class="box">col-8</div>
        </div>
        <div class="col-2">
          <div class="box">col-2</div>
        </div>
      </div>
    </div>  
  ```
  
  - 중첩(Nesting)
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-25-28-image.png" title="" alt="" data-align="center">
  
  ```css
    <div class="container">
      <div class="row">
        <div class="col-4 box">
          <div>col-4</div>
        </div>
        <div class="col-8 box">
          <div class="row">
            <div class="col-6">
              <div class="box">col-6</div>
            </div>
            <div class="col-6">
              <div class="box">col-6</div>
            </div>
            <div class="col-6">
              <div class="box">col-6</div>
            </div>
            <div class="col-6">
              <div class="box">col-6</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  ```
  
  - 상쇄(Offset)
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-31-52-image.png" title="" alt="" data-align="center">
  
  ```css
  <div class="container">
      <div class="row">
        <div class="col-4">
          <div class="box">col-4</div>
        </div>
        <div class="col-4 offset-4">
          <div class="box">col-4 offset-4</div>
        </div>
      </div>
      <div class="row">
        <div class="col-3 offset-3">
          <div class="box">col-3 offset-3</div>
        </div>
        <div class="col-3 offset-3">
          <div class="box">col-3 offset-3</div>
        </div>
      </div>
      <div class="row">
        <div class="col-6 offset-3">
          <div class="box">col-6 offset-3</div>
        </div>
      </div>
    </div>
  ```
  
  - gutter
    
    - grid system에서 column 사이에 여백 영역
    
    - x축은 **padding**, y축은 **margin**으로 여백 생성
    
    - 0~5 까지 가능
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-37-22-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-09-37-37-image.png" title="" alt="" data-align="center">
  
  ```css
    <h2 class="text-center">Gutters(gx-0)</h2>
    <div class="container">
      <div class="row gx-0">
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  ```
  
  ```css
  <h2 class="text-center">Gutters(gy-5)</h2>
    <div class="container">
      <div class="row gy-5">
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  ```
  
  ```css
  <h2 class="text-center">Gutters(g-5)</h2>
    <div class="container">
      <div class="row g-5">
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
        <div class="col-6">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  ```

## Grid system Breakpoints

- 정의
  
  - 웹 페이지를 다양한 화면 크기에서 적절하게 배치하기 위한 분기점
  
  - 화면 너비에 따라 6개의 분기점 제공(xs, sm, md, lg, xl, xxl)
  
  - grid system은 화면 크기에 따라 12개의 칸을 각 요소에 나누어 주는 것
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-10-02-53-image.png" title="" alt="" data-align="center">
  
  - 각 breakpoints 마다 설정된 최대 너비 값 **"이상으로"** 화면이 커지면 grid sysyerm 동작이 변경됨

- breakpoints 실습
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-10-17-38-image.png" title="" alt="" data-align="center">
  
  ```css
  <h2 class="text-center">Breakpoints</h2>
    <div class="container">
      <div class="row">
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-8 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-2 col-lg-3 col-xl-4">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-6 col-md-12 col-lg-3 col-xl-12">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-27-10-18-13-image.png" title="" alt="" data-align="center">
  
  ```css
  <h2 class="text-center">Breakpoints + offset</h2>
    <div class="container">
      <div class="row g-4">
        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-4 col-md-6">
          <div class="box">col</div>
        </div>
        <div class="col-12 col-sm-4 col-md-6 offset-sm-4 offset-md-0">
          <div class="box">col</div>
        </div>
      </div>
    </div>
  ```

## CSS Layout 정리

- 정리
  
  - CSS 레이아웃 기술들은 각각 고유한 특성과 장단점 가지고 있음
  
  - 상호 보완적이며, 특정 상황에 따라 적합한 도구 달라짐
  
  - 최적의 기술 선택하고 효과적으로 활용하기 위해서는 다양한 실제 개발 경험 필수적
