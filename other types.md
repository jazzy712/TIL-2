## Other Types

- **None**
  
  - 파이썬에서 '값이 없음'을 표현하는 자료형

```python
# None
variable = None
print(variable)  # None
```

- **Boolean**
  
  - 참(True) 과 거짓(False)을 표현하는 자료형
  
       -> 조건/반복문
  
  - 비교/논리 연산의 평가 결과로 사용

```python
# Boolean
bool_1 = True
bool_2 = False

print(bool_1)  # True
print(bool_2)  # False
print(3 > 1)  # True
print('3' != 3)  # True
```

  != -> '같지 않다''



- **Collection**
  
  - 여러 개의 항목 또는 요소를 담는 자료 구조
  
  - str, list, tuple. dict. set
  
  - 순서 여부 : 시퀀스 o/x



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-10-31-55-image.png)

```python
# immutable (불변)
my_str = 'hello'
my_str[0] = 'z'  # TypeError: 'str' object does not support item assignment

# mutable (가변)
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list)  # [100, 2, 3]
```



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-01-21-10-32-26-image.png)
