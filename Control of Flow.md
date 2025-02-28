## Control of Flow(제어문)

- 제어문
  
  - 코드의 실행흐름 제어하는데 사용되는 구문
  
  - **조건**에 따라 코드 블록 실행하거나 **반복**적으로 코드 실행
  
  - 조건문
    
    - if, elif, else
  
  - 반복문
    
    - for, while
  
  - 반복문 제어
    
    - break, continue, pass

- **조건문(condtional statement)**
  
  - 주어진 조건식 평가하여 해당 조건이 참(True)인 경우에만 코드 블록 실행하거나 
    
    건너뜀
  
  - if / elif / else
  
  - **' if '** 문
  
  - 복수 조건문
    
    - 조건식을 동시에 검사하는 것이 아니라 "순차적"으로 비교
  
  - 중첩 조건문

```python
if 표현식: 
    코드 블록
elif 표현식: 
    코드 블록 
else: 
    코드 블록
```

```python
a = 5

if a > 3:
    print('3 초과')
else:
    print('3 이하')

print(a)
```

```python
dust = 35

if dust > 150:
    print('매우 나쁨')
elif dust > 80:
     print('나쁨')
elif dust > 30:
     print('보통')
else:
     print('좋음')                             # 복수 조건문
```

```python
dust = 480

if dust > 150:
     print('매우 나쁨')
     if dust > 300:
        print('위험해요!')
elif dust > 80:
     print('나쁨')
elif dust > 30:
     print('보통')
else:
     print('좋음')                             # 중첩 조건문
```

- **반복문(Loop Statemet)**
  
  - 주어진 코드 블록을 여러 번 반복해서 실행
  
  - **for** 
    
    - 특정 작업 반복적 수행
  
  - **while**
    
    - 주어진 조건이 참(True)인 동안 반복 실행

- **for 반복문**
  
  - 임의의 시퀀스 항목들을 그 시퀀스에 들어있는 순서대로 반복
  
  - 리스트 내 첫 항목이 반복 변수에 할당되고 코드블록 실행
  
  - 다음으로 반복 변수에 리스트의 2번째 항목이 할당되고 코드 블록 실행
  
  - 마지막으로 반복 변수에 리스트의 마지막 요소가 할당되고 코드 블록 실행
  
  - 반복 횟수가 명확하게 정해져 있는 경우 유용
  
  - list, tuple. 문자열 등과 같은 시퀀스 형식의 데이터 처리할 때
  
  ```python
  for 변수 in 반복 가능한 객체:
      코드 블록                     # for 반복문의 기본 구조
  ```
  
  ```python
  items = ['apple', 'banana', 'coconut']
  
  for item in items:
      print(item)
  
  """
  apple
  banana
  coconut
  """
  ```
  
  ```python
  country = 'Korea'
  
  for char in country:
      print(char)
  
  """
  K
  o
  r
  e           
  a
  """                              # 문자열 순회
  ```
  
  ```python
  for i in range(5):
      print(i)
  
  """
  0
  1
  2
  3
  4
  """                               # range 순회
  ```
  
  ```python
  my_dict = {
      'x': 10,
      'y': 20,
      'z': 30,
  }
  
  for key in my_dict:
      print(key)
      print(my_dict[key])
  
  """
  x
  10
  y
  20
  z
  30
  """
                                     # 딕셔너리 순회
  ```
  
  ```python
  numbers = [4, 6, 10, -8, 5]
  
  for i in range(len(numbers)):
      numbers[i] = numbers[i] * 2
  
  print(numbers)  # [8, 12, 20, -16, 10]      # 인덱스로 리스트 순회
  ```
  
  ```python
  outers = ['A', 'B']
  inners = ['c', 'd']
  
  for outer in outers:
      for inner in inners:
          print(outer, inner)
  """
  A, c
  A, d
  B, c
  B, d
  """                                 # 중첩 반복문
  ```
  
  ```python
  elements = [['A', 'B'], ['c', 'd']]
  
  for elem in elements:
      print(elem)  # ['A', 'B'] ['c', 'd']
  
  for elem in elements:
      for item in elem:
          print(item)  # A B c d      # 중첩 리스트 순회
  ```

- 반복 가능한 객체(iterable)
  
  - 반복문에서 순회할 수 있는 객체(시퀀스 객체뿐 아니라 **dict, set** 등 포함)

- while 반복문
  
  - 주어진 조건식이 참(True)인 동안 코드를 반복해서 실행 
  
  - == 조건식이 거짓(False)가 될 때까지 반복
  
  - 반드시 **종료 조건**이 필요
  
  - 반복 횟수가 불명확하거나 조건에 따라 반복 종료해야 할때
  
  - 사용자 입력을 받아서 특정 조건이 충족될 때까지 반복

```python
while 조건식:
    코드 블록                              # while 반복문 기본 구조
```

```python
a = 0

while a < 3:
    print(a)
    a += 1

print('끝')

"""
0
1
2
끝
"""                                     # while 문 예시 
```

```python
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')                       # while 문 예시2    
```

- 반복 제어
  
  - for 문과 while은 매 반복마다 본문 내 모든 코드 실행하지만 때때로 일부만 실행하는 것이 필요할 때가 있음
  
  - break
    
    - 반복 즉시 중지
  
  - continue
    
    - 다음 반복으로 건너뜀
  
  - pass
    
    - 아무런 동작도 수행하지 않고 넘어감 
    
    - 코드 작성 중 미완성 부분
      
      - 구현해야 할 부분이 나중에 추가될 수 있고, 코드를 compile하는 동안 오류가 발생하지 않음
    
    - 조건문에서 아무런 동작을 수행하지 않아야 할 때
    
    - 무한 루프에서 조건이 충족되지 않을 때 pass를 사용하여 루플를 계속 진행하는 방법

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i) # 0 1 2 3 4
```

```python
# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i) # 1 3 5 7 9
```

```python
# pass
for i in range(10):
    pass # 아무 작업도 안함
```

```python
# break 예시 1 - "프로그램 종료 조건 만들기"
number = int(input('양의 정수를 입력해주세요.: '))
while number <= 0:
    if number == -9999:
        print('프로그램을 종료합니다.')
        break
    if number < 0:
        print('음수를 입력했습니다.')
    else:
        print('0은 양의 정수가 아닙니다.')
    number = int(input('양의 정수를 입력해주세요.: '))
print('잘했습니다!')

"""
양의 정수를 입력해주세요.: -9999
프로그램을 종료합니다.
잘했습니다!
"""
```

```python
# break 예시 2 - "리스트에서 첫번째 짝수만 찾은 후 반복 종료하기"
numbers = [1, 3, 5, 6, 7, 9, 10, 11]

# 첫 번째 짝수를 찾았는지 여부를 저장하는 플래그 변수
# 초기값은 찾지 못했다(False)로 설정
found_even = False

for number in numbers:
    if number % 2 == 0:
        print(f'첫번째 짝수 {number}를 찾았습니다.')
        # 짝수를 찾은 상태이므로 True로 변경
        found_even = True
        break


# 반복문이 끝날 때까지 짝수를 찾지 못한 경우
if found_even == False:
    print('짝수를 찾지 못함')

"""
첫 번째 짝수를 찾았습니다 : 6
"""
```

```python
# continue 예시 - "리스트에서 홀수만 출력하기"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in numbers:
    if num % 2 == 0:
        continue
    print(num)

"""
1
3
5
7
9
"""                     # 현재 반복문 남은 코드를 건너뛰고 다음 반복으로 넘어감
```

```python
if condition:
    pass # 아무런 동작도 수행하지 않음 
else:
    # 다른 동작 수행
```

- List comprehension
  
  - comprehenstion 을 남용하지 말자.
  
  - 2차원 배열 생성 시

```python
[expression for 변수 in iterable]

list(expression for 변수 in iterable)
```

```python
[expression for 변수 in iterable if 조건식]

list(expression for 변수 in iterable if 조건식)
```

```python
# 기존 방식
numbers = [1, 2, 3, 4, 5]
squared_numbers = []

for num in numbers:
    squared_numbers.append(num**2)

print(squared_numbers) # [1, 4, 9, 16, 25]

# 리스트 컴프리헨션
squared_numbers2 = [num**2 for num in numbers]
squared_numbers2 = list(num**2 for num in numbers)

print(squared_numbers2) # [1, 4, 9, 16, 25]
```

```python
# 리스트 컴프리헨션 with 조건문
# 기존 방식
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)

print(evens)  # [0, 2, 4, 6, 8]

# 리스트 컴프리헨션
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]
```

```python
data1 = [[0] * (5) for _ in range(5)]

# 또는
data2 = [[0] for _ in range(5)] for _ in range(5)]
```

```python
# 리스트를 생성하는 3가지 방법(기본 loop, list comprehension, map) 비교

"""
1. 기본 loop

특징
- 직관적으로 이해하기 쉽고, 복잡한 로직을 담기에도 용이
- 반복문 내부에서 여러 변수를 업데이트하거나, 특정 조건에 따라 continue/break가 필요한 경우 유리
"""
result1 = []
for i in range(10):
    result1.append(i)


"""
# 2. list comprehension
특징
- 파이썬스러운(Pythonic) 방식으로 간결한 코드 작성 가능
- 조건문을 넣거나, 중첩 for 문을 사용하는 등 다양한 패턴을 구현하기에도 용이
- 가독성을 해치지 않을 선에서 사용하는 것이 중요
"""
result2 = [i for i in range(10)]
# result2 = list(i for i in range(10))


"""
3. map
특징
- 함수형 프로그래밍 스타일을 선호하거나, 이미 정의된 함수를 적용해야 할 때 유용
- 이미 존재하는 함수에 여러 값을 한꺼번에 적용할 때 가독성이 좋아짐
- 복잡한 로직은 map 내부에서 처리하기가 난해하므로, 코드가 오히려 읽기 어려워질 수 있음
"""
result3 = list(map(lambda i: i, range(10)))
```

- module 내부 살펴보기
  
  - 내장함수 help를 사용해 module에 무엇이 들어있는지 확인 가능
  
  - **enumerate(iterable, start=0)**
    
    - iterable 객체의 각 요소에 대해 인덱스와 함께 반환하는 내장함수
  
  ```python
  fruits = ['apple', 'banana', 'cherry']
  
  for index, fruit in enumerate(fruits):
      print(index, fruit)
  
  """
  0 apple
  1 banana
  2 cherry
  """
  ```

```python
for index, fruit in enumerate(fruits, 3):
    print(index, fruit)

"""
3 apple
4 banana
5 cherry
"""
```
