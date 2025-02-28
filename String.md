## String(문자열)

- 유니코드

```python
print(f'{ord("대"):x}') 
print(chr(0xb300))  
```

```python
s1 = list(input())
s2 = input() 
```

-> 차이 알기 !

- python에서의 문자열 처리
  
  - char 타입 없음
  
  - 텍스트 데이터의 취급방법 통일
  
  - 문자열 기호
    
    - '(홑따옴표), "(쌍따옴표), '''(홑따옴표 3개), """(쌍따옴표 3개)
    
    - +(연결)
      
      - 문자열 + 문자열 : 이어 붙여주는 역할
    
    - *(반복)
      
      - 문자열 * 수: 수만큼 문자열 반복
  
  - 문자열은 시퀀스 자료형으로 분류, 시퀀스 자료형에서 사용할 수 있는 인덱싱, 슬라이싱 연산 사용 가능
  
  ```python
  replace(), split(), isalpha(), find()
  ```
  
  - 문자열은 튜플과 같이 요소값 변경 불가능

- 문자열 뒤집기
  
  ```python
   txt = list(input())
   N = len(txt)
   for i in range(N//2):
        txt[i], txt[N-1-i] = txt[N-1-i], txt[i]
   print(txt) 
  ```

```python
s = 'string'
s = s[::-1]
print(s, type(s))                 # gnirts <class 'str'>
s_list = list(s)
s_list.reverse()
print(s_list)                     # ['s', 't', 'r', 'i', 'n', 'g']
print(''.join(s_list))            # string
```

- 문자열 비교
  
  - c strcmp() 함수 제공
  
  - 파이썬에서는 ==연산자와 is 연산자 제공
    
    - ==연산자는 내부적으로 특수 메서드 _____eq______() 호출
  
      s1 = 'abc'
      s2 = 'ab'
      s3 = 'def'
      s4 = s2 + 'c'
      print(s1, s4)                     # abc, abc
      print(s1 == s4)                   # True(같은 모양인가?)
      print(s1 is s4)                   # False(같은 메모리 위치인
      print(s1 is 'abc')                # True


