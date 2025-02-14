## Graph

- 그래프는 정점(Vertex)과 간선(Edge)으로 구성된 **비선형 자료구조**
- 복잡한 **M:N 관계**를 효율적으로 표현할 수 있음
- 트리나 선형 자료구조로는 표현하기 어려운 다양한 상황에서,
  그래프를 활용해 **노드 간 연결 관계**를 나타낼 수 있음

## **1. 기본 개념**

### **1.1 개념 및 구성**

- **정점(Vertex)**: 그래프에서 **데이터를 담는** 지점
- **간선(Edge)**: 정점 간 **연결** 관계
- **차수(Degree)**: 정점에 연결된 간선의 수
  - `V`: 정점의 개수
  - `E`: 간선의 개수
- 그래프는 **선형** 자료구조나 **트리**와 달리, 복잡한 **N:N 관계**를 표현하기에 적합

### **1.2 그래프 종류**

- **무향 그래프(Undirected Graph)**
  - 간선에 방향이 없어서, 양방향으로 이동 가능
- **유향 그래프(Directed Graph)**
  - 간선에 방향성이 있음
- **가중치 그래프(Weighted Graph)**
  - 간선마다 비용(가중치)이 존재
- **방향 비순환 그래프(DAG, Directed Acyclic Graph)**
  - 방향성이 존재하며, **사이클**이 없는 그래프
- 트리

### **1.3 그래프 유형**

- **완전 그래프**
  - 가능한 모든 정점 쌍이 간선으로 연결된 그래프
  - ∣V∣|V|개의 정점 각각이, 다른 모든 정점과 연결
- **부분 그래프**
  - 원 그래프에서 일부 정점이나 간선을 제외한 그래프

### **1.4 그래프 성질**

- **인접(Adjacency)**   
  
  - 두 정점을 잇는 간선이 존재하면 ‘인접’ 관계
  - 완전 그래프에서는 모든 정점이 서로 인접
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-35-26-image.png" title="" alt="" data-align="center">

- **경로(Path)**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-35-42-image.png" title="" alt="" data-align="center">
  
  - 그래프에서 간선을 연속적으로 따라갈 수 있는 경로
  - 어떤 정점 A에서 시작하여 다른 정점 B로 끝나는 순회로 두 정점 사이를 잇는 간선들을 순서대로
    나열한 것
  - 같은 정점을 거치지 않는 간선들의 sequence
  - 어떤 정점에서 다른 정점으로 가는 경로는 여러가지일 수 있다.
    - 0 – 6의 경로 예시
    - 정점들: 0 – 2 – 4 – 6
    - 간선들: (0, 2), (2, 4), (4, 6)
  - **단순 경로**: 경로에 같은 정점이 중복 없이 등장
  - **사이클(Cycle)**: 시작 정점으로 다시 돌아오는 경로 (예: 1→3→5→1)

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-36-00-image.png" title="" alt="" data-align="center">

- **차수(Degree)**
  - 각 노드에 연결된 간선의 수
  - 유향 그래프에서는 진입 차수(In-degree)와 진출 차수(Out-degree)로 구분

---

## **2. 그래프 표현**

### **2.1 인접 행렬 (Adjacency Matrix)**

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-36-39-image.png" title="" alt="" data-align="center">

- `V * V` 크기의 2차원 배열로, **연결** 여부를 `1` 과 `0`으로 표시
- 그래프가 조밀하게 연결되어 있는 경우(간선이 많을 때) 직관적
- **공간 복잡도**: `O(N^2)` (N은 노드 수)
- 예시 코드

```python
# 예시: 인접 행렬
#          A  B  C  D  E  F  G
adj = [[0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 1, 0, 0, 0, 0], # A
       [0, 1, 0, 0, 1, 1, 0, 0], # B
       [0, 1, 0, 0, 0, 1, 0, 0], # C
       [0, 0, 1, 0, 0, 0, 1, 0], # D
       [0, 0, 1, 1, 0, 0, 1, 0], # E
       [0, 0, 0, 0, 1, 1, 0, 1], # F
       [0, 0, 0, 0, 0, 0, 1, 0]] # G
```

- 일반적으로 인덱스 0을 고려하지 않기 위해 0으로 구성된 행열을 추가

### 2.2 **인접 리스트 (Adjacency List)**

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-11-37-25-image.png" title="" alt="" data-align="center">

- 각 정점마다 **인접한 정점 목록**을 리스트로 관리
- 그래프가 희소(sparse)할 때 간선을 효율적으로 관리 가능
- **공간 복잡도**: `O(N + E)` (E는 간선 수)
- 예시코드

```python
# 예시: 인접 리스트
graph_list = {
    0: [],
    1: [2, 3],
    2: [1, 3, 4],
    3: [2, 4],
    4: [2, 3]
}

# 또는

graph_list = [
    []
    [2, 3],
    [1, 3, 4],
    [2, 4],
    [2, 3]
]
```

### **2.3 간선 리스트**

- 그래프를 ‘간선’ 중심으로 관리
- (정점1, 정점2, 가중치) 형태로 목록화
- 특정 알고리즘(예: 크루스칼 최소 스패닝 트리 등)에서 유용

---

## **3. 그래프 탐색(순회)**

- 비선형 구조인 그래프에서는, **정점들을 빠짐없이 방문**하기 위해 탐색(순회) 알고리즘이 필요합니다.
- 주요 두 가지 방식: **DFS (깊이 우선 탐색)**, **BFS (너비 우선 탐색)**

### **3.1 DFS (Depth First Search)**

- **한쪽 경로로 깊이** 내려가다가 갈 곳이 없으면 뒤로 돌아오는 방식
- 주로 **스택(Stack)** 자료구조나 **재귀 함수**를 활용
- 예: 웹 크롤링, 백트래킹 문제 등에서 사용

### **3.2 BFS (Breadth First Search)**

- **시작 정점으로부터 가까운(인접) 노드**들을 먼저 방문, 그 다음 거리를 차례대로 탐색
- **큐(Queue)** 자료구조로 구현
- 예: 최단 경로(가중치가 동일한 경우), 레벨 순회 등에 사용

### **3.3 간단 예시 (DFS & BFS)**

```python
from collections import deque

# 그래프 (인접 리스트)
graph = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 5],
    4: [2],
    5: [3]
}

# DFS (스택 기반 또는 재귀)
def dfs(start):
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            # 인접 노드를 스택에 추가 (역순으로 처리하면 방문 순서가 바뀔 수 있음)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    return visited

# BFS (큐 기반)
def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return visited

print('DFS:', dfs(1))  # 예시 -> DFS: [1, 3, 5, 2, 4]
print('BFS:', bfs(1))  # 예시 -> BFS: [1, 2, 3, 4, 5]
```

## **4. 마무리**

1. **그래프**
   - **정점**과 **간선**으로 구성된 비선형 자료구조
   - 복잡한 **M:N 관계** 표현 가능
2. **그래프 표현**
   - **인접 행렬**: `V*V`행렬, 간단하지만 공간 많이 차지
   - **인접 리스트**: 정점마다 연결된 리스트, 공간 효율적
3. **그래프 탐색**
   - **DFS**(깊이 우선): 한 방향으로 깊게 탐색 (스택 / 재귀)
   - **BFS**(너비 우선): 가까운 정점을 먼저 탐색 (큐)

DFS와 BFS는 각각 별도의 콘텐츠에서 더 자세히 다룰 예정이니,
이 문서는 **그래프 전체의 기초 이해**를 중심으로 봐 두시면 좋습니다.


