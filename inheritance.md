## Inheritance(상속)

- inheritance
  
  - 한 클래스(부모)의 속성과 메서드를 다른 클래스(자식)가 물려받는 것
  
  - 코드 재사용
    
    - 기존 클래스의 속성과 메서드 재사용
    
    - 수정하지 않고도 기능 확장
  
  - 계층 구조
    
    - 클래스들 간의 계층 구조 형성
    
    - 부모 클래스와 자식 클래스 간의 관계 표현, 더 구체적인 클래스 만들 수 있음
  
  - 유지 보수 용이
    
    - 코드 일관성 유지, 수정 필요범위 최소화

```python
class Animal:
    def eat(self):
        print('먹는 중')

class Dog(Animal):             # 상속의 기본 표현
    def bark(self):
        print('멍멍')

# 인스턴스 생성
my_dog = Dog()

# 인스턴스 메서드 호출 
my_dog.bark()  # 멍멍멍

# 부모 클래스(Animal) 메서드 사용 가능
my_dog.eat() # 먹는 중
```

 

- class inheritance
  
  - 상속 없이 구현 하는 경우
    
    ```python
    class Person: 
      def __init__(self, name, age):
          self.name = name
          self.age = age
    
      def talk(self):
          print(f'반갑습니다. {self.name}입니다.')
    ```

```python
  s1 = Person('김학생', 23)
  s1.talk()  # 반갑습니다. 김학생입니다.

  p1 = Person('박교수', 59)
  p1.talk()  # 반갑습니다. 박교수입니다.


  class Professor:
      def __init__(self, name, age, department):
          self.name = name
          self.age = age
          self.department = department

      def talk(self):  # 중복
          print(f'반갑습니다. {self.name}입니다.')

  class Student:
      def __init__(self, name, age, gpa):
          self.name = name
          self.age = age
          self.gpa = gpa

      def talk(self):  # 중복
          print(f'반갑습니다. {self.name}입니다.')     # 교수/학생 클래스로 분리했지만 메서드가 중복으로 정 
```

- 상속을 사용한 계층 구조 변경

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def talk(self):  # 메서드 재사용
        print(f'반갑습니다. {self.name}입니다.')


class Professor(Person):
    def __init__(self, name, age, department):
        self.name = name
        self.age = age
        self.department = department


class Student(Person):
    def __init__(self, name, age, gpa):
        self.name = name
        self.age = age
        self.gpa = gpa

```

```python
# 인스턴스 생성
p1 = Professor('박교수', 49, '컴퓨터공학과')
s1 = Student('김학생', 70, 3.5)
```



## Method Overriding

- 부모 클래스의 메서드를 같은 이름, 같은 파라미터 구조로 재정의

- 자식 클래스가 부모 클래스의 메서드를 덮어써서 새로운 동작 구현 가능

```python
class Animal:
    def eat(self):
        print('Animal이 먹는 중')

class Dog(Animal):
    # 오버라이딩 (부모 클래스 Animal의 eat 메서드를 재정의)
    def eat(self):
        print('Dog가 먹는 중')

my_dog = Dog()

my_dog.eat()  # Dog가 먹는 중
```

- Overloading
  
  - 같은 이름, 다른 파라미터 가진 여러 메서드 정의(파이썬 미지원)
  
  - 파이썬은 실제로 하나의 메서드만 인식, 인지의 형태가 다르다는 이유로 메서드를 여러 개 구분하여 불러주지 않음

```python
class Example:
    def do_something(self, x):
        print('첫 번째 do_something 메서드:', x)

    # 파이썬에서는 메서드가 "이름"이 같으면 앞선 정의를 덮어써버림
    def do_something(self, x, y):
        print('두 번째 do_something 메서드:', x, y)

example = Example()
# TypeError: do_something() missing 1 required positional argument: 'y'
example.do_something(10)
```



## Multiple Inheritance(다중 상속)

- 둘 이상의 상위 클래스로부터 여러 행동이나 특징 상속

- 상속받은 모든 클래스의 요소 활용 가능

- 중복된 속성이나 메서드가 있는 경우 **상속 순서에 의해 결정**  

```python
class Person:
    def __init__(self, name):
        self.name = name

    def greeting(self):
        return f'안녕, {self.name}'


class Mom(Person):
    gene = 'XX'

    def swim(self):
        return '엄마가 수영'


class Dad(Person):
    gene = 'XY'

    def walk(self):
        return '아빠가 걷기'
```

```python
class FirstChild(Dad, Mom):
    def swim(self):
        return '첫째가 수영'

    def cry(self):
        return '첫째가 응애'


baby1 = FirstChild('아가')
print(baby1.cry())  # 첫째가 응애
print(baby1.swim())  # 첫째가 수영
print(baby1.walk())  # 아빠가 걷기
print(baby1.gene)  # XY(아빠를 먼저 상속받았기 때문)
```

- 다이아몬드 문제

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-04-09-26-40-image.png)



- 파이썬의 해결책
  
  - MRO 알고리즘 사용하여 클래스 목록 생성
  
  - 부모 클래스로부터 상속된 속성들의 검색을 깊이 우선으로, 왼쪽에서 오른쪽으로, 계층 구조에서 겹치는 같은 클래스를 두 번 검색하지 않음
  
  - 그래서, 속성이 D에서 발견되지 않으면 B에서 찾고, 거기에서도 발견되지 않으면 C에서 찾고, 이런 식으로 진행
  
  

- MRO(Method Resolution Order)
  
  - 파이썬이 메서드를 찾는 순서에 대한 규칙
  
  - 메서드 결정 순서



## Super() Method

- super()
  
  - 부모 클래스(또는 상위 클래스)의 메서드를 호출하기 위해 사용하는 내장 함수
  
  - 다중 상속 상황에서 특히 유용, MRO를 따르기 때문에 여러 부모 클래스를 가진 자식 클래스에서 다음에 호출해야 할 부모 메서드를 순서대로 호출할 수 있게 함
  
  - 단일 상속 구조
    
    - 명시적으로 이름 지정하지 않고 부모 클래스 참조할 수 있으므로, 코드를 더 유지 관리하기 쉽게  만들 수 있음
    
    - 클래스 이름이 변경되거나 부모 클래스가 교체되어도 **super()** 를 사용하면 코드 수정이 더 적게 필요
    
    - Perosn 클래스를 직접 명시하지 않고 **super()** 를 사용하므로, 나중에 클래스 이름이 바뀌거나 상속 구조가 변경되어도 **super()** 호출 부분을 그대로 사용 가능해 유지보수성이 향상
  
  ```python
  class Person:
      def __init__(self, name, age, number, email):
          self.name = name
          self.age = age
          self.number = number
          self.email = email
  
  
  class Student(Person):
      def __init__(self, name, age, number, email, student_id):
          # super()를 통해 Person의 __init__ 메서드 호출
          super().__init__(name, age, number, email)
          self.student_id = student_id
  ```
  
  - 다중 상속 구조
    
    - MRO를 따른 메서드 호출
    
    - 복잡한 다중 상속 구조에서 발생할 수 있는 문제 방지
  
  ```python
  class ParentA:
      def __init__(self):
          super().__init__()
          self.value_a = 'ParentA'
  
      def show_value(self):
          print(f'Value from ParentA: {self.value_a}')
  
  
  class ParentB:
      def __init__(self):
          self.value_b = 'ParentB'
  
      def show_value(self):
          print(f'Value from ParentB: {self.value_b}')
  
  
  class Child(ParentA, ParentB):
      def __init__(self):
          super().__init__()  # ParentA 클래스의 __init__ 메서드 호출
          self.value_c = 'Child'
  
      def show_value(self):
          super().show_value()  # ParentA 클래스의 show_value 메서드 호출
          print(f'Value from Child: {self.value_c}')
  ```
  
  ```python
  child = Child()
  child.show_value()
  """
  Value from ParentA: ParentA
  Value from Child: Child
  """
  
  print(child.value_c)  # Child
  print(child.value_a)  # ParentA
  print(child.value_b)  # AttributeError: 'Child' object has no attribute 'value_b' ParentA
  ```
  
  ```python
  """
  <ParentA에 super().__init__()를 추가하면?>
  그 다음으로 ParentB의 __init__가 실행되어 value_b도 초기화할 수 있음
  그러면 print(child.value_b)는 ParentB를 출력하게 됨
  
  print(child.value_b)  # ParentB
  """
  
  """
  <Child 클래스의 MRO>
  Child -> ParentA -> ParentB
  
  super()는 단순히 “직계 부모 클래스를 가리킨다”가 아니라, 
  MRO 순서를 기반으로 “현재 클래스의 다음 순서” 클래스(또는 메서드)를 가리킴
  
  따라서 ParentA에서 super()를 부르면 MRO상 다음 클래스인 ParentB.__init__()가 호출됨
  """
  ```
  
  ```python
  """
  1.1 Child 클래스의 인스턴스를 생성할 때 일어나는 일
      1.	child = Child() 호출 시, Child.__init__()가 실행
      2.	Child.__init__() 내부에서 super().__init__()를 호출
          - 여기서 Child의 super()는 MRO에 의해 ParentA의 __init__()를 가리킴
      3.	ParentA.__init__()로 진입
  
  1.2. ParentA.__init__() 내부
  	1.	ParentA.__init__()에는 다시 super().__init__()가 있음
  	2.	ParentA를 기준으로 MRO에서 “다음 클래스”는 ParentB, 따라서 ParentA의 super().__init__()는 ParentB.__init__() 호출
      3.	ParentB.__init__()가 실행되면서 self.value_b = 'ParentB'가 설정됨
  	4.	ParentB.__init__()가 종료된 후, 다시 ParentA.__init__()로 돌아와 self.value_a = 'ParentA'가 설정됨
  	5.	ParentA.__init__() 종료 후, 다시 Child.__init__()로 돌아감
  	6.	마지막으로 Child.__init__() 내에서 self.value_c = 'Child'가 설정되고 종료
  
  1.3 결과적으로 child 인스턴스는 value_a, value_b, value_c 세 속성을 모두 갖게 됨
  	- child.value_a → 'ParentA'
  	- child.value_b → 'ParentB' 
  	- child.value_c → 'Child'
  """
  
  ```

- super()의 이점
  
  - 다중 상속 상황에서 super()는 다음에 호출해야 할 부모 메서드를  MRO 순서에 따라 결정하기 때문에, 명시적으로 특정 부모 클래스를 가리키지 않고도 올바른 순서로 부모 초기화나 메서드 호출이 가능
  
  - ClassName._____ __mro____ 또는 ClassName.mro() 를 확인해 MRO 순서를 파악한 뒤 적절히 활용하는 연습을 하면, 보다 복잡한 상속 구조에서도 코드 관리 가능   

```python
class A:
    def __init__(self):
        print('A Constructor')


class B(A):
    def __init__(self):
        super().__init__()
        print('B Constructor')


class C(A):
    def __init__(self):
        super().__init__()
        print('C Constructor')


class D(B, C):
    def __init__(self):
        super().__init__()
        print('D Constructor')
```

```python
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
print(D.mro())

# (<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
print(D.__mro__)
```



- MRO가 필요한 이유
  
  - 부모 클래스들이 여러 번 액세스 되지 않도록, 각 클래스에서 지정된 왼쪽에서 오른쪽으로 가는 순서를 보존, 각 부모를 오직 한 번만 호출하고, 부모들의 우선순위에 영향을 주지 않으면서 서브 클래스를 만드는 단조적 구조 형성



# 
