## Modules

- Module
  
  - 개발자 혼자 힘으로 프로그램 전체를 작성하는 것은 드문 일
  
  - 다른 프로그래머가 작성해 놓은 수많은 코드를 활용하는 것은 생산성에서 매우 
    
    중요한 일
  
  - 한 파일로 묶인 변수와 함수의 모음
  
  - 특정한 기능을 하는 코드가 작성된 파이썬 파일(.py)
  
  - math 내장 모듈
    
    - 파이썬이 미리 작성해 둔 수학 관련 변수와 함수가 작성된 모듈
    
    ```python
    import math
    import random
    import datetime
    
    print(math.pi) # 3.141592653589793
    print(math.sqrt(4)) # 2.0
    
    print(random.randint(1, 10)) 
    
    now = datetime.datetime.now()
    print(now)
    ```

- module 활용
  
  - module을 가져오는 방법
    
    - import 문 사용
    
    ```python
    import math
    
    print(math.sqrt(4))
    ```
    
    - from 절 사용
      
      ```python
      from math import sqrt
      
      print(sqrt(4)) # import문과 다르게 module을 표기하지 않는다
      ```

- ' . (dot)'   연산자
  
  - 점의 왼쪽 객체에서 점의 오른쪽 이름을 찾아라

```python
# 모듈명.변수명
print(math.pi)

# 모듈명.함수명
print(math.sqrt(4))
```

- module 주의사항
  
  - 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생
  
  - 마지막에 import된 이름으로 대체됨

```python
from math import pi, sqrt
from my_math import sqrt
```

```python
# 그래서 모듈 내 모든 요소를 한번에 import하는 * 표기는 권장하지 않음

from math import * # X
```

- ' as ' 키워드
  
  - 별칭(alias) 부여
    
    - 두 개 이상의 모듈에서 동일한 이름의 변수, 함수 클래스 등을 가져올 때 발생하는 이름 충돌 해결
  
  ```python
   from math import sqrt
   from my_math import sqrt as my_sqrt
  
   sqrt(4)
   my_sqrt(4)
  ```

- 사용자 정의 module 

```python
import my_math

print(my_math.add(1, 2))
```

- 파이썬 표준 라이브러리
  
  - 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음

- 패키지
  
  - 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것
  
  ```python
  from my_package.math import my_math
  from my_package.statistics import tools
  
  print(my_math.add(1, 2))
  print(tools.mod(1, 2))
  ```
  
  - psl 내부 패키지
    
    - 설치 없이 바로 **import** 하여 사용
  
  - **외부 패키지**
    
    - **pip** 사용하여 설치 후 **import** 필요
    
    - **pip**
      
      - 외부 패키지들을 설치하도록 도와주는 파이썬의 패키지 관리 시스템
      
      - PyPI(Python Package Index)에 저장된 외부 패키지들 설치

- 패키지 설치
  
  - 최선 버전 / 특정 버전 / 최소 버전을 명시하여 설치 가능
  
  ```python
  $ pip install SomePackage
  $ pip install SomePackage==1.0.5
  $ pip install SomePackage>=1.0.4
  
  # 삭제
  $ pip uninstall SomePackage
  ```

- requests  외부 패키지 설치 및 사용
  
  ```python
  $ pip install requests # 외부 API 서버로 요청
  ```

```python
# HTTP 요청을 보낼 수 있도록 도와주는 requests 라이브러리 import
import requests

# 무작위 사용자 정보를 제공해주는 API의 URL
url = 'https://random-data-api.com/api/v2/users'

# requests.get(url)을 통해 API에 요청을 보냄 
# 서버로부터 응답(Response)을 JSON 형태로 받아 Python 객체(딕셔너리/리스트 등)로 변환
response = requests.get(url).json() # 중

# 받은 응답 데이터(딕셔너리 형태)를 출력
print(response)

print(type(response)) # class 'dict'
```



- 패키지 사용 목적
  
  - 모듈들의 이름 공간을 구분하여 충돌 방지
  
  - 모듈들 효율적 관리하고 재사용할 수 있도록 돕는 역할
