## Django

- Web application
  
  - 인터넷을 통해 사용자에게 제공되는 소프트웨어 프로그램을 구축하는 과정
  
  - 다양한 디바이스에서 웹 브라우저를 통해 접근과 사용 가능

- 클라이언트와 서버
  
  - 웹의 동작 방식
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-10-28-image.png" title="" alt="" data-align="center">
  
  - 클라이언트
    
    - 서비스를 요청하는 주체(사용자의 웹 브라우저, 모바일 웹)
  
  - 서버
    
    - 클라이언트의 요청에 응답하는 주체(웹 서버, 데이터베이스 서버)
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-11-19-image.png" title="" alt="" data-align="center">
    
    - 1. 웹 브라우저(**클라이언트**)에서 'google.com' 을 입력 후 엔터
      
      2. 웹 브라우저는 인터넷에 연결된 전세계 어딘 가에 있는 구글 컴퓨터(**서버**)에게 '**메인홈페이지.html**' 파일을 달라고 **요청**
      
      3. 요청을 받은 구글 컴퓨터는 데이터베이스에서 '**메인 홈페이지.html**' 파일을 찾아 **응답**
      
      4. 웹 브라우저는 전달받은 '**메인 홈페이지.html**' 파일을 사람이 볼 수 있도록 해석해주고 사용자는 구글의 메인 페이지를 보게 됨

## Frontend & Backend

- frontend
  
  - 사용자 인터페이스(UI)를 구성하고, 사용자가 애플리케이션과 상호작용할 수 있도록 함
  
  - html, css, javascript, 프론트엔드 프레임워크 등

- backend
  
  - 서버 측에서 동작하며, 클라이언트의 요청에 대한 처리와 데이터베이스와의 상호작용 등 담당
  
  - 서버 언어(python, java 등) 및 백엔드 프레임워크, 데이터베이스, api, 보안 등
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-14-59-image.png" title="" alt="" data-align="center">

## Framework

- web framework
  
  - 웹 서비스 개발에 필요한 것
    
    - 로그인/로그이웃, 회원관리, 데이터베이스, 보안 등
    
    - 모든 기능을 직접 개발하기에는 현실적 어려움
    
    - 현대 웹 개발의 핵심
      
      - 잘 만들어진 도구를 효과적으로 활용하는 능력
  
  - 웹 애플리케이션을 빠르게 개발할 수 있도록 도와주는 도구
  
  - 개발에 필요한 기본 구조, **규칙**, 라이브러리 제공

## Django framework

- django
  
  - python 기반의 대표적인 웹 프레임워크
  
  - 사용 이유
    
    - 다양성
      
      - python 기반으로 웹, 모바일 앱 백엔드, api 서버 및 빅데이터 관리 등 광범위한 서비스 개발에 적합
    
    - 확장성
      
      - 대량의 데이터에 대해 빠르고 유연하게 확장할 수 있는 기능 제공
    
    - 보안
      
      - 취약점으로부터 보호하는 보안 기능이 기본적으로 내장
    
    - 커뮤니티 지원
      
      - 개발자를 위한 지원, 문서 및 업데이트 제공하는 활성화된 커뮤니티
  
  - 검증된 웹 프레임워크
    
    - 대규모 트래픽 서비스에서도 안정적인 서비스 제공
  
  - 가장 인기있는 backend framework
  
  - django를 사용해서 서버를 구현할 것

## 가상환경(virtual environment)

- 개념
  
  - 하나의 컴퓨터 안에서 또 다른 **'독립된'** 파이썬 환경

- 가상환경이 필요한 시나리오 1
  
  - 1. 한 개발자가 2개의 프로젝트 진행
    
    2. 프로젝트 A는 **requests** 패키지 버전 1 사용
    
    3. 프로젝트 B는 **requests** 패키지 버전 2 사용
    
    4. 파이썬 환경에서 패키지는 1개의 버전만 존재 가능
    
    5. A와 B 프로젝트의 다른 패키지 버전 사용을 위한 **독립적인 개발 환경**이 필요

- 가상환경이 필요한 시나리오 2
  
  - 1. 한 개발자가 2개의 프로젝트 진행
    
    2. 프로젝트 A는 **water** 패키지 사용
    
    3. 프로젝트 B는 **fire** 패키지 사용
    
    4. 파이썬 환경에서 패키지는 **water** 패키지와 **fire** 패키지 함께 사용하면 충돌이 발생하기 때문에 설치할 수 없음
    
    5. A와 B 프로젝트의 패키지 충돌을 피하기 위한 **독립적인 개발 환경**이 필요
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-23-27-image.png" title="" alt="" data-align="center">

- 비유
  
  - 같은 집(컴퓨터) 안에 방(가상환경)을 따로 만들어 두고 필요한 물건(라이브러리, 패키지 등)을 그 방에만 들여놓는 것과 비슷
  
  - 방이 다르면 들여놓은 물건이 달라도 서로 간섭하지 않음

## 가상환경 생성 및 활성화

- 가상 환경 생성
  
  ```python
  $ python -m venv venv
  ```
  
  - 뒤 **venv**는 이름이므로 변경 가능(하지만 하지 않음)
  
  - 현재 디렉토리에 **venv** 라는 폴더 생성
  
  - **venv** 폴더 안에는 파이썬 실행 파일, 라이브러리 등을 담을 공간 마련
  
  - **venv** 라는 이름의 가상환경을 생성한 것이며, 임의의 이름으로 생성이 가능하나 관례적으로 **venv** 이름을 사용

- 가상 환경 활성화
  
  ```python
  $ source venv/Scripts/activate
  ```
  
  - 활성화 후, 프롬프트 앞에 **(venv)** 와 같이 표시된다면 성공한 것
  
  - mac / linux에서는 명령어가 다르니 주의
    
    ```python
    $ source venv/bin/activate
    ```

- 가상 환경 종료
  
  ```python
  $ deactivate
  ```
  
  - 활성화한 상태에서 **deactivate** 명령을 입력하면, 다시 기본 global 파이썬 환경으 로 돌아옴

## 의존성 패키지

- 의존성(dependencies)
  
  - 하나의 소프트웨어가 동작하기 위해 필요로 하는 다른  소프트웨어나 라이브러리

- 의존성 패키지
  
  - 프로젝트가 의존하는 "개발 라이브러리들"을 가리키는 말
    
    - 프로젝트가 실행되기 위해 꼭 필요한 패키지 하나하나

- 패키지 목록 확인
  
  ```python
  $ pip list
  ```
  
  - 현재 가상환경에 설치된 라이브러리 목록 확인
  
  - 갓 생성된 가상환경은 별도의 패키지가 없어, 주로 pip, setuptools 정도만 표시됨
  
  <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-29-17-image.png" alt="" data-align="center">

- 의존성 기록
  
  ```python
  $ pip freeze > requirements.txt
  ```
  
  - **pip freeze** 명령어는 가상환경에 설치된 모든 패키지를 버전과 함께 출력
  
  - 이를 **requirement.txt** 파일에 저장하면, 나중에 동일한 환경을 재현할 때 유용
    
    - 다른 파일명으로도 가능하나 관례적으로 **requirements**를 사용
  
  - 협업 시에도 팀원들이 똑같은 버전의 라이브러리를 설치하도록 공유 가능

- 의존성 리스트 예시
  
  - **requests** 패키지 설치 후 현재 가상환경의 패키지 목록 변화
  
  - 1개만 설치되는 것이 아님
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-31-22-image.png" title="" alt="" data-align="center">

- 의존성 리스트 공유 시나리오
  
  - 만약 2명(A와 B)의 개발자가 하나의 프로젝트를 함께 개발함
  
  - 팀원 A가 먼저 가상 환경을 생성 후 프로젝트를 설정하고 관련된 패키지를 설치하고 개발하다가 협업을 위해 github에 프로젝트를 push
  
  - 팀원 B는 해당 프로젝트를 clone 받고 실행해보려 하지만 실패
  
  - 팀원 A 가 이 프로젝트를 위해 어떤 패키지를 설치했고, 어떤 버전을 설치했는지 A의 가상 환경 상황을 알 수 없음
  
  - 가상 환경에 대한 정보 즉 **패키지 목록**이 공유되어야 함

- 의존성 패키지 관리가 필요한 이유
  
  - 1. 패키지마다 버전이 다르고, 버전이 다른 경우 함수명이나 동작이 달라질 수 있음
    
    2. 프로젝트가 커질수록 사용하는 패키지의 개수도 늘어나므로, 어떤 버전을 쓰고 있는지 기록 및 공유가 필수적
    
    3. 다른 PC나 팀원들이 같은 환경을 구성할 때 **의존성 리스트**가 반드시 필요

## 의존성 패키지 기반 설치

- requirements.txt를 활용하여 다른 환경(혹은 팀원의 PC)에서도 동일한 패키지 버전을 설치하는 방법

- 1. 가상 환경 준비
     
     1. 먼저, 새로운 가상 환경 생성 및 활성화
  
  2. **requirements.txt로부터 패키지 설치**
     
     ```python
     $ pip install -r requirements.txt
     ```
     
     1- requirements.txt 에 기록된 패키지와 버전을 읽어와, 같은 환경으로 설치

## 가상환경 주의사항

- 가상환경 주의사항 및 권장사항
  
  - 1. 가상 환경에 "들어가고 나오는" 것이 아니라 사용할 python 환경을 "on/off"로 전환하는 개념
       
       1. 가상 환경 활성화는 현재 터미널 환경에만 영향을 끼침
       
       2. 새 터미널 창을 열면 다시 활성화해야함
    
    2. 프로젝트마다 별도의 가상환경 사용
    
    3. 일반적으로 가상환경 폴더 **venv**는 관련된 프로젝트와 동일한 경로에 위치시킴
    
    4. 폴더 **venv**는 **.gitignore** 파일에 작성되어 원격 저장소에 공유되지 않음
       
       1. 저장소 크기를 줄여 효율적인 협업과 배포를 가능하게 하기 위함(대신, **requirements.txt**를 공유)

- 가상환경이 필요한 이유
  
  - 1. 프로젝트마다 다른 버전의 라이브러리 사용
       
       1. 한 프로젝트에서는 django 3.2를, 다른 프로젝트에서는 django 4.1을 사용해야 할 수 도 있는데, 이 때 가상환경을 사용하면 서로 다른 버전을 동시에 설치해도 충돌 없이 각각의 프로젝트 유지 가능
    
    2. 의존성 충돌 방지
       
       1. 프로젝트별로 라이브러리를 독립적으로 관리하게 해주어 여러 프로젝트가 동시에 같은 라이브러리를 쓰더라도 버전 충돌 문제를 예방
    
    3. 팀원 간 협업
       
       1. 누구든지 동일한 방식으로 가상환경을 만들어서, 똑같은 버전의 라이브러리를 설치하면 에러 가능성 줄일 수 있음

- 요약
  
  - 1. 가상환경을 만든다(**python -m venv venv**)
    
    2. 가상환경을 활성화(**source venv/Scripts/activate**)
    
    3. 필요한 의존성 패키지 설치(**pip install**)
    
    4. 현재 환경의 모든 패키지 목록을 **pip freeze > requirements.txt**로 저장하여의존성 관리
    
    5. 다른 컴퓨터나 팀원도 같은 환경이 필요하다면, **pip install -r requirements.txt**로 동일한 버전의 라이브러리 설치
    
    6. 작업이 끝나면 **deactivate**로 가상환경 비활성화 

## Django 프로젝트

- 프로젝트 생성 및 서버 실행
  
  - 1. 프로젝트 생성
       
       ```python
       $ django-admin startproject firstpjt .
       ```
       
       1. **firstpjt**라는 이름의 django 프로젝트 생성
    
    2. 서버 실행
       
       ```python
       $ python manage.py runserver
       ```
       
       1- **manage.py**와 동일한 위치에서 명령어 진행
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-09-48-32-image.png" title="" alt="" data-align="center">

## Django Design Pattern

- design pattern
  
  - 디자인 패턴
    
    - 소프트웨어 설계에서 발생하는 문제를 해결하기 위한 일반적인 해결책
    
    - 공통적인 문제를 해결하는 데 쓰이는 형식화 된 관행
      
      - "애플리케이션의 구조는 이렇게 구성하자" 라는 관행
  
  - MVC 디자인 패턴(Model, View, Controller)
    
    - 애플리케이션을 구조화하는 대표적인 패턴
    
    - "데이터" & "사용자 인터페이스" & "비지니스 로직" 분리
      
      - **시각적 요소와 뒤에서 실행되는 로직을 서로 영향 없이, 독립적이고 쉽게 유지 보수할 수 있는 애플리케이션을 만들기 위해**
  
  - MVC 디자인 패턴(Model, Template, View)
    
    - django 에서 애플리케이션을 구조화하는 패턴
    
    - 기존 mvc 패턴과 동일하나 단순히 명칭을 다르게 정의한 것 
    
    - view -> template, controller -> view(단순한 명칭 변경)

## 프로젝트와 앱

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-05-12-image.png" title="" alt="" data-align="center">

- django project
  
  - 애플리케이션의 집합(DB 설정, URL 연결, 전체 앱 설정 등 처리)

- django application
  
  - 독립적으로 작동하는 기능 단위 모듈
  
  - 각자 특정한 기능을 담당하며 다른 앱들과 함께 하나의 프로젝트 구성

- 온라인 커뮤니티 카페를 만든다면?
  
  - 프로젝트 : 카페(전체 설정 담당)
  
  - 앱 : 게시글, 댓글, 회원관리 등(DB, 인증, 화면)

- 앱을 사용하기 위한 순서
  
  - 앱 생성
    
    - 앱의 이름은 '복수형'으로 지정하는 것 권장
    
    ```python
    $ python manage.py startapp articles
    ```
  
  - 앱 등록
    
    - 반드시 **앱을 생성(1)한 후에 등록(2)** 해야 함
    
    - 등록 후 생성은 불가능
    
    ```python
    # settings.py
    ```

    INSTALLED_AAPS = [
        'articles',
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes', 
        'django.contrib.sessions', 
        'django.contrib.messages', 
        'django.contrib.staticfiles',
    ]
    ```

## 프로젝트 및 앱 구조

- 프로젝트 구조
  
  - **settings.py**
    
    - 프로젝트의 모든 설정 관리
  
  - **urls.py**
    
    - 요청 들어오는 URL에 따라 이에 해당하는 적절한 views 연결
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-11-57-image.png" title="" alt="" data-align="center">
  
  - **____init__.py__**
    
    - 해당 폴더를 패키지로 인식하도록 설정하는 파일
  
  - **asgi.py**
    
    - 비동기식 웹 서버와의 연결 관련 설정
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-13-20-image.png" title="" alt="" data-align="center">
  
  - **wsgi.py**
    
    - 웹 서버와의 연결 관련 설정
  
  - **manage.py**
    
    - django 프로젝트와 다양한 방법으로 상호작용 하는 커맨드라인 유틸리티
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-14-54-image.png" title="" alt="" data-align="center">

- 앱 구조
  
  - **admin.py**
    
    - 관리자용 페이지 설정
  
  - **models.py**
    
    - DB와 관련된 model 정의
    
    - mtv 패턴의 m
  
  - **views.py**(중요 !)
    
    - http 요청 처리하고 해당 요청에 대한 응답 반환(url, model, template과 연계)
    
    - mtv 패턴의 v
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-17-32-image.png" title="" alt="" data-align="center">
  
  - **apps.py**
    
    - 앱의 정보가 작성된 곳
  
  - **tests.py**
    
    - 프로젝트 테스트 코드를 작성하는 곳
    
    <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-18-06-image.png" alt="" data-align="center">

## 요청과 응답

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-18-35-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-18-49-image.png" title="" alt="" data-align="center">

- **URLs**
  
  ```python
  # urls.py
  
  from django.contrib import admin
  from django.urls import path
  from articles import views
  
  urlpatterns = [
       path('admin/', admin.site.urls),
       path('index/', views.index),
   ]
  ```
  
  - http://127.0.0.1:8000/index/ 로 요청이 왔을 때 request 객체를 views 모듈의 index view 함수에게 전달하며 호출
    
    - from articles import view -> **articles 패키지에서 views 모듈을 가져오는 것**
    
    - **url 경로는 반드시 '/'(slash)로 끝나야 함**
    
    - **View**
    
    

```python
# view.py

from Django.shortcuts import render

def index(request): 
    return render(request, 'articles/index,html')
```

- view 함수가 정의되는 곳

- 특정 경로에 있는 template과 request 객체를 결합해 응답 객체 반환
  
  - **모든 view 함수는 첫 번째 인자로 요청 객체를 필수적으로 받음**
  
  - **매개 변수 이름이 request가 아니어도 되지만 그렇게 작성하지 않음**

- **Template**
  
  - 1. articles 앱 폴더 안에 templates 폴더 생성
       
       1. **폴더명은 반드시 templates 여야 하며 개발자가 직접 생성해야 함**
    
    2. templates 폴더 안에 articles 폴더 생성
    
    3. articles 폴더 안에 템플릿 파일 생성
    
    ```css
    <!-- aritlces/index.html -->
    
    <!DOCTYPE html>
    <html lang="en">
    <head>
     ...
     <title>Document</title>
    </head>
    <body>
     <h1>Hello, Django</h1>
    </body>
    </html>
    ```
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-26-33-image.png" title="" alt="" data-align="center">

- **Django 에서 template을 인식하는 경로 규칙**
  
  - **app폴더 / templates /** articles / index.html
  
  - **app폴더 / templates /** example.html
    
    - -> Django는 이 지점까지 기본 경로로 인식하기 때문에 view 함수에서  template 경로 작성 시 이 지점 이후의 경로를 작성해야 함
    
    ```python
    # views.py
    
    def index(request):
        return render(request, 'articles/index.html')
    ```
  
  **<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-30-13-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-10-30-53-image.png" title="" alt="" data-align="center">

- 데이터 흐름에 따른 코드 작성하기
  
  - URLs -> View -> Template
  
  - URLs
    
    - path('articles/', **views.index**), 
  
  - View
    
    ```python
    def index(request):
        return render(request, 'articles/index.html')
    ```
  
  - Template
    
    - articles/templates/**articles/index.html**

# 참고

## 가상환경 생성 루틴

- **Django 프로젝트 생성 전 루틴**
  
  - 1. 가상환경 생성
    
    2. 가상환경 활성화
    
    3. **Django** 설치
    
    4. 패키지 목록 파일 생성(패키지 설치 시마다 진행)
  
  ```python
  # 1. 가상환경(venv) 생성
  $ python -m venv venv
  
  # 2. 가상환경 활성화
  $ source venv/Scripts/activate
  
  # 3. Django 설치
  $ pip install django
  
  # 4. 패키지 목록 파일 생성
  $ pip freeze > requirements.txt
  ```

- **Django 프로젝트 생성 루틴 정리  + git**
  
  - 5. **.gitignore 파일 생성(첫 add 전)**
    
    6. **git 저장소 생성(git init)**
    
    7. Django 프로젝트 생성



## Django 관련

- **LTS(Long Term Support)**
  
  - 프레임 워크나 라이브러리 등의 소프트웨어에서 장기간 지원되는 안정적인 버전 의미할 때 사용
  
  - 기업이나 대규모 프로젝트에서는 소프트웨어 업그레이드에 많은 비용과 시간이 필요하기 때문에 안정적이고 장기간 지원되는 버전 필요



## Django는 Full Stack framework 인가요?

- 네

- 하지만 Django가 제공하는 Frontend 기능은 다른 전문적인 Frontend Framework 들에 비해서는 매우 미흡

- 엄밀히 말하면 Full Stack 영역에서 Backend에 속한다고 볼 수 있음

- Full Stack 혹은 Backend Framework 라 부름



## Render 함수

- 주어진 템플릿을 주어진 컨텍스트 데이터와 결합하고 렌더링된 텍스트와 함께 **HttpResonse** 응답 객체 반환하는 함수
  
  - 1. **request**
       
       1. 응답 생성하는 데 요청되는 요청 객체
    
    2. **template_name**
       
       1. 템플릿 이름의 경로
    
    3. **context**
       
       1. 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)
  
  ```python
  render(request, template_name, context)
  ```



## MTV 디자인 패턴 정리

- Model
  
  - 데이터와 관련된 로직 관리
  
  - 응용프로그램의 데이터 구조 정의하고 데이터베이스의 기록 관리

- Template
  
  - 레이아웃과 화면 처리
  
  - 화면 상의 사용자 인터페이스 구조와 레이아웃 정의

- View
  
  - Model & Template과 관련한 로직을 처리해서 응답 반환
  
  - 클라이언트의 요청에 대해 처리 분기하는 역할
  
  - 예시
    
    - 데이터가 필요하다면 model에 접근해서 데이터를 가져오고, 가져온 데이터를 template로 보내 화면을 구성하고, 구성된 화면을 응답으로 만들어 클라이언트에게 반환
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-24-11-02-07-image.png" title="" alt="" data-align="center">



## Trailing Comma

- "후행 쉼표"

- 리스트, 딕셔너리, 튜플 등의 자료 구조에서 마지막 요소 뒤에 심표 추가

- 문법적으로 아무런 영향 주지 않음

- 일반적으로 선택 사항(단일 요소 튜플을 만들 때는 예외)

- 사용 이유
  
  - 새로운 요소 추가하거나 순서 변경할 때 편리
  
  - 값의 목록, 인자 또는 import 항목들이  시간이 지남에 따라 확장될 것으로 예상되는 경우에 주로 사용
  
  - 여러 줄에 걸쳐 작성된 데이터 구조에서 유용하며, 코드의 가독성과 유지보수성 향상
  
  - 일반적인 패턴은 각 값(등)을 별도의 줄에 배치하고, 항상 후행 쉼표를 추가한 뒤, 닫는 괄호/대괄호/중괄호를 다음 줄에 배치
  
  - 닫는 구분 기호와 같은 줄에 후행 쉼표 두는 것은 권장 x



## 프레임워크의 규칙 및 설계 철학

- **지금까지 등장한 Django의 규칙**
  
  - 1. **urls.py**에서 각 url 문자열 경로는 반드시 **'/'** 로 끝남
    
    2. **views.py**에서 모든 view 함수는 **첫 번째 인자로 요청 객체** 받음
       
       1. 매개변수 이름은 반드시 **request**로 지정
    
    3. **Django** 는 **특정 경로**에 있는 template 파일만 읽어올 수 있음
       
       1. 특정 경로 : **app폴더/templates/**

- **프레임워크의 규칙**
  
  - 프레임워크를 사용할 때는 일정한 규칙을 따라야 하며 이는 저마다의 설계 철학이나 목표 반영
  
  - 프레임워크는 개발자에게 **도움을 주는 도구와 환경을 제공하기 위해 규칙을 정해 놓은 것**
