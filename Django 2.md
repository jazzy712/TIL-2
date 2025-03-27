# Django 2

## Template System

### Django Template system

- 개념
  
  - 데이터 **표현**을 제어하면서, **표현**과 관련된 부분 담당
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-05-42-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-05-56-image.png" title="" alt="" data-align="center">

### Django Template Language(DTL)

- 개념
  
  - Template에서 조건, 반복, 변수 등의 프로그래밍적 기능 제공 시스템

- **DTL Syntax**
  
  - **variable**
    
    - **render** 함수의 세 번째 인자로 딕셔너리 데이터 사용
    
    - 딕셔너리 key에 해당하는 문자열이 template에서 사용 가능한 변수명이 됨
    
    - dot('.')을 사용하여 변수 속성에 접근 가능
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-09-25-image.png" title="" alt="" data-align="center">
  
  - **filters**
    
    - 표시할 변수를 수정할 때 사용(변수 + '|' + 필터)
    
    - chained(연결)이 가능하며 일부 필터는 인자를 받기도 함
    
    - 약 60개의 built-in template filters를 제공
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-11-51-image.png" title="" alt="" data-align="center">
  
  - **tags**
    
    - 반복 또는 논리를 수행하여 제어 흐름 만듦
    
    - 일부 태그는 시작과 종료 태그 필요
    
    - 약 24개의 built-in template tags 제공
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-12-35-image.png" title="" alt="" data-align="center">
  
  - **comments**
    
    - DTL에서의 주석
    
    ```python
     <h1>Hello, {# name #}</h1>
    ```
    
    ```python
    {% comment %} 
     ... 
    {% endcomment %}
    ```

- DTL 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-14-02-image.png" title="" alt="" data-align="center">
  
  ```python
  # urls.py 
  
  urlpatterns = [
      path('admin/', admin.site.urls),
      path('articles/', views.index),
      path('dinner/', views.dinner), 
  ]
  ```
  
  ```python
  # views.py 
  
  import random
  
  def dinner(request):
      foods = ['국밥', '국수', '카레', '탕수육',]
      picked = random.choice(foods)
      context = {
          'foods' : foods,
          'picked' : picked
      }
      return render(request, 'articles/dinner.html', context)
  ```

```
```python
<!-- articles/dinner.html ->

<p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
<h2>메뉴판</h2>
<ul>
  {% for food in foods %}
    <li>{{ food }}</li>
  {% endfor %}
</ul>

{% if foods|length == 0 %}
  <p>메뉴가 소진 되었습니다.</p>
{% else %}
  <p>아직 메뉴가 남았습니다.</p>
{% endif %}
```

## 템플릿 상속

### 기존 템플릿 구조의 한계

- 만약 모든 템플릿에 bootstrap을 적용하려면?
  
  - 모든 템플릿에 bootstrap CDN을 작성해야 할까?

- **템플릿 상속**(template inheritance)
  
  - **페이지의 공통 요소를 포함**하고, **하위 템플릿이 재정의 할 수 있는 공간**을 정의하는 기본 'skeleton' 템플릿을 작성하여 상속 구조 구축

- 상속 구조 만들기
  
  ```python
  <!-- articles/base.html -->
  
  <!DOCTYPE html>
  <html lang="en">
  <head>
    ...
    {% comment %} bootstrap CDN 생략 {% endcomment %}
  </head>
  <body>
    {% block content %}
    {% endblock content %}
    {% comment %} bootstrap CDN 생략 {% endcomment %}
  </body>
  </html>
  ```
  
  - 기존 하위 템플릿의 변화
  
  ```python
  <!-- articles/dinner.html -->
  
  {% extends "articles/base.html" %}
  
  {% block content %}
    <p>{{ picked }} 메뉴는 {{ picked|length }}글자 입니다.</p>
    <h2>메뉴판</h2>
    <ul>
      {% for food in foods %}
      <li>{{ food }}</li>
      {% endfor %}
    </ul>
  
    {% if foods|length == 0 %}
      <p>메뉴가 소진 되었습니다.</p>
    {% else %}
      <p>아직 메뉴가 남았습니다.</p>
    {% endif %}
  {% endblock content %}
  ```

## 상속 관련 DTL 태그

- **'extends' tag**
  
  ```python
  {% extends 'path %}
  ```
  
  - 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
    
    - **반드시 자식 템플릿 최상단에 작성되어야 함(2개 이상 사용 불가)**

- **'block' tag**
  
  ```python
  {% block name %}{% endblock name %}
  ```
  
  - 하위 템플릿에서 재정의 할 수 있는 블록 정의(상위 템플릿에 작성하며 하위 템플릿이 작성할 수 있는 공간 지정)

- **하위 템플릿이 재정의 할 수 있는 block 영역**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-39-50-image.png" title="" alt="" data-align="center">

## 요청과 응답

### HTML form

- **데이터를 보내고 가져오기**(sending and retrieving form data)
  
  - HTML **'form'** element를 통해 사용자와 애플리케이션 간의 상호작용 이해하기

- **HTML 'form'은 HTTP 요청을 서버에 보내는 가장 편리한 방법**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-43-06-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-09-45-28-image.png" title="" alt="" data-align="center">
  
  - **form과 input이 제일 중요**

- **'form' element**
  
  - 사용자로부터 할당된 데이터를 서버로 전송
    
    - 웹에서 사용자 정보를 입력하는 여러 방식(**text, password, checkbox 등**) 제공

- **fake Naver 실습**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-06-09-image.png" title="" alt="" data-align="center">
  
  - **input**에 **hello**를 입력하고 제출 버튼을 누른 후 브라우저의 URL 변화 확인
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-07-14-image.png" title="" alt="" data-align="center">
  
  - 실제 Naver에서 검색 후 URL 확인
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-08-52-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-09-15-image.png" title="" alt="" data-align="center">

### HTML form 핵심 속성

- **'action' & 'method'**
  
  - **form의 핵심 속성 2가지**
    
    - "데이터를 어디(**action**)로 어떤 방식(**method**)으로 요청할지"
  
  - **action**
    
    - 입력 데이터가 전송될 URL 지정(목적지)
    
    - 만약 이 속성을 지정하지 않으면 데이터는 현재 form이 있는 페이지의 URL로 보내짐
  
  - **method**
    
    - 데이터를 어떤 방식으로 보낼 것인지 정의
    
    - 데이터의 HTTP request methods(get, post) 지정

- **'input' element**
  
  - 사용자의 데이터를 입력 받을 수 있는 요소
  
  - **type** 속성 값에 따라 다양한 유형의 입력 데이터 받음
    
    - 핵심 속성 - **'name'**

- **'name' attribute**
  
  - input의 핵심 속성
  
  - 사용자가 입력한 데이터에 붙이는 이름
  
  - 데이터를 제출했을 때 서버는 name 속성에 설정된 값을 통해서만 사용자가 입력한 데이터에 접근 가능

- **Query String Parameters**
  
  - 사용자의 입력 데이터를 URL 주소에 파라미터를 통해 서버로 보내는 방법
  
  - 문자열은 앰퍼샌드(**'&'**)로 연결된 **key = value** 쌍으로 구성되며, 기본 URL  과는 물음표(**'?'**)로 구분됨
  
  - 예시
    
    - http://host:port/path?**key=value**&**key=value**

### HTML form 활용

- **사용자가 입력 데이터를 받아 그대로 출력하는 서버 만들기**
  
  - view 함수는 몇 개가 필요할까?
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-15-10-image.png" title="" alt="" data-align="center">

- **throw 로직 작성**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-17-50-image.png" title="" alt="" data-align="center">

- **catch 로직 작성**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-20-43-image.png" title="" alt="" data-align="center">

- **HTTP request 객체**
  
  - **form**으로 전송한 데이터 뿐만 아니라 Django로 들어오는 모든 요청 관련 데이터가 담겨 있음(view 함수의 첫 번째 인자로 전달됨)

- **request 객체 살펴보기**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-27-22-image.png" title="" alt="" data-align="center">

- **request 객체에서 form 데이터 추출**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-27-49-image.png" title="" alt="" data-align="center">

- **catch 로직 마무리**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-28-37-image.png" title="" alt="" data-align="center">

- **throw - catch 간 요청과 응답 정리**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-29-02-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-29-24-image.png" title="" alt="" data-align="center">

## Django URLs

- **요청과 응답에서 Django URLs의 역할**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-32-20-image.png" title="" alt="" data-align="center">

- **URL dispatcher**(운항 관리자, 분배기)
  
  - URL 패턴을 정의하고 해당 패턴이 일치하는 요청을 처리할 view 함수 연결(매핑)

### Variable Routing

- **현재 URL 관리의 문제점**
  
  - 템플릿의 많은 부분이 중복되고, URL의 일부만 변경되는 상황이라면 계속해서 비슷한 URL과 템플릿을 작성해 나가야 할까?
  
  ```python
  urlpatterns = [
      path('articles1/', ...),
      path('articles2/', ...),
      path('articles3/', ...),
      path('articles4/', ...),
      path('articles5/', ...),
      ...
  ]
  ```

- **variable routing**
  
  - URL 일부에 변수를 포함시키는 것(변수는 view 함수의 인자로 전달할 수 있음)

- **variable routing 작성법**
  
  - **< path_converter:variable_name >**
  
  ```python
  path('aritlcles/<int:num>/', views.detail)
  path('hello/<str:name>/', views.greeting)
  ```

- **path converters**
  
  - URL 변수의 타입 지정(**str, int** 등 5가지 타입 지원)

- **variable routing  실습**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-42-32-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-43-01-image.png" title="" alt="" data-align="center">

### App URL 정의

- **App URL mapping**
  
  - 각 앱에 URL을 정의하는 것
    
    - 프로젝트와 각 앱이 URL을 나누어 관리를 편하게 하기 위함

- **2번째 앱 pages 생성 후 발생할 수 있는 문제**
  
  - view 함수 이름이 같거나 같은 패턴의 URL 주소를 사용하게 되는 경우
  
  - 아래 코드와 같이 해결해 볼 수 있으나 더 좋은 방법이 필요
    
    - **URL을 각자 app에서 관리하자**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-44-38-image.png" title="" alt="" data-align="center">

- **기존 url 구조**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-44-55-image.png" title="" alt="" data-align="center">

- **변경된 url 구조**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-45-16-image.png" title="" alt="" data-align="center">

- **url 구조 변화**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-47-33-image.png" title="" alt="" data-align="center">

- **include()**
  
  - 프로젝트 내부 앱들의 URL을 참조할 수 있도록 매핑하는 함수
    
    - URL의 일치하는 부분까지 잘라내고, 남은 문자열 부분은 후속 처리를 위해 include된 URL로 전달

- **include 적용**
  
  - 변경된 프로젝트의 urls.py
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-52-24-image.png" title="" alt="" data-align="center">

## URL 이름 지정

### Naming URL patterns

- **url 구조 변경에 따른 문제점**
  
  - 기존 '**articles/**' 주소가 '**articles/index/**' 로 변경됨에 따라 해당 url을 사용하는 모든 위치를 찾아가 변경해야 함
  
  - **URL에 이름을 지어주면 이름만 기억하면 되지 않을까?**
  
  <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-53-38-image.png" alt="" data-align="center">

- **Naming URL patterns**
  
  - URL에 이름을 지정하는 것
  
  - **path** 함수의 **name** 인자를 정의해서 사용
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-54-19-image.png" title="" alt="" data-align="center">

- **URL 표기 변화**
  
  - **url**을 작성하는 모든 곳에서 변경
  
  - **a** 태그의 **href** 속성 값 뿐만 아니라 **form**의 **action** 속성 등도 포함
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-55-25-image.png" title="" alt="" data-align="center">

### DTL URL tag

- **'url' tag**
  
  ```rpy
  {% url 'url name' arg1 arg2 %}
  ```
  
  - 주어진 url 패턴의 이름과 일치하는 절대 경로 주소 반환

- **url tag 적용 후 브라우저 출력 확인**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-57-16-image.png" title="" alt="" data-align="center">

## URL 이름 공간

### app_name 속성

- **url 이름 지정 후 남은 문제**
  
  - **articles** 앱의 **url** 이름과 **pages** 앱의 **url** 이름이 같은 상황
  
  - 단순히 이름만으로는 완벽하게 분리 불가능
  
  - **이름에 성(key)을 붙이자**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-58-25-image.png" title="" alt="" data-align="center">

- **'app_name' 속성 지정**
  
  - 'app_name' 변수 값 설정
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-58-51-image.png" title="" alt="" data-align="center">

- **url tag의 최종 변화**
  
  - 마지막으로 url 태그가 사용하는 모든 곳의 표기 변경
  
  ```python
  {% url 'app_name:path_name' %}
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-10-59-36-image.png" title="" alt="" data-align="center">

## 참고

### 추가 템플릿 경로

- **추가 템플릿 경로 지정**
  
  - 템플릿 기본 경로 외 커스텀 경로 추가
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-11-00-57-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-11-01-11-image.png" title="" alt="" data-align="center">

- **BASE_DIR**
  
  - settings에서 경로지정을 편하게 하기 위해 최상단 지점을 지정해 둔 변수
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-25-11-01-44-image.png" title="" alt="" data-align="center">

### DTL 주의사항

- python 처럼 일부 프로그래밍 구조(**if, for** 등)를 사용할 수 있지만 명칭을 그렇게 설계했을 뿐이지 **python 코드로 실행되는 것이 아니며 python과는 관련 없음**

- 프로그래밍적 로직이 아니라 표현을 위한 것임을 명심

- 프로그래밍적 로직은 되도록 view 함수에서 작성 및 처리

### Trailing Slashes

- Django는 url 끝에 **'/'** 가 없다면 자동으로 붙임

- "기술적인 측면에서, **foo.com/bar**와 **foo.com/bar/** 는 서로 다른 url"
  
  - 검색 엔진 로봇이나 웹 트래픽 분석 도구에서는 이 두 주소를 서로 다른 페이지로 보기 때문

- 그래서 django는 검색 엔진이 혼동하지 않게 하기 위해 무조건 붙이는 것을 선택

- 그러나 모든 프레임워크가 이렇게 동작하는 것은 아님
