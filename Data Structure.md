## Data Structure

- 여러 데이터를 효과적으로 사용,관리하기 위한 구조
  
  - str, list, dict ...
  
  - 문자열, 리스트, 딕셔너리 등 각 데이터 구조의 **메서드**를 호출하여 다양한 기능 활용

- **Method**
  
  - 객체에 속한 함수
  
  - 객체의 상태 조작하거나 동작 수행
  
  - 클래스 내부에 정의되는 함수
  
  - 클래스는 파이썬에서 '타입을 표현하는 방법'이며 은연중에 사용해왔음
  
  - help 함수 통해 str 호출해보면 class 였다는 것 확인 가능
  
  - **'데이터 타입 객체'.메서드()**
  
  ```python
  # 문자열 메서드 예시 
  'hello'.capitalize()
  ```

```python
# 리스트 메서드 예시
numbers = [1, 2, 3]
numbers.append(4)

print(numbers) # [1, 2, 3, 4]
```

- Sequence Data Structure
  
  - 문자열
    
    - s.find(x)
      
      - x의 첫 번째 위치 반환. 없으면, -1 반환
    
    ```python
    text = 'banana'
    print(text.find('a'))  # 1
    print(text.find('z'))  # -1
    ```
    
    - s.index(x)
      
      - x의 첫 번째 위치 반환. 없으면 오류 발생
    
    ```python
    print(banana.index('a'))  # 1
    print(banana.index('z'))  # ValueError: substring not found
    ```
    
    - s.isupper()
      
      - 문자열 내의 모든 문자가 대문자인지 확인
    
    - s.islower()
      
      - 문자열 내의 모든 문자가 소문자인지 확인
    
    ```python
    # isupper
    string1 = 'HELLO'
    string2 = 'Hello'
    print(string1.isupper())  # True
    print(string2.isupper())  # False
    
    # islower
    print(string1.islower())  # False
    print(string2.islower())  # False
    ```
    
    - s.isalpha()
      
      - 문자열 내의 모든 문자가 알파벳인지 확인
      
      - 단순 알파벳이 아닌 유니코드 상 Letter(한국어 포함)
    
    ```python
    # isalpha
    string1 = 'Hello'
    string2 = '123heis98576ssh'
    print(string1.isalpha())  # True
    print(string2.isalpha())  # False
    ```

- 문자열 조작 메서드
  
  - **s.replace(old, new[,count])**
    
    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
  
  ```python
  text = 'Hello, world! world world'
  new_text1 = text.replace('world', 'Python')
  new_text2 = text.replace('world', 'Python', 1)
  print(new_text1)  # Hello, Python! Python Python
  print(new_text2)  # Hello, Python! world world
  ```
  
  - **s.strip([chars])**
    
    - 공백이나 특정 문자 제거
  
  ```python
  text = '  Hello, world!  '
  new_text = text.strip()
  print(new_text)  # Hello, world!
  ```
  
  - **s.split(sep=None, maxsplit=-1)**
    
    - sep를 구분자 문자열로 사용하여 문자열에 있는 단어들의 리스트 반환
  
  ```python
  text = 'Hello, world!'
  words1 = text.split(',')
  words2 = text.split()
  print(words1)  # ['Hello', ' world!']
  print(words2)  # ['Hello,', 'world!']
  ```
  
  - **'separator'.join(iterable)**
    
    - 구분자로 iterable의 문자열 연결한 문자열 반환
  
  ```python
  words = ['Hello', 'world!']
  new_text = '-'.join(words)
  print(new_text)  # Hello-world!
  ```
  
  - s.caplitalize()
    
    - 가장 첫 번째 글자 대문자로 변경
  
  - s.title()
    
    - 문자열 내 띄어쓰기 기준으로 각 단어의 첫 글자는 대문자로, 나머지는 소문자로 변환
  
  - s.upper()
    
    - 모두 대문자로 변경
  
  - s.lower()
    
    - 모두  소문자로 변경
  
  - s.swapcase()
    
    - 대 <-> 소문자로 서로 변경
  
  ```python
  # capitalize
  text = 'heLLo, woRld!'
  new_text1 = text.capitalize()
  print(new_text1)  # Hello, world!
  
  # title
  new_text2 = text.title()
  print(new_text2)  # Hello, World!
  
  # upper
  new_text3 = text.upper()
  print(new_text3)  # HELLO, WORLD!
  
  # lower
  new_text4 = text.lower()
  print(new_text4)  # hello, world!
  
  # swapcase
  new_text5 = text.swapcase()
  print(new_text5)  # HEllO, WOrLD!
  ```

- **List**
  
  - **L.append(x)**
    
    - 리스트 마지막에 항목 x를 추가
  
  ```python
  my_list = [1, 2, 3]
  my_list.append(4)
  print(my_list)  # [1, 2, 3, 4]
  ```
  
  - **L.extend(m)**
    
    - iterable m의 모든 항목들을 리스트 끝에 추가(+=과 같은 기능)
  
  ```python
  my_list = [1, 2, 3]
  my_list.extend([4, 5, 6])
  print(my_list)  # [1, 2, 3, 4, 5, 6] 
  
  # append와의 비교
  my_list.append([4, 5, 6])
  print(my_list)  # [1, 2, 3, 4, 5, 6, [4, 5, 6]]
  
  # 반복 가능한 객체가 아니면 추가 불가
  my_list.extend(100)
  # TypeError: 'int' object is not iterable
  ```
  
  - L.insert(i, x)
    
    - 리스트 인덱스 i에 항목 x를 삽입
  
  ```python
  my_list = [1, 2, 3]
  my_list.insert(1, 5)
  print(my_list)  # [1, 5, 2, 3]
  ```
  
  - L.remove(x)
    
    - 리스트 가장 왼쪽에 있는 항목(첫 번째)  x를 제거
    
    - 항목이 존재하지 않을 경우,  ValueError
  
  ```python
  my_list = [1, 2, 3, 2, 2, 2]
  my_list.remove(2)
  print(my_list)  # [1, 3, 2, 2, 2]
  ```
  
  - **L.pop()**
    
    - 리스트 가장 오른쪽에 있는 항목(마지막)을 반환 후 제거
  
  - **L.pop(i)**
    
    - 리스트의 인덱스 i에 있는 항목 반환 후 제거
  
  ```python
  my_list = [1, 2, 3, 4, 5]
  item1 = my_list.pop()
  item2 = my_list.pop(0)
  
  print(item1)  # 5
  print(item2)  # 1
  print(my_list)  # [2, 3, 4]
  ```
  
  - L.clear()
    
    - 리스트 모든 항목 삭제
  
  ```python
  my_list = [1, 2, 3]
  my_list.clear()
  print(my_list)  # []
  ```

- L.index(x)
  
  - 리스트에서 첫 번째로 일치하는 항목 x의 인덱스 반환

```python
my_list = [1, 2, 3]
index = my_list.index(2)
print(index)  # 1
```

- L.count(x)
  
  - 리스트에서 항목  x의 개수 반환

```python
my_list = [1, 2, 2, 3, 3, 3]
counting_number = my_list.count(3)
print(counting_number)  # 3
```

- **L.reverse()**
  
  - 리스트의 순서를 역순으로 변경(정렬x)

```python
my_list = [1, 3, 2, 8, 1, 9]
my_list.reverse()
print(my_list.reverse())  # None
print(my_list)  # [9, 1, 8, 2, 3, 1]
```

- **L.sort()**
  
  - 리스트 정렬(매개변수 이용가능)

```python
my_list = [3, 2, 100, 1]
my_list.sort()
print(my_list)  # [1, 2, 3, 100]

# sort(내림차순 정렬)
my_list.sort(reverse=True)
print(my_list)  # [100, 3, 2, 1]
```
