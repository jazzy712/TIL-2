## DFS(깊이 우선탐색)

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-54-45-image.png" title="" alt="" data-align="center">

- 비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요

- **시작 정점**의 한 방향으로 **갈 수 있는 경로가 있는 곳까지** 깊이 탐색해 가다가 **더 이상 갈 곳이 없게 되면**, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회방법

- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 **깊이 우선 탐색**을 반복해야 하므로 **후입선출** 구조의 스택 사용

- dfs 알고리즘
  
  - 1. 시작 정점 v를 결정하여 방문
    
    2. 정점 v에 인접한 정점 중에서
       
       1)방문하지 않은 정점 w가 있다면, 정점 v를 스택에 push하고 정점 w를 방문 그리고 w를 v로 하여 다시 2. 반복
       
       2)방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 2. 반복
    
    3. 스택이 공백이 될 때까지 2. 반복
  
  ```python
  visited[], stack[] 초기화
  Dfs(v)
      시작점 v 방문;
      visited[v] <- true;
      while {
          if ( v의 인접 정점 중 방문 안 한 정점 w가 있으면)
              push(v);
              v <- w; (w에 방문)
              visited[w] <- true;
          else
              if (스택이 비어 있지 않으면)
                  v <- pop(stack);
              else
                  break
      }
  end Dfs{}
  ```

- dfs 예시
  
  - 초기 상태 : 배열 visited 를 False로 초기화하고, 공백 스택 생성
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-12-46-image.png" title="" alt="" data-align="center">
  
  - 1. 정점 A 시작으로 깊이 우선 탐색(dfs) 시작
  
  ```python
  A 방문;
   visited[A] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-17-16-image.png" title="" alt="" data-align="center">
  
  - 2. 정점 A에 방문하지 않은 정점 B,C가 있으므로 A를 스택에 push 하고, 인접 정점 B,C 중에서 오름차순에 따라 B를 선택하여 탐색을 계속
  
  ```python
  push(A);
  B 방문;
  visited[B] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-20-12-image.png" title="" alt="" data-align="center">
  
  - 3. 정점 B에 방문하지 않은 정점 D,E가 있으므로 B를 스택에 push 하고, 인접 정점 D,E 중에서 오름차순에 따라 D를 선택하여 탐색을 계속
  
  ```python
  push(B);
  D 방문;
  visited[D] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-21-37-image.png" title="" alt="" data-align="center">
  
  - 4. 정점 D에 방문하지 않은 정점 F가 있으므로 D를 스택에 push 하고, 인접 정점 F를 선택하여 탐색을 계속
  
  ```python
  push(D);
  F 방문;
  visited[F] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-22-48-image.png" title="" alt="" data-align="center">
  
  - 5. 정점 F에 방문하지 않은 정점 E,G가 있으므로 F를 스택에 push 하고, 인접 정점 E,G 중에서 오름차순에 따라 E를 선택하여 탐색 계속
  
  ```python
  push(F);
  E 방문;
  visited[E] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-23-59-image.png" title="" alt="" data-align="center">
  
  - 6. 정점 E에 방문하지 않은 정점 C가 있으므로 E를 스택에 push 하고, 인접정점 C를 선택하여 탐색 계속
  
  ```python
  push(E);
  C 방문;
  visited[C] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-25-01-image.png" title="" alt="" data-align="center">
  
  - 7. 정점 C에서 방문하지 않은 인접 정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 E에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-26-00-image.png" title="" alt="" data-align="center">
  
  - 8. 정점 E는 방문하지 않은 인접 정점이 없으므로, 다시 스택을 pop하여 받은 정점 F에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-26-53-image.png" title="" alt="" data-align="center">
  
  - 9. 정점 F에 방문하지 않은 정점 G가 있으므로 F를 스택에 push 하고, 인접 정점 G를 선택하여 탐색 계속
  
  ```python
  push(F);
  G 방문;
  visited[G] <- true;
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-28-02-image.png" title="" alt="" data-align="center">
  
  - 10. 정점 G에서 방문하지 않은 인접 정점이 없으므로, 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 F에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-29-00-image.png" title="" alt="" data-align="center">
  
  - 11. 정점 F에서 방문하지 않은 인접 정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 D에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-30-07-image.png" title="" alt="" data-align="center">
  
  - 12. 정점 D에서 방문하지 않은 인접 정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 B에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-31-17-image.png" title="" alt="" data-align="center">
  
  - 13. 정점 B에서 방문하지 않은 인접 정점이 없으므로, 다시 마지막 정점으로 돌아가기 위해 스택을 pop하여 받은 정점 A에 대해서 방문하지 않은 인접 정점이 있는지 확인
  
  ```python
  pop(stack);
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-10-32-19-image.png" title="" alt="" data-align="center">
  
  - 14. 현재 정점 A에서 방문하지 않은 인접 정점이 없으므로 마지막 정점으로 돌아가기 위해 스택을 pop하는데, 스택이 공백이므로 깊이 우선 탐색(dfs) 을 종료
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-14-10-33-03-image.png)

## **2. DFS 구현 방식**

아래는 DFS를 구현하는 대표적인 방법(1번)을 포함해 총 4가지 방법을 코드와 함께 안내합니다.

1. 인접 행렬 + 스택
2. 인접 리스트 + 스택
3. 인접 행렬 + 재귀 함수
4. 인접 리스트 + 다른 input 구조

이 때, `그래프 표현 방식`인 **인접 행렬**과 **인접 리스트**는 다음과 같은 차이가 있습니다.

- **인접 행렬**
  - 2차원 배열(행렬)로 그래프 연결 정보를 표현
  - 노드의 개수가 **적거나**, 그래프가 조밀(dense)할 때 사용하기 편리
  - 공간 복잡도가 대체로 `$O(N^2)$` (N은 노드 수)
- **인접 리스트**
  - 리스트를 사용하여 노드별로 연결된 정점들을 저장
  - 노드의 개수가 많지만 간선이 상대적으로 **드문(sparse)** 그래프에서 공간 절약 가능
  - 공간 복잡도는 `$O(N + E)$` (E는 간선 수)



**2.1 인접 행렬 + 스택**

```python
import sys
from pprint import pprint as print

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬(Adjacency Matrix) 생성: V+1 크기 (노드를 1부터 사용)
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
# print(adj_matrix)

# 간선 정보를 인접행렬에 기록 (양방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1
# print(adj_matrix)


def DFS_stack(start):
    '''
    스택을 활용한 DFS (깊이 우선 탐색)

    - start: 시작 노드 번호
    - visited: 방문 여부 확인용 리스트
    - adj_matrix: 인접 행렬 (n1, n2 사이가 연결되면 값 = 1)
    '''
    stack = [start]  # 스택 초기화 (시작 노드 삽입)
    visited = [0] * (V + 1)  # 각 노드 방문 여부 체크

    while stack:
        current_node = stack.pop()  # 스택의 마지막 원소 꺼냄

        if visited[current_node] == 0:
            visited[current_node] = 1  # 방문 처리
            print(current_node, end='')  # 방문 노드 출력(줄바꿈 없이)

            # 현재 노드와 인접한 노드들을 스택에 삽입 (현재 노드에서 갈 수 있는 다음 노드들을 스택에 추가)
            # V부터 1까지 역순으로 확인 (작은 번호의 노드가 스택의 위쪽에 위치하게 됨, 작은 번호 우선)
            # 만약, 큰 번호의 노드를 우선 방문하고 싶다면 정방향(작->큰)으로 스택에 push (for next_node in range(1, V + 1))
            for next_node in range(V, 0, -1):
                if (
                    adj_matrix[current_node][next_node] == 1
                    and visited[next_node] == 0
                ):
                    stack.append(next_node)

DFS_stack(1)

```

- push 시점 방문 처리 방식

```python
import sys

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 행렬 생성 (노드 번호 1 ~ V)
adj_matrix = [[0]*(V+1) for _ in range(V+1)]

# 간선 정보 (양방향)
for i in range(E):
    n1 = data[2*i]
    n2 = data[2*i + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

def DFS_stack_push_style(start):
    '''
    스택을 활용한 DFS (Push 시점 방문 처리)
    - 인접 행렬 adj_matrix를 사용
    - 방문 순서: 작은 번호 노드를 우선 방문 (역순 push)
    '''

    visited = [0]*(V+1)
    stack = []

    # 시작 노드를 먼저 방문 처리 후 스택에 push
    visited[start] = 1
    stack.append(start)

    while stack:
        current = stack.pop()
        print(current, end='')  # 문제 요구대로 줄바꿈 없이 출력

        # current 노드의 인접 노드들을 확인
        # 작은 번호를 우선 방문하고 싶다면, 스택에는 큰 번호부터 push
        for next_node in range(V, 0, -1):
            if adj_matrix[current][next_node] == 1 and not visited[next_node]:
                # 방문하지 않은 노드를 발견하면,
                # 이 시점에서 방문 처리 후 push
                visited[next_node] = 1
                stack.append(next_node)

# 실행
DFS_stack_push_style(1)

```

**2.2 인접 리스트 + 스택**

```python
import sys
from pprint import pprint as print

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 리스트(Adjacency List) 생성
adj_list = [[] for _ in range(V + 1)]
print(adj_list)

# 간선 정보 입력 (양방향)
for i in range(E):
    n1, n2 = data[2 * i], data[2 * i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
print(adj_list)

# 방문 순서를 결정하기 위해, 인접 리스트를 각 노드별로 내림차순 정렬
# 내림차순 정렬해두면, 스택에서 pop할 때 작은 번호를 먼저 방문하도록 유도 가능
# 문제 요구사항(‘노드를 작은 번호부터 방문해야 한다’)과 스택의 LIFO 구조를 맞추기 위함
for i in range(1, V + 1):
    adj_list[i].sort(reverse=True)


def DFS_stack_adj_list(start):
    '''
    스택을 활용한 DFS (깊이 우선 탐색) - 인접 리스트 버전

    - start: 탐색을 시작할 노드 번호
    - adj_list: 각 노드별 연결된 노드 목록 (내림차순 정렬 상태)
    - visited: 노드 방문 여부를 기록하는 리스트
    '''
    stack = [start]  # 시작 노드를 스택에 넣음
    visited = [0] * (V + 1)  # 방문 여부 리스트

    while stack:
        current_node = stack.pop()
        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end='')  # 문제 출력 예시에 맞춰 줄바꿈 없이

            # 현재 노드의 인접 노드들을 스택에 push
            # adj_list[current_node]가 이미 내림차순 정렬되어 있으므로
            # 그대로 순회하면 작은 번호가 스택 top에 올라가 먼저 방문함
            for next_node in adj_list[current_node]:
                if visited[next_node] == 0:
                    stack.append(next_node)


# 실제 DFS 실행 (예: 시작 노드 1)
DFS_stack_adj_list(1)

```

-  구현 설명
1. **인접 리스트(`adj_list`) 생성**

```python
adj_list = [[] for _ in range(V+1)]
```

- 노드가 1부터 V까지 존재하므로, 인덱스를 맞추기 위해 `V+1` 크기로 생성

- `adj_list[u]`에는 노드 `u`와 인접한 노드들을 담음
2. **간선 정보 입력 (양방향 그래프)**

```python
for i in range(E):
    n1, n2 = data[2*i], data[2*i + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
```

- 각 노드 쌍(n1, n2)에 대해 `adj_list[n1]`와 `adj_list[n2]`에 서로 추가
3. **인접 리스트 정렬**

```python
for i in range(1, V+1):
    adj_list[i].sort(reverse=True)
```

- **내림차순 정렬**해두면, 스택에서 pop할 때 **작은 번호를 먼저 방문**하도록 유도 가능

- 문제 요구사항(‘노드를 작은 번호부터 방문해야 한다’)과 스택의 LIFO 구조를 맞추기 위함

- 만약 큰 번호부터 방문하고 싶다면 `reverse=False`로 정렬하거나 정렬을 생략할 수도 있음
4. **DFS (`DFS_stack_adj_list`)**

```python
def DFS_stack_adj_list(start):
    stack = [start]
    visited = [0]*(V+1)
    while stack:
        current_node = stack.pop()
        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end='')
            for next_node in adj_list[current_node]:
                if visited[next_node] == 0:
                    stack.append(next_node)
```

- **스택**을 이용한 DFS
- 스택에서 노드를 pop → 방문하지 않았다면 방문 처리 + 인접 노드 push
- 인접 노드를 push할 때, **이미 visited인 경우**는 제외
- 출력 형식은 문제 예시와 동일하게 줄바꿈 없이 노드 번호 이어붙이기

### **2.3 인접 행렬 + 재귀 함수**

```python
import sys
from pprint import pprint

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬 생성 (V+1 크기)
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 저장
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

visited = [0] * (V + 1)  # 방문 여부 배열


def DFS_recursive(start):
    '''
    재귀 함수를 이용한 DFS (깊이 우선 탐색)

    - start: 현재 방문할 노드
    - visited[start] = 1로 방문 처리 후,
      인접 노드들을 재귀적으로 방문
    '''
    visited[start] = 1
    print(start, end='')  # 줄바꿈 없이 출력

    # start 노드와 인접하고, 아직 방문 안 한 노드를 재귀 호출
    for next_node in range(1, V + 1):
        if adj_matrix[start][next_node] == 1 and visited[next_node] == 0:
            DFS_recursive(next_node)


# DFS 실행
DFS_recursive(1)


"""
동작 과정 예시

1. DFS_recursive(1) 호출
2. 1번 노드 방문 표시 및 출력
3. 1번 노드의 인접 노드 중 방문하지 않은 2번 노드 발견
4. DFS_recursive(2) 호출
5. 2번 노드 방문 표시 및 출력
6. 2번 노드의 인접 노드 중 방문하지 않은 4번 노드 발견
7. DFS_recursive(4) 호출
8. ...
9. 마지막 노드에서 더 이상 방문할 인접 노드가 없음
10. 이전 호출로 돌아가며 남은 인접 노드 확인
11. 모든 노드 방문 완료 시 전체 DFS 종료
==> 명시적인 종료 조건 없이도 그래프의 모든 연결된 노드를 방문한 후 DFS가 자연스럽게 종료됨
"""


"""
DFS_recursive 함수의 종료 조건
1. 암묵적 종료 조건
  - 현재 노드에서 더 이상 방문할 수 있는 인접 노드가 없을 때 함수가 종료
  - for 루프가 모든 노드를 검사했지만 조건을 만족하는 노드를 찾지 못했을 때 발생
2. 방문 여부 확인
  - if adj_matrix[start][next_node] == 1 and visited[next_node] == 0: 조건에서, 
  모든 인접 노드가 이미 방문되었다면 재귀 호출이 더 이상 일어나지 않음
"""

```

- 재귀 함수를 이용할 때에는 **함수 호출 스택**을 자연스럽게 사용합니다.
- `dfs_matrix_recursive` 함수를 호출할 때마다, 아직 방문하지 않은 노드가 있으면 그 노드를 재귀적으로 방문하는 구조입니다.

### 2.4 인접 리스트 + 다른 input 구조

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-12-14-01-image.png" title="" alt="" data-align="center">

```python
import sys

sys.stdin = open('input2.txt')


def dfs_adjlist_another_input(V, E):
    '''
    스택을 활용한 DFS (인접 리스트 버전)
    - 정점이 0부터 (V-1)까지 번호를 갖지만,
      실제 출력 시에는 각 노드에 +1을 하여 1~V 범위로 출력.
    - 예) 노드 0 -> 출력 "1", 노드 1 -> 출력 "2", ...
    '''
    # 인접 리스트 생성
    adj_list = [[] for _ in range(V)]

    # 간선 정보 (양방향)
    for _ in range(E):
        n1, n2 = map(int, input().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # 작은 번호 노드를 우선 방문하기 위해, 인접 리스트를 '내림차순' 정렬
    # => 스택에 push 시 작은 노드가 먼저 pop되도록
    for i in range(V):
        adj_list[i].sort(reverse=True)

    stack = [0]  # 시작 노드(0)로 설정
    visited = [0] * V
    result = []  # 방문 순서 기록

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
            # 여기서 current+1을 출력(문자열로)
            result.append(str(current + 1))  # 숫자 -> 문자열로 변환

            # 인접 노드들을 스택에 push (아직 방문 안 한 노드만)
            for nxt in adj_list[current]:
                if not visited[nxt]:
                    stack.append(nxt)

    # 방문 순서를 이어붙여 문자열로 반환
    return ''.join(result)


# -------------------------------
V = int(input().strip())  # 정점 개수
E = int(input().strip())  # 간선 개수

# DFS 실행
dfs_result = dfs_adjlist_another_input(V, E)
print(dfs_result)
```

- 코드 설명
  
  1. **입력 구조**
     
     - 첫 줄: 정점 개수 `V`
     - 둘째 줄: 간선 개수 `E`
     - 이후 `E`줄에 걸쳐 간선 정보 (예: `0 1`, `0 2`, …)
     - 정점은 `0`부터 `V-1`까지 번호가 매겨짐
  
  2. **인접 리스트 생성**
     
     ```python
     adj_list = [[] for _ in range(V)]
     for _ in range(E):
        n1, n2 = map(int, sys.stdin.readline().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)
     ```
     
     - `adj_list[i]`에 정점 i와 인접한 노드들을 저장
     - 양방향 그래프이므로 `n1->n2`, `n2->n1` 모두 추가
  
  3. **정렬**
     
     ```python
     for i in range(V):
        adj_list[i].sort(reverse=True)
     ```
     
     - **내림차순 정렬**해두면, 스택에서 pop할 때 작은 번호의 노드를 먼저 방문.
     - 예: `[2,1]` 을 스택에 넣으면, pop 시 먼저 `1`이 나옴 (작은 번호 우선)
  
  4. **스택 기반 DFS**
     
     ```python
     stack = [0]
     visited = [False]*V
     result = []
     
     while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            result.append(str(current + 1))  # 노드번호+1을 문자열로
            for nxt in adj_list[current]:
                if not visited[nxt]:
                    stack.append(nxt)
     ```
     
     - 시작 노드는 `0`(→ 출력 시 `'1'`)
     - 방문하면 `visited[current] = True`, 그리고 결과 목록에 `current+1`을 문자열로 넣음
     - 인접 노드 중 방문 안 한 노드를 스택에 push
  
  5. **결과 출력**
     
     ```python
     return ''.join(result)
     ```
     
     - 예: `'1246573'` 형태. (각 노드를 붙여서 생성한 문자열)
  
  6. **주의사항**
     
     - **노드 0 → 출력 '1'**, 노드 1 → 출력 '2' … 식으로, 기존 노드번호에 +1 해주어 문제 요구 사항 `'1246573'` 형식을 맞춤
     - 그래프 구조나 간선 입력에 따라 방문 순서가 달라질 수 있음
     - 문제의 예시 그래프에서 DFS 순서가 `'1246573'`가 될 것으로 가정

## DFS 알고리즘 핵심 순서

### 3.1 스택 DFS 핵심 순서

1. **시작 정점 `v`** 를 **스택에 push** 하되, **아직 방문하지 않는다** (visited[v] = False).
2. **스택이 비어 있지 않은 동안**:
   1. **스택 최상단 노드를 pop**하여 `current`라 한다.
   2. **`current`가 아직 방문되지 않았다면**(`visited[current] == False`),
      - **`current`를 방문 처리(visited[current] = True)`** 및 필요한 작업(출력 등)을 수행한다.
      - **인접한 노드 중 방문하지 않은 노드를 스택에 push**한다. (이 시점에서는 visited 처리 안 함)
3. **스택이 공백이 되면**(더 이상 갈 곳이 없으면) DFS 종료.

> - pop 시점에 방문 처리 → 한 노드가 스택에 여러 번 들어갈 수 있으나, 실제로 방문은 한 번만 이루어진다.

- '방문하지 않은 정점 w'를 확인하면 push하지만, pop해서 실제로 뽑아봤을 때 여전히 방문 전이면 그때 방문한다.

### 3.2 재귀 DFS 핵심 순서

1. **시작 정점 `v`** 를 방문 처리(`visited[v] = True`)하고, 필요한 작업(출력 등)을 수행한다.
2. **정점 `v`와 인접한 노드들**을 확인하면서, 아직 방문하지 않은 정점 `w`를 발견하면,
   - `DFS(w)`를 재귀 호출한다. (호출 스택에 `v`가 잠시 보관됨)
3. **더 이상 방문할 인접 정점이 없거나 모두 방문 되었다면**,
   - 재귀 함수는 끝나면서 **이전 호출**(`DFS(v)`)로 돌아간다(백트래킹)
4. 모든 경로를 탐색하고, 재귀 호출 스택이 비면 DFS가 완료된다.

> - 함수 호출 스택을 통해 ‘끝까지 파고든 뒤 되돌아오는(백트래킹)’ 과정을 자동으로 구현할 수 있다.
>   예) DFS_recursive(start) → 인접 노드 재귀 → 더 이상 갈 곳 없으면 함수 종료 → 이전 노드로 복귀.

---

## 4. 두 코드(스택 방식 vs 재귀 방식) 차이점

- **재귀 방식**
  - 내부적으로 **함수 호출 스택**을 사용하여 “끝까지 들어갔다가 되돌아오는” 과정을 자동화.
  - 코드가 짧고 간결하지만, 깊은 재귀가 필요한 그래프(노드 수가 매우 큰 경우)에서는 파이썬 재귀 제한 등에 주의.
- **스택 방식 (Pop 시 방문)**
  - **명시적 스택 자료구조**로 DFS를 구현.
  - 노드를 push할 때는 방문 표시를 안 하고, **pop으로 꺼냈을 때** 방문되지 않은 것이면 방문 처리.
  - 여러 번 스택에 들어가도, “방문 안 된 시점에만 방문 처리”를 하므로 중복 방문은 없음.

---

## **5. BFS와의 비교**

- **BFS (너비 우선 탐색)**
  - 시작 노드에 인접한 모든 노드를 먼저 방문하고, 그 다음 레벨의 노드를 탐색
  - **선입선출(FIFO)** 구조의 큐(Queue)를 사용하는 것이 자연스럽습니다.
- **DFS (깊이 우선 탐색)**
  - 한 노드에서 출발해 갈 수 있는 경로를 **최대한 깊이** 탐색 후, 더 이상 내려갈 수 없을 때 **뒤로** 올라옴
  - **후입선출(LIFO)** 구조의 스택(Stack)을 사용하거나 재귀 함수를 이용해 구현하는 것이 일반적입니다.

> 🔴주의🔴
> 
> - “DFS는 큐로 구현할 수 없다” 혹은 “BFS는 스택으로 구현할 수 없다”라고 말하는 것은 **틀린 표현**입니다.
> - 다른 자료구조를 사용해도 추가적인 연산이나 조작을 통해 유사한 결과를 낼 수 있지만, **가장 자연스럽고 효율적인 구현**은 DFS → 스택, BFS → 큐를 사용하는 것입니다.

---

## **6. 참고: DFS vs. BFS, 그리고 자료구조**

- **DFS**
  - **스택**(또는 재귀 함수)
  - 깊이 우선 탐색(LIFO)
- **BFS**
  - **큐**
  - 너비 우선 탐색(FIFO)
- 각 알고리즘은 탐색 전략과 자료구조가 **자연스럽게 매칭**됩니다.
- “DFS는 큐로 못 한다, BFS는 스택으로 못 한다”는 **엄밀히는 틀린 말**이지만,
  일반적인 구현과 효율성 측면에서는 DFS ↔ 스택, BFS ↔ 큐 조합이 가장 합리적입니다.

---

## **7. 마무리**

- **DFS(깊이 우선 탐색)**:
  1. **인접 행렬 + 스택**
  2. **인접 리스트 + 스택**
  3. **인접 행렬 + 재귀 함수** 위 3가지 방법을 기본적으로구현할 수 있으며,
     그래프를 **어떻게 표현하느냐(행렬 vs. 리스트)**, 스택을 코드로 직접 쓰느냐(스택) vs. 언어의 호출 스택(재귀)를 활용하느냐에 따라 구현이 달라집니다.
- BFS(너비 우선 탐색)와의 차이
  - BFS는 **레벨 순**으로 탐색하므로 **큐(Queue)** 사용이 일반적
  - DFS는 **한쪽 방향**으로 끝까지 탐색 후 돌아오는 방식이므로 **스택(Stack)** 혹은 재귀(호출 스택)를 활용
- 결론적으로, **그래프 탐색** 시 목적과 자료구조 특성에 따라 DFS와 BFS를 적절히 선택 및 구현하여 문제를 해결할 수 있음
