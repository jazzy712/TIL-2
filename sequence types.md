## Sequence Types



- 여러 개의 값들을 **순서대로 나열**(정렬 x)

- str(문자열)
  
  - 문자들의 순서가 있는 **변경 불가능**한 자료형

- f-string

- index
  
  - slicing

- list
  
  - **여러 개의 값을 순서대로 저장**하는 **변경 가능한** 자료형
  
  - 0개 이상의 객체 포함하며 데이터 목록 저장
  
  - 대괄호([])로 표기
  
  - 데이터는 어떤 자료형도 저장 가능
  
  - 시퀀스 특징
  
  - list 변경은 재할당이 아님
    
    - 기존 요소의 주소가 바뀔 뿐 list의 주소는 바뀌지 않는다
  
  - 

```bash
my_list_1 = []
my_list_2 = [1, 'a', 3, 'b', 5]
my_list_3 = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
```

```bash
# 인덱싱
print(my_list[1]) # a

# 슬라이싱
print(my_list[2:4])  # [3, 'b']
print(my_list[:3])  # [1, 'a', 3]
print(my_list[3:])  # ['b', 5]
print(my_list[0:5:2])  # [1, 3, 5]
print(my_list[::-1])  # [5, 'b', 3, 'a', 1]

# 길이
print(len(my_list))  # 5
```

```bash
# 중첩된 리스트 접근
my_list = [1, 2, 3, 'Python', ['hello', 'world', '!!!']]
print(len(my_list))  # 5
print(my_list[4][2])  # !!!
print(my_list[4][-1])  # !!!
print(my_list[4][1][0])  # w
print(my_list[-1][1][0])  # w

# 리스트는 가변
my_list = [1, 2, 3]
my_list[0] = 100
print(my_list) # [100, 2, 3]

my_list_test = [1, 'world', 3]
my_list_test[1] = 100
print(my_list_test) # [1, 100, 3]

```



- tuple
  
  - 여러 개의 값을 순서대로 저장하는 **변경 불가능한** 시퀀스 자료형
  
  - 0개 이상의 객체 포함하며 데이터 목록 저장
  
  - 소괄호(())로 표기
  
  - 데이터는 어떤 자료형도 저장 가능
  
  - 단일 요소 튜플을 만들 때는 반드시 Trailing comma(후행 쉼표)를 사용해야 함
  
  - (1) -> int, (1,) -> tuple
  
  - 튜플의 **불변 특성**을 사용하여 **내부 동작**과 안전한 데이터 전달에 사용
  
           -> 다중할당, 값 교환, 그룹화, 함수 다중 반환 값 등

```bash
# 튜플 표현
my_tuple_1 = ()
my_tuple_2 = (1,)
my_tuple_3 = (1, 'a', 3, 'b', 5)
```

```bash
my_tuple = (1, 'a', 3, 'b', 5)

# 인덱싱
print(my_tuple[1])  # a

# 슬라이싱
print(my_tuple[2:4])  # (3, 'b')
print(my_tuple[:3])  # (1, 'a', 3)
print(my_tuple[3:])  # ('b', 5)
print(my_tuple[0:5:2])  # (1, 3, 5)
print(my_tuple[::-1])  # (5, 'b', 3, 'a', 1) 


# 길이
print(len(my_tuple))  # 5
```

```bash
# 튜플은 불변
# TypeError: 'tuple' object does not support item assignment
my_tuple[1] = 'z'
```

```bash
# 다중 할당
x, y = 10, 20
print(x)  # 10
print(y)  # 20 

# 실제 내부 동작
(x, y) = (10, 20)
```

```bash
# 값 교환
x, y = 1, 2
x, y = y, x 

# 실제 내부 동작
temp = (y, x)  # 튜플 생성
x, y = temp  # 튜플 언패킹
print(x, y)  # 2 1


```

```bash
# 그룹화
student = ('Kim', 20, 'CS')
name, age, major = student  # 언패킹 

print(name, age, major)  # Kim 20 CS


```

- range
  
  - 연속된 정수 시퀀스를 **생성**하는 **변경 불가능한** 자료형
  
  - 모든 매개변수는 **정수**만 사용 가능
  
  - range(n)
    
    - **0**부터 **n-1**까지 1씩 증가
  
  -  range(n,m)
    
    - **n**부터  **m-1** 까지의 1씩 증가
  
  - range(n,m, step)
    
    - **n**부터 **m-1**까지 step만큼 증가
  
  - 증가 값 규칙
    
    - 기본 증가 값은 **1**
    
    - 음수 증가 값
      
      - 감소하는 수열 생성
    
    - 양수 증가 값
      
      - 증가하는 수열 생성
    
    - 증가 값이 **0** 이면 에러
  
  - 음수 증가 시
    
    - 시작 값이 끝 값보다 커야 함
  
  - 양수 증가 시
    
    - 시작 값이 끝 값보다 작아야 함
  
  - 주로 반복문과 함께 활용 예정

```bash
range(시작 값, 끝 값, 증가 값)    
```

```bash
my_range_1 = range(5)
my_range_2 = range(1, 10)
my_range_3 = range(5, 0, -1)

print(my_range_1)  # range(0, 5)
print(my_range_2)  # range(1, 10)
print(my_range_3)  # range(5, 0, -1)

# 리스트로 형 변환 시 데이터 확인 가능
print(list(my_range_1))  # [0, 1, 2, 3, 4]
print(list(my_range_2))  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(my_range_3))  # [5, 4, 3, 2, 1]
```

```bash
# 음수 증가 시
# 시작 값이 끝 값보다 큰 경우 (정상)
print(list(range(5, 1, -1)))  # [5, 4, 3, 2]
# 시작 값이 끝 값보다 작은 경우
print(list(range(1, 5, -1)))  # []
```

```bash
# 양수 증가 시
# 시작 값이 끝 값보다 작은 경우 (정상)
print(list(range(1, 5)))  # [1, 2, 3, 4]
# 시작 값이 끝 값보다 큰 경우
print(list(range(5, 1)))  # []
```

```bash
# 주로 반복문과 함께 활용 예정
for i in range(1, 10):
    print(i)  # 1 2 3 4 5 6 7 8 9

for i in range(1, 10, 2):
    print(i)  # 1 3 5 7 9

```


