## Nonsequence Types

- **dict(딕셔너리)**
  
  - **key - value** 쌍으로 이루어진 **순서와 중복이 없는** **변경 가능한** 자료형 
    
    -> **index** 접근 불가
  
  - key
    
    - 변경 불가능한 자료형만 사용가능(str, int, float, tuple, range ...)
  
  - value
    
    - 모든 자료형 사용 가능
  
  - 중괄호(**{}**)로 표기
  
  - key를 통해 value에 접근

```bash
# 딕셔너리 표현
my_dict_1 = {}
my_dict_2 = {'key' : 'value'}
my_dict_3 = {'apple' : 12, 'list' : [1,2,3]}
print(my_dict_1)  # {}
print(my_dict_2)  # {'key' : 'value'}
print(my_dict_3)  # {'apple':12, 'list' : [1,2,3]}
```

```bash
my_dict = {'apple': 12, 'list': [1, 2, 3]}

print(my_dict['apple']) # 12
print(my_dict['list']) # [1, 2, 3]
print(my_dict['list'][1]) # 2

# 추가
my_dict['banana'] = 50
print(my_dict)  # {'apple': 12, 'list': [1, 2, 3], 'banana': 50}

# 변경
my_dict['apple'] = 100
print(my_dict)  # {'apple': 100, 'list': [1, 2, 3], 'banana': 50}
```

- **set**
  
  - **순서와 중복이 없는 변경 가능한** 자료형 -> **index** 접근 불가
  
  - 집합 자료형
  
  - 수학에서의 집합과 동일한 연산 처리 가능
  
  - 중괄호(**{}**)로 표기 -> **dict**와 겹치지 않기 위해 **set()** 로 표시 

```bash
my_set_1 = set()
my_set_2 = {1, 2, 3}
my_set_3 = {1, 1, 1}
print(my_set_1)  # set()
print(my_set_2)  # {1, 2, 3}
print(my_set_3)  # {1}
```

```bash
# 세트의 집합 연산산
my_set_1 = {1, 2, 3}
my_set_2 = {3, 6, 9}

# 합집합
print(my_set_1 | my_set_2)  # {1, 2, 3, 6, 9}

# 차집합
print(my_set_1 - my_set_2)  # {1, 2}

# 교집합
print(my_set_1 & my_set_2)  # {3}
```


