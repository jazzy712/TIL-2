## Python

- Program
  
  - 프로그래밍 - **문제를 해결**

- 쉽고 간결한 문법
  
  - 복잡한 논리 구조 알고리즘  이해와 구현

- 파이썬 커뮤니티의 지원

- 광범위한 응용 분야

- 강력한 표준 라이브러리
  
  - 다양한 알고리즘 구현에 필요 도구 제공

- 빠른 프로토타이밍
  
  - 알고리즘 빠르게 테스트와 수정

- 파이썬 <-> **파이썬 인터프리터** <-> 운영 체제

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-10-24-25-image.png)

- 파이썬 인터프리터
  
  - shell이라는 프로그램으로 한 번에 한 명령어 씩 입력해서 실행
    
    ```bash
    python -i
    ```
  
  - 확장자가 .py인 파일에 작성된 파이썬 프로그램 실행
    
    ```bash
    python sample.py
    ```

- 표현식
  
  - 값으로 평가될 수 있는 코드 조각
  
  - 값 : 표현식이 평가된 결과
  
  - 표현식이 **평가**되어 값이 **반환**됨
  
  - 평가 : 표현식을 실행하여 값을 얻는 과정
  
  - **표현식을 순차적으로 평가하여 프로그램의 동작 결정**
  
  - 문장 : 실행 가능한 동작 기술 코드 (조건문,반복문,함수 정의...)
  
  - 문장은 보통 여러 개의 표현식 포함

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-10-35-13-image.png)

-     타입
  
  - 변수나 값이 가질 수 있는 데이터의 종류
  
  - 어떤 종류의 데이터인지, 어떻게 해석되고 처리되어야 하는지를 정의
  
  - "**값"** 과 ""**값에 적용할 수 있는 연산**"" 으로 이루어짐

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-10-38-20-image.png)

- 데이터 타입
  
  - 값의 종류와 그 값에 적용 가능한 연산과 동작을 결정하는 속성
  
  - 값들을 구분하고, 어떻게 다뤄야 하는지를 알 수 있음
  
  - 요리 재료마다 특정한 도구가 필요하듯이 각 데이터 타입 값들도 각자에게 적합한
    
    도구를 가짐
  
  - 타입을 명시적으로 지정하면 코드를 읽는 사람이 변수의 의도를 더 쉽게 이해할 수 있고, 잘못된 데이터 타입으로 인한 오류를 사전예방
  
  - numeric type
    
    - int(정수), float(실수), complex(복소수)
      
      - int (integer) : 정수 자료형
      - float : 실수 자료형 - 실수에 대한 **근삿값**
    
    - 2진수(binary) : 0b
    
    - 8진수(octal) : 0o
    
    - 16진수(hexademical) : 0x
      
          print(0b10) # 2
          print(0o30) # 24
          print(0x10) # 16text sequence type
    
    - e 또는 E를 사용한 지수 표현# 314 * 0.01

- text sequence type
  
  - str(문자열)

- non-sequence types

- boolean, none, functions ...

- 데이터 타입에 맞는 연산을 타입이 수행

- -(음수부호), +(덧셈), -(뺄셈), *(곱셈), /(나눗셈), //(몫), %(나머지), **(거듭제곱)

- ** -> - -> *./,//,% -> +,- : 연산자 우선순위

- -2 ** 4 = -16, -(2 ** 4) = -16, (-2) ** 4 = 16

- 변수
  
  - 값을 저장하기 위한 이름 -> 값을 **참조**하기 위한 이름
  
  - 변수 할당
    
    - 표현식을 통해 변수에 값을 저장 
  
  ```bash
  degrees = 36.5
  ```
  
  - "" 변수 degrees에 값 36.5를 **할당**했다."" - 할당문
  
  ```bash
  degrees = 'abc'
  ```
  
  - "" 변수 degrees에 값 'abc'를 **재할당**했다.""

- 할당문
  
      variable = expression
  
  1. 할당 연산자(=) 오른쪽에 있는 표현식을 평가해서 값(메모리 주소)을 생성
  
  2. 값의 메모리 주소를 '=' 왼쪽에 있는 변수에 저장
  - 존재하지 않는 변수라면
    
    - 새 변수를 생성 (할당)
  
  - 기존에 존재했던 변수라면
    
    - 기존 변수를 재사용해서 변수에 들어 있는 메모리 주소를 변경 (재할당)
  
  - 거리에 집 주소가 있듯이 메모리의 모든 위치에는 그 위치를 고유하게 식별하는     메모리 주소가 존재
  
  - 객체 
    
    - 타입을 갖는 메모리 주소 내 값
    
    - "값이 들어있는 상자"
  
  - 변수는 그 변수가 참조하는 객체의 메모리 주소를 가짐
  
  - 변수 degrees는 값 36.5를 참조
  
  ```bash
  number = 10
  double = 2 * number
  print(double)  # 20
  
  number = 5
  print(double)  # 20
  ```

- 지수 표현 방식
  
  - e 또는 E를 사용한 지수 표현
    
    ```bash
    # 314 * 0.01
    number = 314e-2
    # 3.14
    print(number)
    ```

- 유한 정밀도
  
  - 컴퓨터 메모리 용량은 한정, 한 숫자에 대해 저장하는 용량이 제한
    
    # 0.66666666666666
    
      print(2 / 3)
    
    # 1.66666666666667
    
      print(5 / 3)
  
  - 컴퓨터는 2진수, 사람은 10진법 사용
  
  - 10진수 0.1은 2진수로 표현하면 0.0001100110011001100... 무한대로 반복
  
  - 무한대 숫자를 그대로 저장할 수 없어서 사람이 사용하는 10진법의 근삿값만 표시
  
  - 0.1의 경우 3602879701896397 / 2 ** 55 이며 0.1에 가깝지만 정확히 동일 x
  
  - 이런 과정에서 예상치 못한 결과 -> **부동소수점 에러**

- 부동소수점 에러 해결책
  
  - **decimal** 모듈 사용해 부동소수점 연산의 정확성 보장
  
  ```bash
  a = 3.2 - 3.1
  b = 1.2 - 1.1
  print(a) # 0.100000000009
  print(b) # 0.099999999987
  print(a -- b) # False
  ```

->              

```bash
from decimal import Decimal

a = Decimal('3.2') - Decimal('3.1')
b = Decimal('1.2') - Decimal('1.1')

print(a) # 0.1
print(b) # 0.1
print(a --b) # True
```

- Sequence Types
  
  - **여러 개의 값들**을 **순서대로 나열**하여 저장하는 자료형
  
  - str, list, tuple, range
  
  - 순서(sequence)
    
    - 값들이 순서대로 저장(정렬 x)
  
  - 인덱싱(indexing)
    
    - 각 값에 고유한 인덱스(번호) 갖고 있으며, 인덱스를 사용하여 특정 위치의 값을 선택하거나 수정 가능
  
  - 슬라이싱(slicing)
    
    - 인덱스 범위를 조절해 부분적인 값 추출
  
  - 길이(length)
    
    - len() 함수를 사용해 저장된 값의 개수(길이)를 구할 수 있음
  
  - 반복(lteration)
    
    - 반복문을 사용하여 저장된 값들을 반복적으로 처리 가능
  
  - Str 
    
    - 문자들의 순서가 있는 **변경 불가능한** 시퀀스 자료형
    
    - 문자열은 단일 문자나 여러 문자의 조합으로 이루어짐
    
    - 작음따옴표(') 또는큰따옴표(")로 감싸서 표현 -> 섞어쓰면 안됨
  
  ```bash
  # Hello, World!
  print('Hello, World!')
  
  #str
  print(type('Hello, World!'))
  ```
  
  - 중첩 따옴표
    
    - 따옴표 안에 따옴표 표현
      
      - 작은따옴표가 들어있는 경우는 큰따옴표로 문자열 생성
      
      - 큰따옴표가 들어있는 경우는 작은따옴표로 문자열 생성

- Escape Sequence
  
  - 역슬래시(backslash, \) 뒤에 특정 문자가 와서 특수한 기능을 하는 문자 조합
  
  - 파이썬의 일반적인 문법 규칙을 잠시 탈출
  
  - \n : 줄바꿈
  
  - \t : 탭
  
  - \\\ : 백슬래시
  
  - \' : 작음따옴표
  
  - \" : 큰 따옴표

- String Interpolation
  
  - 문자열 내에 변수나 표현식 삽입

```bash
# 철수야 '안녕'
print('철수야 \'안녕'')


'''
이 다음은 엔터
입니다.
'''
print('이 다음은 엔터\n입니다.')
```

- f-string
  
  - 문자열에 f 또는  F 접두어를 붙이고 표현식을 {expression}로 작성하는 문법
  
  - 문자열에 파이썬 표현식의 값을 삽입 가능

```bash
bugs = 'roaches'
counts = 13
area = 'living room'

# Debugging roaches 13 living room
print(f'Debugging {bugs}{counts}{area})
```

- 문자열의 시퀀스 특징

```bash
my_str = 'hello'

# 인덱싱
print(my_str[1]) # e


# 슬라이싱
print(my_str[2:4]) # ll

# 길이
print(len(my_str)) # 5
```

- 인덱스
  
  - 시퀀스 내의 값들에 대한 고유번호, 각 값의 위치 식별하는데 사용되는 숫자

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-39-26-image.png)

- 슬라이싱
  
  - 시퀀스의 일부분을 선택하여 추출
  
  - 시작 인덱스와 끝 인덱스를 지정하여 해당 범위의 값을 포함하는 새로운 시퀀스 생성
  
  - 인덱스 [a:b] = a부터 b 사이(이상, 미만)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-40-35-image.png)

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-42-37-image.png)

-> 시작지점 생략 가능

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-43-05-image.png)

-> 끝지점 생략 가능

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-44-10-image.png)

-> step : 2

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-20-14-45-13-image.png)

-> 음수의 step ->   **문자열 뒤집기**

- 불변의 문자열(변경 불가)

```bash
my_str='hello'

# TypeError: 'str' object does not support item assignment
my_str[1] ='z'
```

- Style Guide
  
  - 코드의 일관성가 가독성을 향상시키기 위한 규칙과 권장 사항들의 모음
  
  - 변수명은 무엇을 위한 변수인지 **직관적인 이름**을 가져야함
  
          -> a=1 이라는 변수 설정 x
  
  - 공백(spaces) 4칸을 사용하여 코드 블록을 들여쓰기
  
  - 한 줄의 길이는 79자로 제한하며, 길어질 경우 줄 바꿈을 사용
  
  - 문자와 밑줄(__)을 사용하여 함수,변수,속성의 이름을 작성
  
  - 함수 정의나 클래스 정의 등의 블록 사이에는 빈 줄을 추가

- 변수명 규칙
  
  - 영문 알파벳, 언더스코어(__), 숫자로 구성
  
  - 숫자로 시작할 수 없음
  
  - 대소문자를 구분
  
  - 아래 키워드는 파이썬의 내부 예약어로 사용x
  
  ['False', 'None', 'True', '______peg_parser______', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield' ]

- 주석(Comment)
  
  - 프로그램 코드 내에 작성되는 설명이나 메모
  
  - 인터프리터에 의해 실행되지 않음
  
  - ctrl + /
  
  - 코드의 특정 부분 설명하거나 임시로 코드 비활성화
  
  - 코드를 이해하거나 문서화
  
  - 다른 개발자나 자신에게 코드의 의도나 동작 설명

```bash
# 이것은
age = 10

#주석입니다
print(age)
```
