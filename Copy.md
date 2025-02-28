## Copy

- 객체와 참조
  
  - 가변(mutable) 객체
    
    - 생성 후 내용 변경 가능한 객체
    
    - list, dict, set
    
    - 객체 내용 변경되어도 같은 메모리 주소 유지
  
  ```python
  a = [1, 2, 3, 4]
  b = a
  b[0] = 100
  
  print(f'a의 값: {a}')  # [100, 2, 3, 4]
  print(f'b의 값: {b}')  # [100, 2, 3, 4]
  print(f'a와 b가 같은 객체를 참조하는가? {a is b}')  # True
  ```
  
  - 불변(immutable) 객체
    
    - 생성 후 내용 변경 불가능 객체
    
    - int(정수), float(실수), 문자열(str), 튜플(tuple)
    
    - 새로운 값 할당하면 새로운 객체 생성, 변수는 새 객체 참조
  
  ```python
  a = 20
  b = a
  b = 10
  
  print(f'a의 값: {a}')  # 20
  print(f'b의 값: {b}')  # 10
  print(a is b)  # False
  ```

- 변수 할당
  
  - 객체에 대한 참조 생성 과정
  
  - 변수는 객체의 메모리 주소 가리키는 label 역할 함
  
  - '=' 연산자 사용하여 변수에 값 할당
  
  - 할당 시 새로운 객체 생성되거나 기존 객체에 대한 참조 생성

- 메모리 참조 방식
  
  - 변수는 객체의 '메모리 주소' 저장
  
  - 여러 변수 동일한 객체 참조 가능

- id() 함수 사용한 메모리 주소 확인
  
  - id( ) 함수 사용하여 객체 메모리 주소 확인 가능
  
  - is 연산자 통해 두 변수가 같은 객체를 참조하는지 확인 가능
  
  ```python
  x = [1, 2, 3]
  y = x
  z = [1, 2, 3]
  
  print(f'x의 id: {id(x)}')  # 1644244407744
  print(f'y의 id: {id(y)}')  # 1644244407744
  print(f'z의 id: {id(z)}')  # 1644244776640
  print(f'x와 y는 같은 객체인가? {x is y}')  # True
  print(f'x와 z는 같은 객체인가? {x is z}')  # False
  ```

- **얕은 복사**
  
  - 객체의 최상위 요소만 새로운 메모리에 복사
  
  - 내부에 중첩된 객체 있다면 그 객체의 참조만 복사
  
  - 리스트 슬라이싱
  
  - copy() 메서드
  
  - list() 함수

```python
# 1차원 리스트
a = [1, 2, 3]
b = a[:]  # 슬라이싱
c = a.copy()  # copy() 메서드
d = list(a)  # list() 함수

b[0] = 100
c[0] = 999
d[0] = 8080
print(a)  # [1, 2, 3]
print(b)  # [100, 2, 3]
print(c)  # [999, 2, 3]
print(d)  # [8080, 2, 3]          # 얕은 복사로 충분히 독립적 본사본 만들 수 있
```

```python
# 다차원 리스트
print('\n다차원 리스트 얕은 복사의 한계')
a = [1, 2, [3, 4, 5]]
b = a[:]

b[0] = 999
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [999, 2, [3, 4, 5]]

b[2][1] = 100
print(a)  # [1, 2, [3, 100, 5]]
print(b)  # [999, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # True
```

-> 최상위 리스트만 복사되고, 내부 리스트는 여전히 원본과 같은 객체 참조

- **깊은 복사**
  
  - 객체 모든 수준의 요소를 새로운 메모리에 복사
  
  - 중첩된 객체까지 모두 새로운 객체로 생성
  
  - copy 모듈에서 제공하는 **deepcopy()** 함수 사용

```python
import copy

new_object = copy.deepcopy(original_object)
```

```python
a = [1, 2, [3, 4, 5]]
b = copy.deepcopy(a)

b[2][1] = 100
print(a)  # [1, 2, [3, 4, 5]]
print(b)  # [1, 2, [3, 100, 5]]
print(f'a[2]와 b[2]가 같은 객체인가? {a[2] is b[2]}')  # False
```

```python
original = {
    'a': [1, 2, 3],
    'b': {
        'c': 4,
        'd': [5, 6],
    },
}
copied = copy.deepcopy(original)

copied['a'][1] = 100
copied['b']['d'][0] = 500

print(f'원본: {original}')  # {'a': [1, 2, 3], 'b': {'c': 4, 'd': [5, 6]}}
print(f'복사본: {copied}')  # {'a': [1, 100, 3], 'b': {'c': 4, 'd': [500, 6]}}
print(
    f'original["b"]와 copied["b"]가 같은 객체인가? {original["b"] is copied["b"]}'
)  # False
```

- 메서드 체이닝
  
  - 여러 메서드를 연속해서 호출
  
  ```python
  text = 'heLLo, woRld!'
  new_text = text.swapcase().replace('l', 'z')
  print(new_text)  # HEzzO, WOrLD!             # 문자열
  ```

```python
# 1. 단계별로 실행하기
text = 'heLLo, woRld!'
step1 = text.swapcase()
print('1단계 결과:', step1)  # HEllO, WOrLD!

step2 = step1.replace('l', 'z')
print('2단계 결과:', step2)  # HEzzO, WOrLD!

# 2. 한 줄로 실행하기 (위와 동일한 결과)
new_text = text.swapcase().replace('l', 'z')
print('최종 결과:', new_text)  # HEzzO, WOrLD!
```

    # 잘못된 체이닝 방식 1
    numbers = [3, 1, 4, 1, 5, 9, 2]
    result = numbers.copy().sort()
    print(result)  # None (sort()는 None을 반환하므로 체이닝이 중단됨)
    print(numbers)  # [3, 1, 4, 1, 5, 9, 2] (원본은 변경되지 않음)     # 리스트
    
    # 올바른 체이닝 예
    sorted_numbers = sorted(numbers.copy())
    print(sorted_numbers)  # [1, 1, 2, 3, 4, 5, 9]

- 메서드 체이닝 주의사항
  
  - 모든 메서드가 체이닝 지원 x
    
    -  메서드가 객체 반환할때만 체이닝 가능
  
  -  None 반환하는 메서드는 메서드 체이닝 불가능
    
    -  append(), sort()



- 문자 유형 판별 메서드
  
  - isdecimal( )
    
    - 문자열이 모두 숫자 문자(0~9)로만 이루어져 있어야 True
  
  - isdigit( )
    
    - isdecimal()과 비슷하지만, 유니코드 숫자도 인식
  
  - isnumeric( )
    
    - isdigit()과 유사하지만, 몇 가지 추가적인 유니코드 문자들 인식
    
    - 분수, 지수, 루트 기호도 숫자로 인식
