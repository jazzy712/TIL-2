## Git

- 분산 **버전 관리 시스템** 
  
  - 버전 관리  : 변화 기록 및 추적
  
  - 코드의 '변경 이력'을 기록하고 '협업'을 원활하게 하는 도구
    
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-20-45-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-25-41-image.png)

- 중앙  vs 분산

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-27-01-image.png)

    

- 중앙 집중식의 문제 : 중앙 서버가 무너지면 나머지 서버도 모두 무너짐

-----> 분산식 등장

- 분산 구조의 장점
  
  - 중앙 서버에 의존x, 동시에 다양한 작업 수행 가능
  
  - 개발자들 간 작업 충돌 축소, 개발 생산성 향상
  
  - 중앙 서버의 장애나 손실 대비 백업과 복구가 용이
  
  - 인터넷에 연결되어 있지 않은 환경에서도 작업 지속 가능
  
  - 변경 이력과 코드를 로컬 저장소에 기록, 추후에 중앙 서버와 동기화

## Git의 역할

- 코드의 버전(히스토리) 관리

- 개발되어 온 과정 파악

- 이전 버전과 변경 사항 비교

## Git의 영역

- working directory : 실제 작업 중인 파일들이 위치하는 영역

- staging area : working directory 에서 변경된 파일 중, 다음 버전에 포함시킬 파일들을 선택적으로 추가하거나 제외할 수 있는 **중간** 준비 영역, skip 불가능

- repository : **버전** 이력과 파일들이 영구적으로 저장되는 영역
  
                       모든 버전과 변경 이력이 기록됨     

- commit : 변경된 파일들을 저장하는 행위, 사진을 찍듯이 기록한다하여 'snapshot'이라도 함.

## Git의 동작

- git init(시작) : 로컬 저장소 설정(초기화) -> git의 버전 관리를 시작할 디렉토리에서 진행 

- git add : 변경사항이 있는 파일을 staging area에 추가
  
  - git commit : staging area에 있는 파일들을 저장소에 기록
    
                         -> 해당 시점의 버전을  생성하고 변경 이력을 남기는 것

- master : git의 영역
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-46-11-image.png)
  
  - git 내부에 git 존재 불가능 -> git init을 상위 디렉토리에 적용 시 하위 디렉토리에 
    
    git init 불가

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-14-37-05-image.png)

- git status를 중간중간 체크

<img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-01-16-11-52-48-image.png" alt="" width="835">

--> 빨간색 글씨 : working directory에 존재

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-53-29-image.png)

--> 초록색 글씨 : staging area에 존재

- git commit(버전) -> 책임 필요 -> 누가??(버전 만든 사람의 서명 필요) - 유저네임/이메일

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-11-56-52-image.png)

- global <-> local
  
      

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-01-16-11-59-17-image.png" title="" alt="" width="703">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-01-16-11-59-55-image.png" title="" alt="" width="692">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-01-16-12-01-27-image.png" title="" alt="" width="726">

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-12-12-29-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-12-14-29-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-12-16-07-image.png)

- git은 로컬 저장소(git init) 내 모든 파일의 '**변경사항**'을 감시하고 있다.

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-12-19-14-image.png)

-> **git add .** 중요!!

- 명령어 입력 때 화살표 이용하면 이전에 사용한 명령어들 사용 가능

## Local

- 현재 사용자가 직접 접속하고 있는 기기/시스템

- 개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조작하는 환경

## 기타 명령어

- git log --oneline : commit 목록 한 줄로 보기

- q 버튼 : end 상태에서 못 나올 때 나오게 하는 버튼
  
  - git config --global -l : git global 설정 정보 보기

- ls -a : 숨김 폴더까지 표시(폴더 이름 앞 . : 숨김 ex) .git/)

- rm -r .이름/ : 숨긴 폴더 제거 -> master 표시 제거

## Remote Repository

- 온라인 repository(3번째 영역)

- 코드와 버전 관리 이력을 온라인 상의 특정 위치에 저장하여 여러 개발자가 협업하고 코드를 공유할 수 있는 저장 공간

- Gitlab, Github, Bitbucket ...

- **git remote** add origin 주소 : 로컬 저장소에 원격 저장소 추가

- (https://github.com/jazzy712/ssafy-git) : 별칭(origin)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-09-16-image.png)

- git remote -v : 등록된 원격 저장소 목록 확인

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-09-46-image.png)

## Push

- **git push** origin(별칭) master : 원격 저장소에 commit 목록을 업로드

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-13-39-image.png)

- windows 자격 증명 -> 자리 변경 시    **지워야함!!** (github)

- github에 올라가는 것은  **commit** 이지, 드라이브의 개념이 아님(파일을 새로 만든다고 올라가는 것이 아님)

- 로컬 저장소에 변경 사항 -> push -> 변경사항만큼 업로드됨

- push 가 되지 않는다면 원격 저장소와 로컬 저장소의 과거 내역들이 일치하지 않아서임

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-47-40-image.png)

## Pull&Clone

- 원격 저장소의 변경사항만을 받아옴(업데이트) 
  
  ```bash
  git pull origin master
  ```

- **git clone** origin(별칭) master : 원격 저장소 전체를 복제(다운로드)
  
  - **clone** 으로 받은 프로젝트는 이미 **git init** 이 되어있음 

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-51-23-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-51-48-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-16-15-52-03-image.png)

- 다른 **로컬 저장소**에서 같은 별칭 사용 가능

- **원격 저장소**에 이미  commit이 존재하면 push 불가능, pull/clone으로 **로컬 저장소**로 commit을 맞춰주고 나서 push 해야함
  
  - **README.md** 은 원격 저장소의 메인 페이지에 내용이 노출됨(저장소의 가이드라인                                            제시)
