## Nonsequence data structure

- **Dictionary**
  
  - 고유한 항목들의 정렬되지 않은 컬렉션
  
  - D.clear()
    
    - 딕셔너리 D의 모든 키/값 쌍을 제거
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  person.clear()
  print(person) # {}
  ```
  
  - **D.get(k)**
    
    - 키 k에 연결된 값 반환(키가 없으면 None 반환)
  
  - **D.get(k, v)**
    
    - 키 k에 연결된 값 반환하거나 키가 없으면 기본 값으로 v 반환
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.get('name')) # Alice
  print(person.get('country')) # None
  print(person.get('country', 'Unknown')) # Unknown
  print(person['country'])  # KeyError: 'country'
  ```
  
  - **D.keys()**
    
    - 딕셔너리 D의 키를 모은 객체 반환
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.keys())  # dict_keys(['name', 'age'])
  for item in person.keys():
      print(item)
  """
  name
  age
  """
  ```
  
  - **D.values()**
    
    - 딕셔너리 D의 값을 모은 객체 반환
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.values())  # dict_values(['Alice', 25])
  for item in person.values():
      print(item)
  """
  Alice
  25
  """
  ```
  
  - **D.items()**
    
    - 딕셔너리 D의 키/값 쌍을 모은 객체 반환
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.items())  # dict_items([('name', 'Alice'), ('age', 25)])
  for key, value in person.items():
      print(key, value)
  """
  name Alice
  age 25
  """
  ```
  
  - **D.pop(k)**
    
    - 딕셔너리 D에서 키 k를 제거하고 연결됐던 값 반환(없으면 오류)
  
  - **D.pop(k, v)**
    
    - 딕셔너리 D에서 키 k를 제거하고 연결됐던 값 반환(없으면 v 반환)
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.pop('age'))  # 25
  print(person)  # {'name': 'Alice'}
  print(person.pop('country', None))  # None
  print(person.pop('country'))  # KeyError
  ```
  
  - D.setdefault(k)
    
    - 딕셔너리 D에서 키 k와 연겨된 값 반환
  
  - D.setdefault(k, v)
    
    - 딕셔너리 D에서 키 k와 연결된  값 반환
    
    - k가 D의 키가 아니면 값 v와 연결된 키 k를 D에 추가하고 v 반환
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  print(person.setdefault('country', 'KOREA'))  # KOREA
  print(person)  # {'name': 'Alice', 'age': 25, 'country': 'KOREA'}
  ```
  
  - D.update(other)
    
    - other 내 각 키에 대해 D에 있는 키면 D에 있는 그 키의 값을 other에 있는 값으로 대체.
    
    - other에 있는 각 키에 대해 D에 없는 키면 키/값 쌍을 D에 추가
  
  ```python
  person = {'name': 'Alice', 'age': 25}
  other_person = {'name': 'Jane', 'country': 'KOREA'}
  
  person.update(other_person)
  print(person)  # {'name': 'Jane', 'age': 25, 'country': 'KOREA'}
  
  person.update(age=100, address='SEOUL')
  print(person)  # {'name': 'Jane', 'age': 100, 'country': 'KOREA', 'address': 'SEOUL'}
  ```

- **Set**
  
  - 고유한 항목들의 정렬되지 않은 컬렉션
  
  - **s.add(x)**
    
    - 세트 s에 항목 x를 추가. 이미 x가 있다면 변화 없음
  
  ```python
  my_set = {'a', 'b', 'c', 1, 2, 3}
  my_set.add(4)
  print(my_set) # {1, 'b', 3, 2, 'c', 'd', 'a'}
  
  my_set.add(4)
  print(my_set) # {1, 'b' 3, 2, 'c', 'd', 'a'}
  ```
  
  - s.clear()
    
    - 세트 s의 모든 항목 제거
  
  ```python
  my_set = {'a', 'b', 'c', 1, 2, 3}
  my_set.clear()
  print(my_set)  # set()
  ```
  
  - **s.remove(x)**
    
    - 세트 s에서 항목 x를 제거. 항목 x가 없을 경우 Keyerror
  
  ```python
  my_set = {'a', 'b', 'c', 1, 2, 3}
  my_set.remove(2)
  print(my_set) # {'b', 1, 3, 'c', 'a'}
  
  my_set.remove(10) 
  print(my_set)  # KeyError: 10
  ```

```
- s.pop()

  - 세트 s에서 **임의의** 항목 **반환**하고 해당 항목 제거

```python
my_set = {'a', 'b', 'c', 1, 2, 3}
element = my_set.pop()
print(element) # 1
print(my_set) # {2, 3, 'b', 'a', 'c'}
```

- s.discard(x)
  
  - 세트 s에서 항목 x 제거
  
  ```python
  my_set = {'a', 'b', 'c', 1, 2, 3}
  my_set.discard(2)
  print(my_set) # {1, 3, 'a', 'c', 'b'}
  my_set.discard(10)
  print(my_set) # {1, 3, 'a', 'c', 'b', 2}
  ```

- s.update(iterable)
  
  - 세트 s에 다른 iterable 요소 추가
  
  ```python
  my_set = {'a', 'b', 'c', 1, 2, 3}
  my_set.update([1, 4, 5])
  print(my_set)  # {'c', 2, 3, 1, 'b', 4, 5, 'a'}
  ```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-03-17-22-57-image.png)

```python
set1 = {0, 1, 2, 3, 4}
set2 = {1, 3, 5, 7, 9}
set3 = {0, 1}

print(set1.difference(set2))  # {0, 2, 4}
print(set1.intersection(set2))  # {1, 3}
print(set1.issubset(set2))  # False
print(set3.issubset(set1))  # True
print(set1.issuperset(set2))  # False
print(set1.union(set2))  # {0, 1, 2, 3, 4, 5, 7, 9}
```

## Hash Table

- 해시 함수를 사용하여 변환한 값을 인덱스로 삼아 키(key)와 데이터(value)를 저장하는 자료구조

- 데이터를 빠르게 저장하고 검색하기 위해 사용

- 1. 키를 해시 함수를 통해 해시 값으로 변환
  
  2. 변환된 해시 값을 인덱스로 삼아 데이터를 저장하거나 찾음
  
  3. 이로 인해 검색, 삽입, 삭제가 매우 빠르게 수행

- hash(해시) 
  
  - 임의의 크기를 가진 데이터를 고정된 크기의 고유한 값으로 변환
  
  - 생성된 해시 값(고유한 정수)은 해당 데이터를 식별하는 '지문' 역할
  
  - 해시 값을 이용해 해시 테이블에 데이터 저장

- hash function(해시 함수)
  
  - 임의 길이 데이터 입력 받아 고정 길이(정수)로 변환해 주는 함수
  - 매우 빠른 검색 위해 활용
  - '해시 알고리즘'

- set의 요소&dict의 키와 해시테이블 관계
  
  - set
    
    - 각 요소를 해시 함수로 변환해 나온 해시 값에 맞춰 해시 테이블 내부 버킷에 위치
    
    - "버킷 위치(인덱스)"가 요소 위치 결정
    
    - set는 순서 보장 x
  
  - dict
    
    - 키 -> 해시 함수 -> 해시 값 -> 해시 테이블 저장
    
    - set와 달리 "삽입 순서"는 유지한다는 것이 언어 사양으로 보장
      
      - 키를 추가한 순서대로 반복문 순회할 때 나오게 됨
      
      - 사용자에게 보여지는 키 순서는 삽입 순서가 유지되도록 설계

- set의 pop 메서드 정수 예시

```python
my_set = {3, 2, 1, 9, 100, 4, 87, 39, 10, 52}
print(my_set.pop()) # 1
print(my_set.pop()) # 2
print(my_set.pop()) # 3
print(my_set.pop()) # 100
print(my_set.pop()) # 4
print(my_set.pop()) # 39
print(my_set.pop()) # 9
print(my_set.pop()) # 10
print(my_set.pop()) # 52
print(my_set.pop()) # 87
print(my_set) # set()
```

- set의 pop 메서드 문자열 예시

```python
my_str_set = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'}
print(my_str_set.pop()) # a
print(my_str_set.pop()) # f
print(my_str_set.pop()) # h
print(my_str_set.pop()) # e
print(my_str_set.pop()) # d
```

- 파이썬에서의 해시 함수
  
  - 정수
    
    - 같은 정수는 항상 같은 해시 값
    
    - hash(1)은 여러 번 호출해도 결과 동일
  
  - 문자열
    
    - 문자열 해시 시, 파이썬 인터프리터 시작 때 설정되는 난수 시드(seed)가 달라질 수 있음
    
    - 보안상 이유로 난수화 도입
    
    - 각 실행마다 달라질 수 있어 'a'의 해시 값도 매번 바뀔 수 있음
  
  ```python
  print(hash(1)) # 1
  print(hash(1)) # 1
  print(hash('a'))  # 실행 시마다 다름
  print(hash('a'))  # 실행 시마다 다름
  ```
* 해시 난수화와 난수 시드
  
  * 파이썬프로세스가 새로 시작될 때마다 해시를 계산할 때 사용하는 난수 시드가 달라짐
    
    * 해시 계산에 쓰이는 시드 값이 실행마다 달라지는 것
  
  * 동일한 데이터라도 매번 해시 값이 달라져 결과적으로 버킷 배치 달라짐

## Hashable

- hashable
  
  - hash() 함수에 넣어 해시 값을 구할 수 있는 객체
  
  - 대부분 불변 타입 해시 가능
    
    - int, float, str, tuple
  
  - 가변형 객체(list, dict, set)는 기본적으로 해시 불가능
    
    - 값이 변하면 해시 값도 달라질 수 있어 해시 테이블 무결성 깨짐
  
  ```python
  print(hash(1))
  print(hash(1.0))
  print(hash('1'))
  print(hash((1, 2, 3)))
  
  # TypeError: unhashable type: 'list'
  print(hash((1, 2, [3, 4])))
  ```

- hashable과 불변성 간의 관계
  
  - 해시 테이블(ex) set,dict의 키)에는 해시 가능한 객체만 저장 가능
  
  - 불변 객체는 생성 후 값 변경이 불가능하므로, 항상 가튼 해시 값을 유지
  
  - 다만, **"hash 가능하다 ! = 불변이다"** 가 절대적이진 않지만 일반적으로 내장 자료형 기준 불변이어야 해시 가능

- 가변형 객체가 hashable 하지 않은 이유
  
  - 값이 변경될 수 있으므로, 같은 객체라도 값이 바뀌면 해시 값도 변경 가능
  
  - 해시 테이블에서는 "동일 키 -> 동일 위치" 로 가정하고 빠른 검색 수행하는데, 이 가정이 깨짐
  
  - ex) 리스트, 집합, 딕셔너리 자체를 set이나 dict의 키로 쓸 수 없음

```python
# TypeError: unhashable type: 'list'
print(hash([1, 2, 3]))
# TypeError: unhashable type: 'list'
my_set = {[1, 2, 3], 1, 2, 3, 4, 5}
# TypeError: unhashable type: 'set'
my_dict = {{3, 2}: 'a'}
```

- hashable 객체 필요 이유
  
  - 해시 테이블 기반 자료 구조 사용
  
  - 불변성 통한 일관된 해시 값
  
  - 안정성과 예측 가능성 유지
