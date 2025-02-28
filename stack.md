## Stack

- stack의 특성
  
  - 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
  
  - 선형 구조
    
    - 선형 구조 : 자료 간의 관계가 1대1 관계
    
    - 비선형 구조 : 자료 간 관계가 1대N 관계
  
  - stack에 자료를 삽입하거나 자료를 꺼낼 수 있음
  
  - 마지막에 삽입한 자료를 가장 먼저 꺼냄
    
    - **후입선출**
  
  - 자료 구조 : 자료를 선형으로 저장할 저장소
    
    - 배열 사용 가능
    
    - 저장소 자체 -> stack
    
    - stack에서 마지막 삽입된 원소의 위치 -> top
  
  - 연산
    
    - 삽입 : 저장소에 자료 저장(push)
    
    - 삭제 : 저장소에서 자료 꺼냄, 꺼낸 자료는 삽입한 자료의 역순으로 꺼냄(pop)
    
    - isEmpty : stack이 공백인지 확인
    
    - peek : stack의 top에 있는 item(원소) 반환
  
  - stack의 삽입/삭제 과정
    
    - 빈 stack에 원소 a,b,c를 차례로 삽입 후 한번 삭제
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-09-13-39-image.png" title="" alt="" data-align="center">
  
  - push 알고리즘
    
    - append 메소드를 통해 리스트의 마지막에 데이터 삽입
    
    ```python
    def push(item):
        s.append(item)
    ```
  
  - pop 알고리즘
  
  ```python
  def pop():
      if len(s) == 0:
          # underflow
          return
      else:
          return s.pop()
  ```
  
  ```python
  def pop():
      global top
      if top == -1:
          print('underflow')
          return 0
      else:
          top -= 1
          return stack[top+1]
      
      
  print(pop())
  
  if top > -1:                    # pop()
      top -= 1
      print(stack[top+1])
  ```

- stack 구현 고려사항
  
  - 1차원 배열 사용하여 구현할 경우 구현 용이하다는 장점이 있지만 스택 크기를 변경하기 어렵다는 단점이 있다

- 괄호 검사
  
  - 괄호 종류 : [], {}, ()
  
  - 조건
    
    - 왼쪽 괄호 개수와 오른쪽 괄호 개수 같아야함
    
    - 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야함
    
    - 괄호  사이에는 포함 관계만 존재

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-09-46-18-image.png" title="" alt="" data-align="center">

-  여눈 괄호가 나오면 push, 닫는 괄호 나오면 pop하여 비교

- function call
  
  - 프로그램에서의 함수 호출과 복귀에 따른 수행 순서 관리
    
    - 가장 마지막에 호출된 함수가 가장 먼저 실행 완료하고 복귀하는 후입선출 구조이므로, 후입선출 구조의 스택 이용하여 수행순서 관리
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-13-03-image.png" title="" alt="" data-align="center">
  
  - 함수 호출 발생하면 호출한 함수 수행에 필요한 지역변수, 매개변수 및 수행 후 복귀할 주소 등의 정보를 stack frame에 저장하여 시스템 스택에 삽입
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-14-05-image.png" title="" alt="" data-align="center">
  
  - 함수 실행이 끝나면 시스템 stack의 top 원소(stack frame)를 삭제(pop)하면서 프레임에 저장되어 있던 복귀주소를 확인하고 복귀
  
  - 함수 호출과 복귀에 따라 이 과정을 반복하여 전체 프로그램 수행이 종료되면 시스템 스택은 공백 스택이 됨
  
  <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-21-34-image.png" alt="" data-align="center">
  
  - 함수 호출과 복귀에 따른 전체 프로그램의 수행 순서
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-21-58-image.png" title="" alt="" data-align="center">



## 재귀호출

- 재귀호출 
  
  - 필요한 함수가 자신과 같은 경우 다시 호출하는 구조
  
  - 함수에서 실행해야 하는 작업의 특성에 따라 일반적인 호출방식보다 재귀호출방식을 사용하여 함수를 만들면 프로그램 크기를 줄이고 간단하게 작성
  
  - factoral
  
  - n애 대한 factorial : 1부터 n까지의 모든 자연수 곱하여 구하는 연산
  
  ```python
  n! = n x (n-1)!
   (n-1)! = (n-1) x (n-2)!
   (n-2)! = (n-2) x (n-3)!
  ...
   2! = 2 x 1!
   1! = 1
  ```
  
  - factorial 함수에서 n=4인 경우의 실행
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-27-50-image.png" title="" alt="" data-align="center">
  
  - 피보나치 수열
    
    - 0과 1로 시작하고 이전의 두 수 합을 다음 항으로 하는 수열
    
    - 0, 1, 1, 2, 3, 5, 8, 13 ...
    
    - i번째 값을 계산하는 함수 F
    
    ```python
    F0 = 0,F1 = 1
    Fi = Fi-1 + Fi-2 for i >= 2
    ```
    
    - 피보나치 수 구하는 재귀함수
    
    ```python
    def fibo(n):
        if n < 2:
            return n
        else:
            return fibo(n-1) + fibo(n-2) 
    cnt = 0                 # 호출 횟수 기록
    print(fibo(10), cnt)
    ```

- 모든 배열 원소에 접근

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-37-46-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-41-57-image.png" title="" alt="" data-align="center">

```python
def f(i, N):        # 크기 N인 배열 arr[i]에 접근
    if i == N:      # 중단 조건
        return
    else:            # 재귀 호출
        print(arr[i])
        f(i+1, N)
```

- 배열에 v가 있으면 1, 없으면 0을 return

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-42-44-image.png" title="" alt="" data-align="center">

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-13-10-46-22-image.png" title="" alt="" data-align="center">

```python
def f(i, N, v):        # v 찾는 값
    if i == N:
        return 0
    elif arr[i] == v:
        return 1
    else:
        return f(i+1, N)
```
