## Functions

- **함수**
  
  - 특정 작업을 수행하기 위한 재사용 가능한 코드 묶음
  
  - 두 수의 합을 구하는 함수를 정의하고 사용함으로써 코드 중복 방지
  
  - **재사용성**이 높아지고, 코드의 **가독성과 유지보수성** 향상

```python
# 두 수의 합을 구하는 코드
num1 = 5
num2 = 3
sum_result = num1 + num2
print(sum_result)
```

```python
# 두 수의 합을 구하는 함수
def get_sum(num1, num2):
    return num1 + num2

# 함수를 호출하여 결과 출력
num1 = 5
num2 = 3
sum_result = get_sum(num1, num2)
print(sum_result)
```

- **함수 호출**
  
  - 함수를 실행하기 위해 함수의 이름을 사용하여 해당 함수의 코드 블록 실행

```python
function_name(arguments)
```

- **함수 구조**
  
  - pram : parameter
  
  - "" ~ "" : docstring
  
  - "" ~ 끝 : function body
  
  - return ~ : return value(반환값)

```python
def make_sum(pram1, pram2):
    """이것은 두 수를 받아
    두 수의 합을 반환하는 함수입니다.
    >>> make_sum(1, 2)
    3
    """
    return pram1 + pram2 

# 함수 호
result = make_sum(100, 30)
print(result) # 130
```

- **함수 정의와 호출**
  
  - 함수 정의
    
    - **def** 키워드로 시작
    
    - **def** 키워드 이후 함수 이름 작성
    
    - 괄호안에 매개변수 정의
    
    - 매개변수(parameter)는 함수에 전달되는 값 나타냄
  
  - 함수 body
    
    - 콜론(:) :다음에 들여쓰기 된 코드 블록
    
    - 함수가 실행될 때 수행되는 코드
  
  - docstring
    
    - 함수 body 앞에 선택적으로 작성 가능한 함수 설명서
  
  - 함수 반환 값
    
    - 함수는 필요한 경우 결과 반환 가능
    
    - **return** 키워드 이후 반환값 명시
    
    - **return** 문은 함수의 실행을 종료하고, 결과를 호출 부분으로 반환
    
    - 함수 내에서 **return**문이 없다면 **None**이 반환됨

- **함수와 반환 값**
  
  - print() 함수는 반환 값이 없다
    
    - **print()** 함수는 화면에 값을 출력하기만 할 뿐, 반환(**return**) 값이 없음
    
    - 파이썬에서 반환 값이 없는 함수는 기본적으로 **None**을 반환한다고 간주되기 때문
    
    - 출력을 담당하는 함수는 결과를 반환(**return**) 하지 않으므로, 내부적으로 아무 값도 반환하지 않는 함수와 마찬가지로 **None**이 나옴

```python
# print() 함수는 반환값이 없다.
return_value = print(1)
print(return_value) # None
```

```python
def my_func():
   print('hello')

result = my_func
print(result) # None
```

-  **매개 변수와 인자**
  
  - 매개변수(parameter)
    
    - 함수를 **정의할 때**, 함수가 받을 값을 나타내는 변수
  
  - 인자(argument)
    
    - 함수를 **호출할 때**, 실제로 전달되는 값

```python
def add_numvers(x, y): # x와 y는 매개변수(parameter)
    result = x + y
    return result

a = 2
b = 3
sum_result = add_numvers(a, b)
print(sum_result)
```

- **positional arguments(위치 인자)**
  
  - 함수 호출 시 인자의 위치에 따라 전달되는 인자
  
  - **위치인자는 함수 호출 시 반드시 값을 전달해야 함**

```python
# 1. Positional Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Alice', 25)  # 안녕하세요, Alice님! 25살이시군요.
greet(25, 'Alice')  # 안녕하세요, 25님! Alice살이시군요.
greet('Alice')  # TypeError: greet() missing 1 required positional argument: 'age'
```

- **default argument values(기본 인자 값)**
  
  - 함수 정의에서 매개변수에 기본 값을 할당
  
  - 함수 호출 시 인자를 전달하지 않으면, 기본값이 매개변수에 할당됨

```python
# 2. Default Argument Values
def greet(name, age=20):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet('Bob')  # 안녕하세요, Bob님! 30살이시군요.
greet('Charlie', 40)  # 안녕하세요, Charlie님! 40살이시군요.
```

- **keyword arguments(키워드 인자)**
  
  - 함수 호출 시 인자의 이름과 함께 값을 전달하는 인자
  
  - 매개변수와 인자를 일치시키지 않고, 특정 매개변수에 값을 할당 가능
  
  - 인자의 순서는 중요x, 인자의 이름을 명시하여 전달
  
  - **단, 호출 시 키워드 인자는 위치 인자 뒤에 위치해야 함**

```python
# 3. Keyword Arguments
def greet(name, age):
    print(f'안녕하세요, {name}님! {age}살이시군요.')


greet(name='Dave', age=35)  # 안녕하세요, Dave님! 35살이시군요.
greet(age=35, name='Dave')  # 안녕하세요, Dave님! 35살이시군요.
```

```python
greet(age=35, 'Dave')  # Positional argument cannot appear after keyword arguments
```

- **arbitrary argument lists(임의의 인자 목록)**
  
  - 정해지지않은 개수의 인자 처리하는 인자
  
  - 함수 정의 시 매개변수 앞에 **' * '** 를 붙여 사용
  
  - 여러 개의 인자를 tuple로 처리

```python
# 4. Arbitrary Argument Lists
def calculate_sum(*args):
    print(args)  # (1, 100, 5000, 30)
    print(type(args))  # <class 'tuple'>


calculate_sum(1, 100, 5000, 30)
```

- **aribitrary keyword argument lists(임의의 키워드 인자 목록)**
  
  - 정해지지 않은 개수의 키워드 인자 처리 인자
  
  - 함수 정의 시 매개변수 앞에 **' ** '** 를 붙여 사용
  
  - 여러 개의 인자를 dict로 묶어 처리 

```python
# 5. Arbitrary Keyword Argument Lists
def print_info(**kwargs):
    print(kwargs)


print_info(name='Eve', age=30)  # {'name': 'Eve', 'age': 30 }
```

- 함수 인자 권장 작성순서
  
  - 위치 -> 기본 -> 가변 -> 가변 키워드
  
  - 호출 시 인자 전달 과정에서 혼란 줄일 수 있도록 함
  
  - 단, 모든 상황에 적용되는 절대적 규칙은 아니며, 상황에 따라 유연하게 조정 가능

```python
def func(pos1, pos2, default_arg='default', *args, **kwargs):
```

```python
# 인자의 모든 종류를 적용한 예시
def func(pos1, pos2, default_arg='default', *args, **kwargs):
    print('pos1:', pos1)
    print('pos2:', pos2)
    print('default_arg:', default_arg)
    print('args:', args)
    print('kwargs:', kwargs)


func(1, 2, 3, 4, 5, 6, key1='value1', key2='value2')
```

```python
"""
pos1: 1
pos2: 2
default_arg: 3
args: (4, 5, 6)
kwargs: {'key1': 'value1', 'key2': 'value2'}
"""
```


