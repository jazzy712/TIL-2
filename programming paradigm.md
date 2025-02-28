## Programming paradigm

- **절차 지향**(PP)
  
  - 프로그램을 함수와 로직 중심으로 작성
  
  - 데이터를 함수에 전달하며 순차적 처리
  
  - 변수와 함수를 별개로 다룸
  
  - 입력을 받고, 처리하고, 결과를 내는 과정이 위에서 아래로 순차적으로 흐르는 형태
  
  - 순차적인 명령어 실행
  
  - 데이터와 함수(절차)의 분리
  
  - **함수 호출의 흐름이 중요**
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-03-09-05-49-image.png)
  
  - 한계
    
    - 복잡성 증가
      
      - 프로그램 규모가 커질수록 데이터와 함수 관리가 어려움
      
      - 전역 변수 증가로 인한 관리 어려움
    
    - 유지보수 문제
      
      - 코드 수정 시 영향 범위 파악 어려움
    
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-03-09-06-50-image.png)
    
    ```python
    name = 'Alice'
    age = 25
    
    def introduce(name, age):
        print(f'안녕하세요, {name}입니다. 나이는 {age}살입니다.')
    
    introduce(name, age)
    ```

- **객체 지향**(OOP)
  
  - 데이터와 함수를 하나의 단위(객체)로 묶어서 관리
  
  - 객체들 조합하고 재활용하는 방식으로 프로그램 구성
  
  - 프로그램을 데이터(변수)와 데이터 처리하는 함수(메서드)들
  
  - 하나의(단위)로 묶어서 조직적 관리
  
  - 데이터와 메서드 결합
  
  - **객체 간 상호작용과 메시지 전달 중요**

```python
# 예: 사람(객체) 안에 name, age와 이와 관련된 기능(메서드) 포함
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f'안녕하세요, {self.name}입니다. 나이는 {self.age}살입니다.')

alice = Person('Alice', 25)
alice.introduce()  # 객체가 자신의 정보를 출력
```

- **객체**
  
  - 실제 존재하는 사물 추상화
  
  - "속성", "동작"
    
    - 속성 : 객체의 상태/데이터
    
    - 메서드 : 객체의 행동/기능
  
  - 고유성
    
    - 각 객체는 고유한 특성 가짐

- **클래스**
  
  - 객체 만들기 위한 설계도
  
  - 데이터와 기능 함께 묶는 방법 제공
  
  - 파이썬에서 타입 표현 방법
  
  - 사용자 정의 객체를 만드는 수단이자 속성과 메서드 정의
  
  - 클래스 이름은 파스칼 케이스(Pascal case) 방식으로 작성
    
    - 대문자로 시작
  
  - '_ _ init _ _' 메서드는 '생성자 메서드'로 불리며 새로운 객체 만들때 필요한 초기 값 설정    

```python
class MyClass:
    pass
```

```python
class Person:
    def __init__(self, name, age):            # 개발자가 실제로 호출 x
        self.name = name  # 인스턴스 속성
        self.age = age  # 인스턴스 속성

    def introduce(self):
        print(f'안녕하세요. 저는 {self.name}, 나이는 {self.age}살입니다.')
```

- **인스턴스**
  
  - 클래스 통해 생성된 객체
  
  - 클래스가 설계도라면 인스턴스는 실제로 만든 '개별 물건'
  
  - ex) 클래스 : 가수, 인스턴스 : 아이유

```python
p1 = Person('Alcice', 25)
p1.introduce() # "안녕하세요. 저는 Alice, 나이는 25살입니다"

p2 = Person('Bella', 30)
p2.introduce() # "안녕하세요. 저는 Bella, 나이는 30살입니다"
```

- 클래스와 인스턴스
  
  - 변수 name의 타입은 str 클래스다
  
  - 변수 name은 **str클래스의 인스턴스**이다.
  
  - "hello".upper()
    
    - 문자열.대문자로()
    
    - 객체.행동()
    
    - 인스턴스.메서드()
  
  - [1, 2, 3].sort()
    
    - 리스트.정렬해()
    
    - 객체.행동()
    
    - 인스턴스.메서드()
  
  - 하나의 객체는 특정 클래스의 인스턴스이다.

```python
name = 'Alice'

print(type('name'))  # <class 'str'>
```

- 클래스 구조
  
  - 생성자 메서드
    
    - 인스턴스 생성 시 자동 호출되는 특별 메서드
    
    - ____ __init_______ 이라는 이름의 메서드
    
    - 인스턴스 변수의 초기화 담당
  
  ```python
  class Circle:
      pi = 3.14                             # 클래스 변수
  
      def __init__(self, radius):           # 생성자 메서드        
          self.radius = radius              # 인스턴스 변수   
  
  # 인스턴스 생성
  c1 = Circle(1)
  c2 = Circle(2)
  ```
  
  - 인스턴스 변수
    
    - 각 인스턴스별 고유 속성
    
    - self.변수명 형태의 정의
    
    - 인스턴스마다 독립 값 유지
  
  - 클래스 변수(속성)
    
    - 모든 인스턴스 공유 속성
    
    - 클래스 내부에서 직접 정의
  
  ```python
  # 인스턴스 변수(속성)
  print(c1.radius) # 1
  print(c2.radius) # 2
  ```

- 클래스 변수와 인스턴스 변수
  
  - 클래스 변수와 동일한 이름으로 인스턴스 변수 생성 시 클래스 변수가 아닌 인스턴스 변수에 먼저 참조
  
  - **class.class_variable** 로 클래스 변수 참조 가능

```python
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius


c1 = Circle(5)
c2 = Circle(10)

print(c1.radius)  # 5
print(c2.radius)  # 10
```

```python
# c1의 인스턴스 변수 pi를 생성
c1.pi = 100

print(c1.pi)  # 100
print(Circle.pi)  # 3.14

# c2는 인스턴스 변수 pi가 없으므로 클래스 변수 pi를 참조
print(c2.pi)  # 3.14
```

- **메서드** 
  
  - 클래스 내부에 정의된 함수
  
  - 해당 객체가 어떻게 동작할지 정의
  
  - 인스턴스 메서드
  
  - 클래스 메서드
  
  - 스태틱 메서드

- **인스턴스 메서드**
  
  - 클래스로부터 생성된 각 인스턴스에서 호출할 수 있는 메서드
  
  - 인스턴스의 상태 조작하거나 동작 수행 
  
  - 반드시 첫 번째 인자로 **인스턴스 자신(self)** 을 받음
  
  - 인스턴스의 속성에 접근하거나 변경 가능
  
  - self 동작 원리
    
    - upper 메서드를 사용해 문자열 'hello'를 대문자로 변경
    
    ```python
    'hello'.uppper()
    ```
    
    - 하지만 실제 파이썬 내부 동작은 다음과 같이 진행
    
    ```python
    str.upper('hello')
    ```
    
    - str 클래스가 upper 메서드를 호출했고, 그 첫번째 인자로 문자열 인스턴스가 들어간 것
      
      -> 인스턴스 메서드의 첫 번째 인자가 반드시 인스턴스 자기 자신인 이유
    
    ```python
    'hello'.upper()
    ```
    
    ```python
    str.upper('hello')
    ```
    
    - 전자가 후자를 객체 지향 방식의 메서드로 호출하는 표현(단축형 표현)
    
    - 'hello'라는 문자열 객체가 단순히 어딘가의 함수로 들어가는 인자로 활용되는 것이 아닌 객체 스스로 메서드를 호출하여 코드를 동작하는 객체 지향적인 표현인 것
  
  ```python
  class MyClass:
  
      def instance_method(self, arg1, ...):       # self는 매개변수 이름일 뿐이며 
                                                    다른 이름으로 설정 가능
          pass
  ```

```python

class Counter:
  def __init__(self):
      self.count = 0

  def increment(self):
      self.count += 1


c = Counter()
c.increment()
print(c.count) # 1
```

- **생성자 메서드**
  
  - 인스턴스 객체가 생성될 때 자동으로 호출되는 메서드
  
  - 인스턴스 변수들의 초기값 설정

```python
class Person:
    def __init__(self, name):
        # 왼쪽 name : 인스턴스 변수 name
        # 오른쪽 name : 생성자 메서드의 매개변수 이름
        self.name = name
        print('인스턴스가 생성되었습니다.')

    def greeting(self):
        print(f'안녕하세요 {self.name}입니다.')


person1 = Person('지민')  # 인스턴스가 생성되었습니다.
person1.greeting()  # 안녕하세요. 지민입니다.
# Person.greeting(person1)   # 안녕하세요. 지민입니다.
```

- **클래스 메서드** 
  
  - 클래스가 호출하는 메서드
  
  - 클래스 변수를 조작하거나 클래스 레벨의 동작 수행
  
  - @classmethod 데코레이터 사용하여 정의
  
  - 호출 시, 첫 번째 인자로 해당 메서드를 호출하는 클래스(cls)가 전달됨
  
  - 클래스를 인자로 받아 클래스 속성을 변경하거나 읽는 데 사용

```python
class MyClass:

    @classmethod   
    def class_method(cls, arg1, ...):
        pass         # cls는 매개변수 이름일 뿐이며 다른 이름으로 설정가능 하지만 다른 이름으로 사용하지 않을 것 권
```

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name
        Person.increase_population()

    @classmethod
    def increase_population(cls):
        cls.population += 1    

person1 = Person('Alice')
person2 = Person('Bob')
print(Person.population)  # 2
```



- **스태틱 메서드**
  
  - 클래스, 인스턴스와 상관없이 독립적으로 동작하는 메서드
  
  - @staticmethod 데코레이터 사용하여 정의
  
  - 호출 시 자동으로 전달받는 인자가 없음(self,cls 받지않음)
  
  - 인스턴스나 클래스 속성에 직접 접근하지 않는, '도우미 함수'와 비슷한 역할

```python
class MyClass:

    @staticmethod
    def static_method(arg1, ...):
        pass
```

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b


print(MathUtils.add(3, 5))  # 8
```



- 메서드 활용

```python
# 입출금이 가능한 은행 계좌 클래스 만들기
# 은행 계좌를 모델링하는 클래스를 만들고, 입출금 기능(메서드)를 구현


class BankAccount:
    interest_rate = 0.02  # 이자율

    def __init__(self, owner, balance=0):
        self.owner = owner  # 계좌 소유자
        self.balance = balance  # 초기 잔액

    # 입금
    def deposit(self, amount):
        self.balance += amount

    # 출금
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print('잔액이 부족합니다다!')

    # 이자율 설정
    @classmethod
    def set_interest_rate(cls,rate):
        cls.interest_rate = rate

    # 금액이 양수인지 검증
    @staticmethod
    def is_positive(amount):
        return amount > 0


# 계좌 개설 (인스턴스 생성)
alice_acc = BankAccount('Alice', 1000)
print(alice_acc.owner)
print(alice_acc.balance)

# 입금 및 출금 (인스턴스 메서드 호출)
alice_acc.deposit(500)
alice_acc.withdraw(300)

# 잔액 확인 (인스턴스 변수 참조)
print(alice_acc.balance) # 1500
print(alice_acc.balance) # 1200

# 이자율 변경 (클래스 메서드 호출)
BankAccount.set_interest_rate(0.03)
print(BankAccount.interest_rate)  # 0.03

# 잔액이 양수인지 확인 (정적 메서드 호출)
BankAccount.is_positive(alice_acc.balance)
print(BankAccount.is_positive(alice_acc.balance)) # True
```



- 메서드 정리
  
  - 인스턴스 메서드
    
    - 인스턴스 상태 변경하거나, 해당 인스턴스의 특정 동작 수행
  
  - 클래스 메서드
    
    - 인스턴스의 상태에 의존하지 않는 기능 정의
    
    - 클래스 변수 조작하거나 클래스 레벨 동작 수행
  
  - 스태틱 메서드
    
    - 클래스 및 인스턴스와 관련이 없는 일반적 기능 수행
  
  - 클래스 사용
    
    - 클래스 메서드
    
    - 스태틱 메서드
  
  - 인스턴스 사용
    
    - 인스턴스 메서드

```python
class MyClass:
    def instance_method(self):
        return 'instance method', self

    @classmethod
    def class_method(cls):
        return 'class method', cls

    @staticmethod
    def static_method():
        return 'static method'
```

```python
instance = MyClass()

# 클래스가 할 수 있는 것
print(MyClass.instance_method(instance))
print(MyClass.class_method())
print(MyClass.static_method())
```

```python
# 인스턴스가 할 수 있는 것
print(instance.instance_method())
print(instance.class_method())
print(instance.static_method())
```

-> 클래스는 **클래스 메서드와 스태틱 메서드만** 사용하도록 한다

    인스턴스는 **인스턴스 메서드만** 사용하도록 한다



- 클래스와 인스턴스 간 이름 공간
  
  - 클래스 정의하면 클래스와 해당하는 이름 공간 생성
  
  - 인스턴스 만들면, 인스턴스 객체가 생성되고 **독립적인** 이름 공간 생성
  
  - 인스턴스에서 특정 속성 접근하면, 인스턴스 -> 클래스 순으로 탐색

```python
class Person:
    name = 'unknown'

    def talk(self):
        print(self.name)

p1 = Person()
p1.talk()  # unknown(p1은 인스턴스 변수가 정의되어 있지 않아 클래스 변수 unknown이 출력)

# p2 인스턴스 변수 설정 전/후
p2 = Person()
p2.talk()  # unknown
p2.name = 'Kim'
p2.talk()  # Kim(p2는 인스턴스 변수가 정의되어 인스턴스 변수 Kim이 출력)

print(Person.name)  # unknown
print(p1.name)  # unknown
print(p2.name)  # Kim(클래스 변수 name값이 Kim으로 변경된 것이 아닌 p2 인스턴스의 인스턴스 변수 name이 Kim으로 저장)
```



- 매직 메서드
  
  - double underscore('__') 가 있는 메서드는 특수한 동작을 위해 만들어진 메서드
  
  - 인스턴스 메서드
  
  - 특정 상황에 자동으로 호출
  
  - 스페셜 메서드 로도 불림
    
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-03-11-00-33-image.png)

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __str__(self):
        return f'원의 반지름: {self.radius}'


c1 = Circle(10)
c2 = Circle(1)

print(c1)  # 원의 반지름: 10
print(c2)  # 원의 반지름: 1
```



- 데코레이터
  
  - 다른 함수의 코드 유지한 채로 수정하거나 확장하기 위해 사용되는 함수

```python
# 데코레이터 정의
def my_decorator(func):
    def wrapper():
        # 함수 실행 전에 수행할 작업
        print('함수 실행 전')
        # 원본 함수 호출
        result = func()
        # 함수 실행 후에 수행할 작업
        print('함수 실행 후')
        return result
    return wrapper
```

```python
# 데코레이터 사용
@my_decorator
def my_function():
    print('원본 함수 실행')
my_function()

"""
함수 실행 전
원본 함수 실행
함수 실행 후
"""
```
