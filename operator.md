## 연산자

- 산술 연산자

- 복합 연산자
  
  - 연산과 할당이 함께 이뤄짐
  
  - 순서가 중요

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-10-39-42-image.png)

```python
# 복합 연산자
y = 10
y -= 4
# y = y - 4
print(y)  # 6

z = 7
z *= 2
print(z)  # 14

w = 15
w /= 4
print(w)  # 3.75

q = 20
q //= 3
print(q)  # 6
```

- 비교 연산자
  
  - **==** 비교 연산자
    
    - 값(데이터)가 같은지를 비교
    
    - 동등성(equality)
    
    - **1 == True** 의 경우 파이썬이 내부적으로 **True**를 **1**로 간주할 수 있으므로 **True** 결과가 나옴
  
  - **is** 비교 연산자
    
    - 객체 자체가 같은지를 비교
    
    - 식별성(identitiy)
    
    - 두 변수가 동일한 메모리 주소(레퍼런스)를 가리키고 있을 때만 **True** 
  
  - **is** 대신 **==** 의 사용이유
    
    - is는 객체의 식별성(identities)을 비교하므로, 숫자나 문자열 같은 값 자체를 비교하려는 상황에서는 적절치 않음
    
    - is 연산자를 이용하면 코드 상에서의 의도치 않게 False가 나오거나 파이썬 버전에 따라 내부 구현 차이 때문에 기대하는 결과가 달라질 수 있음
    
    - 예를 들어,  is를 사용하면 항상 **False**가 나오지만 실제로 데이터 값은 논리적으로  같기 때문에 ==를 써야 의미가 더 맞음
  
  - **is** 는 언제 사용하는가? - **None** 비교
    
    - 1.  **None** 을 비교를 비교 할때
      
      2-   싱글턴 객체를 비교 할 때
    
    - "같은 주소에 있는가?" 라는 질문에 답해야 할 때 사용
    
    - 파이썬 공식 스타일 가이드에서는  **None**을 비교할 때 **==** 대신 **is**를 사용하라고 권장
    
    - 싱글턴(Singleton) 객체
      
      - 프로그램 전체에서 오직 1개만 존재하도록 만들어진 특별한 객체
      
      - **None, True, False**
    
    - 이들은 파이썬 전체에서 딱 1개만 사용되며, 새로 만들어지는게 아니라, 미리 정해진 하나의 객체가 재사용되기 때문에, 여러 곳에서 쓰더라도 같은 메모리 주소 가리킴
  
  - **==** 와 **is** 정리
    
    - 값 비교에는 **==** 을 사용하고, 객체(레퍼런스) 비교에는 **is**를 사용하는 것이 원칙
    
    - 숫자나 문자열, 불리언 값 등 동등성(값) 을 판단해야 할 때 **is**를 쓰면 의도치 않은 결과(**False**)가 나올 수 있으며, 이는 파이썬 내부적인 최적화나 타입 차이로 인해 일관성이 깨질 수 있기 때문
    
    - **is**는 주로 **None** 비교나, 싱글턴 객체(ex: **True, False**)에 대한 정체성 체크에 
      
      사용



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-10-42-37-image.png)

**!** -> not / 부정

```python
# 비교 연산자
print(3 > 6)  # False

# == 비교 연산자
print(2.0 == 2)  # True
print(2 != 2)  # False
print('HI' == 'hi')  # False 
print(1 == True) # True
```

```python
# is 비교 연산자
# SyntaxWarning: "is" with a literal. Did you mean "=="?
print(1 is True)  # False
print(2 is 2.0)  # False
```

```python
# 왜 is 대신 ==를 사용해야 하나?
print(1 is True)  # False
print(2 is 2.0)  # False
print(1 == True)  # True
print(2 == 2.0)  # True
```

```python
# is 연산자는 언제 사용하는가?
x = None

# 권장
if x is None:
    print('x는 None입니다.')

# 비권장
if x == None:
    print('x는 None입니다.')
```

```python
# 싱글턴 객체
x = True
y = True

# True, False, None은 실제로 같은 객체를 가리킨다.
print(x is y)  # True
print(True is True)  # True
print(False is False)  # True
print(None is None)  # True
```

- 리스트나 객체 비교
  
  - 리스트 또는 다른 가변 객체(mutable)를 비교할 때, 값 자체가 같은지 확인하려면 ==를 사용
  
  - 두 변수가 완전히 동일한 객체를 가리키는지를 확인해야 한다면 **is**를 사용

```python
# 추가 예시: 리스트나 객체 비교
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True (두 리스트의 값은 동일)
print(a is b)  # False (서로 다른 리스트 객체)

# b가 a를 그대로 참조하도록 할 경우
b = a
print(a is b)  # True (같은 객체를 가리키므로 True)
```

- 논리 연산자
  
  - 비교 연산자와 함께 사용 가능



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-10-54-25-image.png)

```python
# 논리 연산자
print(True and False)  # False
print(True or False)  # True
print(not True)  # False
print(not 0)  # True
```

```python
# 논리 연산자 & 비교 연산자
num = 15
result = (num > 10) and (num % 2 == 0)
print(result)  # False

name = 'Alice'
age = 25
result = (name == 'Alice') or (age == 30)
print(result)  # True
```

- 단축평가
  
  - 논리 연산에서 **두 번째 피연산자를 평가하지 않고** 결과를 결정하는 동작
  
  - 코드 실행 최적화, 불필요한 연산 피할 수 있도록 함
  
  - **and**
    
    - 첫 번째 피연산자가 **False**인 경우, 전체 표현식은 **False**로 결정
      
      두 번째 피연산자는 평가되지 않고, 그 값이 무시
    
    - 첫 번째 피연산자가  **True**인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정
      
      두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반환
  
  - **or**
    
    - 첫 번째 피연산자가  **True**인 경우, 전체 표현식은 **True**로 결정
      
      두 번째 피연산자는 평가되지 않고 그 값이 무시
    
    - 첫 번째 피연산자가 **False**인 경우, 전체 표현식의 결과는 두 번째 피연산자에 의해 결정
      
      두 번째 피연산자가 평가되고 그 결과가 전체 표현식의 결과로 반횐

```python
vowels = 'aeiou'

print(('a' and 'b') in vowels)  # False
print(('b' and 'a') in vowels)  # True

print(3 and 5)  # 5
print(3 and 0)  # 0
print(0 and 3)  # 0
print(0 and 0)  # 0

print(5 or 3)  # 5
print(3 or 0)  # 3
print(0 or 3)  # 3
print(0 or 0)  # 0
```

- 멤버십 연산자



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-11-01-13-image.png)



- 시퀀스형 연산자



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-11-01-54-image.png)

```python
# 시퀀스형 연산자

# Gildong Hong
print('Gildong' + 'Hong')  

#hihihihihi
print('hi' * 5)  

# [1, 2, 'a', 'b']
print([1, 2] + ['a', 'b'])  

# [1, 2, 1, 2]
print([1, 2] * 2)  
```

- 연산자 우선순위



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-11-02-35-image.png)



-  Trailing Comma
  
  - 컬렉션의 마지막 요소 뒤에 붙는 쉼표
  
  - 일반적으로 작성은 '선택사항'
  
  - 단, 하나의 요소로 구성된 튜플을 만들 때는 필수
  
  - 각 요소를 별도의 줄에 작성
  
  - 마지막 요소 뒤에 trailing comma 추가
  
  - 닫는 괄호는 새로운 줄에 배치

```python
x = 1 # 정수
x = (1) # 정수

x = 1, # 튜플
x = (1,) # 튜플
```

```python
items = [
    'item 1',
    'iten 2',
    'item 3',  
]

config = {
    'host' : 'localhost',
    'port' : 8080,
    'debug' : True
}
```

```python
# Good

items = [
    'item 1'
    'item 2'
]

my_func(
    'value1',
    'value2',
)
```

```python
# Bad

items = ['item1', 'item2',]

my_func('value1', 'value2',)
```

```python
# 한 줄 작성 시에는 불필요

items = ['item1', 'item2']

my_func('value1', 'value2')
```


