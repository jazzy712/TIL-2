## Revert & Reset

- **Git Revert**
  
  - 특정 commit을 없었던 일로 만드는 작업
    
    ```bash
    git revert <commit id>
    ```
  
  - "재설정"
  
  - 단일 commit을 실행 취소
  
  - 프로젝트 기록에서 commit을 없었던 일로 처리 후 그 결과를 새로운 commit으로 추가
  
  - 변경 사항을 지웠다는 사실을 다음 commit으로 남김
  
  - commit 은 이전의 commit 에 이어지게 됨
  
  - revert를 하게되면 pull을 받으면 됨

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-11-13-29-image.png)

- **Vim**
  
  - 입력모드/명령모드
  
  - insert -> 입력모드
  
  - esc버튼 -> 명령모드
  
  - 명령모드 - : 입력 후 명령어 입력
  
  - w : write, q : quit
  
  - :wq - > vim 종료시키는 명령어
  
  - second commit를 revert하고 git log -> second commit은 삭제되지 않고 새로운 commit이 작성됨

- **Git revert** 정리
  
  - 변경 사항을 안전하게 실행 취소할 수 있도록 도와주는 순방향 실행 취소 작업
  
  - commit 기록에서 commit을 삭제하거나 분리하는 대신, 지정된 변경 사항을 반전시키는 새 commit을 생성
    
    -> git에서 기록이 손실되는 것을 방지하며 기록의 무결성과 협업의 신뢰성 향상

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-11-29-28-image.png)

- **Git reset**
  
  - 특정 commit으로 되돌아가는 작업    
    
    ```bash
    git reset [옵션] <commit id>
    ```
  
  - "되돌리기"
  
  - 특정 commit으로 되돌아 갔을 때, 되돌아간 commit 이후의 모든 commit 삭제
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-11-32-07-image.png)

- **삭제되는 commit들의 기록을 어떤 영역에 남겨둘 것인지** 옵션을 활용해 조정가능

- 삭제된 commit의 기록을 **staging area**에 남김
  
  ```bash
  --soft
  ```

- 삭제된 commit의 기록을 **working directory**에 남김(기본 옵션 값)
  
  ```bash
  --mixed         
  ```

- 삭제된 commit의 기록을 남기지 않음
  
  ```bash
  --hard
  ```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-11-35-38-image.png)

- git reflog
  
  - HEAD가 이전에 가리켰던 모든 commit을 보여줌
  
  - reset의 **--hard**옵션을 통해 지워진 commit도 **reflog**로 조회하여 복구 가능

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-11-43-51-image.png)

- **git restore**
  
  - modified 상태의 파일 되돌리기
  
  - working directory에서 파일 수정 후 파일의 수정 사항 취소하고 원래 모습대로 되돌리는 작업
  
  - git-undoing-practice 폴더 생성 -> 생성 폴더 이동 -> vscode 실행 -> git init -> README.md 파일이 git에 의해 버전 관리가 될 수 있도록 첫 commit 작성
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-17-12-09-22-image.png)
  
  - 원래 파일로 덮어쓰는 원리이기 때문에 수정 내용 전부 사라짐
  
  - git restore 통해 수정 취소 후 해당 내용 복원 불가능

- staging area에 올라간 파일  unstage
  
  - staging area에서  working directory로 되돌리기(git 저장소에 "commit이 **없는** 
    
    경우")
    
    ```bash
    git rm --cached
    ```
  
  - git-unstage-practice 폴더 생성 -> 생성 폴더 이동 -> vscode 실행 -> git init
  
          -> README.md 생성 -> git add . -> git status -> git rm --cached -> git status

- staging area에서 working directory로 되돌리기(git 저장소에 "commit이 **존재하는** 
  
  경우")
  
  ```bash
  git restore --staged
  ```
  
  - commit 생성 -> README.md 재수정 후 저장 -> git add . ->  git restore --staged
