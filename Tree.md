## Tree

- 개념   
  
  - 비선형 구조
  
  - 원소들 간에 1:n 관계를 가지는 자료구조
  
  - 원소들 간에 계층관계를 가지는 계층형 자료구조
  
  - 상위 원소에서 하위 원소로 내려가면서 확장되는 트리(나무) 모양의 구조
  
  - 한 개 이상의 노드로 이루어진 유한 집합
    
    - 노드 중 최상위 노드를 루트(root)라 함
    
    - 나머지 노들은 n(>= 0)개의 분리 집합 T1,...,TN 으로 분리 가능
  
  - T1,...,TN은 각각 하나의 트리가 되며(재귀적 정의) 루트의 부 트리(subtree)라 함
  
  - 트리(Tree)는 **사이클이 없는(acyclic)** **무향 연결 그래프**의 특별한 형태
    
    한 노드에서 다른 노드로 가는 **유일한 경로**가 존재 (분기 구조)
    
    **계층형**(Hierarchy) 자료구조의 대표적 예
    
    노드는 **최대 하나의 부모**와 여러 자식 노드를 가질 수 있음 (비선형 구조)
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-03-39-image.png" title="" alt="" data-align="center">
  
  - 노드(node) : 트리의 원소
  
  - 간선(edge) : 노드를 연결하는 선. 부모 노드와 자식 노드를 연결
  
  - 루트 노드(root node) : 트리의 시작 노드
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-07-05-image.png" title="" alt="" data-align="center">
  
  - 형제 노드(sibling node) : 같은 부모 노드의 자식 노드들
  
  - 조상 노드 : 간선을 따라 루트 노드까지 이르는 경로에 있는 모든 노드들
  
  - 서브 트리(subtree) : 부모 노드와 연결된 간선을 끊었을 때 생성되는 트리
  
  - 자손 노드 : 서브 트리에 있는 하위 레벨의 노드들
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-08-48-image.png" title="" alt="" data-align="center">
  
  - 차수(degree)
    
    - 노드의 차수 : 노드에 연결된 자식 노드의 수
    
    - 트리의 차수 : 트리에 있는 노드의 차수 중에서 가장 큰 값
    
    - 단말 노드(리프 노드) : 차수가 0인 노드. 자식 노드가 없는 노드
  
  - 높이
    
    - 노드의 높이 : 루트에서 노드에 이르는 간선의 수. 노드의 레벨
    
    - 트리의 높이 : 트리에 있는 노드의 높이 중에서 가장 큰 값. 최대 레벨
  
  <img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-12-04-image.png" alt="" data-align="center">

### **1.1 특징 요약**

<img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-05-24-image.png" alt="" data-align="center">

1. **루트 노드(Root)**: 부모가 없는 최상위 노드
2. **부모 노드(Parent)**: 어떤 노드와 연결되었으며, 상위 레벨에 있는 노드
3. **자식 노드(Child)**: 부모 노드에 연결된 하위 노드
4. **형제 노드(Sibling)**: 같은 부모를 공유하는 노드들
5. **리프(Leaf) / 단말 노드**: 자식이 없는 노드
6. **서브트리(Subtree)**: 부모-자식 간선을 끊었을 때 생기는 작은 트리
7. **차수(Degree)**
   - 노드의 차수: 해당 노드가 가진 **자식 노드 수**
   - 트리의 차수: 모든 노드의 차수 중 **최댓값**
8. **높이(Height)**
   - 노드의 높이: 루트에서 해당 노드까지의 간선 수 (또는 레벨)
   - 트리의 높이: 트리 내 노드들의 높이 중 **가장 큰 값**
   - **0부터 시작할 수도, 1부터 시작할 수도 있음** 

## Binary Tree(이진 트리)

- 개념
  
  - 모든 노드들이 2개의 서브트리를 갖는 특별한 형태의 트리
  
  - 각 노드가 자식 노드를 최대한 2개까지만 가질 수 있는 트리
    
    - 왼쪽 자식 노드
    
    - 오른쪽 자식 노드
  
  - **레벨 n**에서 최대 `2^n`개의 노드 가능
    
    높이가 h인 이진트리의 **노드 개수**
    
    - 최소: `h+1` (편향 트리)
    
    - 최대: `2^(h+1) - 1` (모든 레벨이 꽉 찬 포화 이진트리)
  
  - 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-18-10-image.png" title="" alt="" data-align="center">
  
  - 레벨 i에서의 노드의 최대 개수는 2의 i 제곱 (개)
  
  - 높이가 h인 이진 트리가 가질 수 있는 노드의 최소 개수는 (h+1)개가 되며, 최대 개수는 (2의 h+1 제곱 - 1)개가 됨
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-20-26-image.png" title="" alt="" data-align="center">

- **포화 이진 트리(Full Binary Tree)**
  
  - 모든 레벨에 노드가 포화상태로 차 있는 이진 트리
  
  - 높이가 h일 때, 최대의 노드 개수인 (2의 h+1 제곱 - 1)의 노드를 가진 이진 트리
  
  - 루트를 1번으로 하여 (2의 h+1 제곱 - 1) 까지 정해진 위치에 대한 노드 번호를 가짐
  
  - 모든 레벨이 **노드로 가득 찬** 이진 트리
    
    높이 h에서 노드 개수는 정확히 `2^(h+1)-1`
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-21-49-image.png" title="" alt="" data-align="center">

- **완전 이진 트리(Complete Binary Tree)**
  
  - 높이가 h이고 노드 수가 n개일 때(단, 2의 h 제곱 <= n <= 2의 h+1 제곱 - 1), 포화 이진 트리의 노드 번호 1번부터 n번까지 빈 자리가 없는 이진 트리
  
  - **왼쪽부터** 노드를 차곡차곡 채운 이진 트리
    
    마지막 레벨을 제외하면 포화 상태, 마지막 레벨에서도 **왼쪽부터** 노드가 연속적으로 존재
    
    오른쪽 자식만 존재하는 경우는 없는 트리
  
  - 노드가 10개인 완전 이진 트리
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-23-10-image.png" title="" alt="" data-align="center">

- **편향 이진 트리(Skewed Binary Tree)**
  
  - 높이 h에 대한 최소 개수의 노드를 가지면서 한쪽 방향의 자식 노드만을 가진 이진 트리
    
    모든 노드가 한쪽 자식만 가짐 (왼쪽만 or 오른쪽만)
    → 높이가 n이 될 수 있으며, 탐색 시 `O(n)` 발생
    
    이진 트리의 장점(균형적 접근)이 사라짐
    
    - 왼쪽 편향 이진 트리
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-23-49-image.png" title="" alt="" data-align="center">
    
    - 오른쪽 편향 이진 트리
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-24-09-image.png" title="" alt="" data-align="center">
    
    ## 

## 이진 탐색 트리(Binary Search Tree, BST)

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-41-41-image.png" title="" alt="" data-align="center">

- **탐색**을 빠르게 하기 위해 설계된 이진 트리

- **특징**
  
  1. 왼쪽 서브트리의 모든 노드 값 < 루트 노드 값
  2. 오른쪽 서브트리의 모든 노드 값 > 루트 노드 값
  3. 위 규칙이 재귀적으로 적용 (각 서브트리도 BST)

- **중위 순회**(왼 → 루트 → 오른쪽)를 수행하면 **오름차순 정렬**된 순서로 방문할 수 있음

- **삽입/삭제** 시, 규칙에 따라 탐색하며 적절한 위치에서 삽입/삭제

- **성능**:
  
  - 평균적으로 탐색/삽입/삭제가 **`O(log n)`**
  - 최악(편향 트리) 경우 **`O(n)`**

- ### 이진 탐색 트리 연산
  
  **탐색**
  
  - 루트에서 시작
  - 탐색할 키 값 x를 루트 노드의 키 값과 비교
    - x < 루트 : 왼쪽 서브트리 탐색연산
    - x > 루트 : 오른쪽 서브트리 탐색 연산
  - 서브트리에 대해서 순환적으로 탐색 연산을 반복한다.
  
  **삽입**
  
  - 먼저 탐색 연산을 수행
    - 같은 원소가 트리에 있는지 탐색하여 확인
    - 탐색 실패가 결정되는 위치가 삽입 위치
  
  **삭제**
  
  - 루트가 삭제될 때는 왼쪽 노드의 오른쪽 leaf 값을 루트자리에 가져오는게 제일 무난하다
    - 우측 노드에서 왼쪽값을 찾는거 보다 왼쪽에서 오른쪽 leaf를 찾는게 편하다

## **힙(Heap)**

- **완전 이진 트리**에서 **최댓값**(혹은 최솟값)을 효율적으로 찾기 위한 자료구조
- **최대 힙(Max-Heap)**
  - 부모 노드의 키 `$≥$` 자식 노드 키
  - 루트 노드는 가장 큰 키
  - 키 값이 가장 큰 노드를 찾기 위한 **완전 이진 트리**
- **최소 힙(Min-Heap)**
  - 부모 노드의 키 `$≤$` 자식 노드 키
  - 루트 노드는 가장 작은 키
  - 키 값이 가장 작은 노드를 찾기 위한 **완전 이진 트리**

### 6.1 힙 성질

1. **완전 이진 트리**
2. 각 노드가 자식 노드보다 **우선순위(크거나 작음)가 높음**
- **삽입**
  - 트리의 가장 마지막(완전 이진 트리 유지) 위치에 노드 삽입
  - 부모와 비교해 힙 성질이 깨지면 **위로 올리기**(swap)
- **삭제**
  - 루트 노드(최댓값/최솟값)만 삭제 가능
  - **마지막 노드**를 루트로 옮긴 후, 자식과 비교해 **힙 성질**이 지켜지도록 **내려보내기**(heapify)
- **우선순위 큐(Priority Queue)** 구현에 힙을 사용
  → 삽입/삭제 `O(log n)`, 최대/최소 `O(1)`

## **7. 정리**

1. **트리(Tree)**: 비선형 자료구조, 그래프의 일종. 노드들 간 계층 관계를 표현
2. **이진 트리(Binary Tree)**: 노드가 최대 2개 자식, 완전·포화·편향 등 형태
3. **트리 순회(Traversal)**: 전위·중위·후위 등, 모든 노드를 빠짐없이 방문
4. **이진 트리 표현**: 배열 인덱스 방식 / 연결 리스트 방식
5. **이진 탐색 트리(BST)**: 왼쪽 < 루트 < 오른쪽, 중위 순회 시 오름차순, 탐색/삽입/삭제 평균 `$O(log n)$`
6. **힙(Heap)**: 완전 이진 트리에서 최대/최소값을 효율적으로 추출, 우선순위 큐 구현에 활용

트리는 다양한 파생 구조(이진 탐색 트리, 힙 등)로 확장되며,

그래프 알고리즘, 계층형 데이터, 검색 최적화 등 폭넓게 쓰이는 핵심 자료구조

## Traversal(순회)

- 개념
  
  - 트리의 각 노드를 중복되지 않게 전부 방문하는 것
  
  - 트리는 비선형 구조이기 때문에 선형구조에서와 같이 선후 연결 관계 알 수 없음
  
  - 트리의 노드들을 체계적으로 방문
  
  - 반드시 root에서 시작하지 않아도 됨
  
  - 3가지 방법
    
    - 전위순회(preorder traversal)  VLR
      
      - 부모 노드 방문 후, 자식노드를 좌,우 순서로 방문
    
    - 중위순회(inorder traversal) : LVR
      
      - 왼쪽 자식노드, 부모노드, 오른쪽 자식노드 순으로 방문
    
    - 후위순회(postorder traversal) : LRV
      
      - 자식 노드를 좌우 순서로 방문 후, 부모 노드 방문
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-34-11-image.png" title="" alt="" data-align="center">

- 트리(특히 이진 트리)의 노드를 **중복 없이** 방문하는 과정
  
  - **전위 순회(Preorder)**: **루트 → 왼쪽 서브트리 → 오른쪽 서브트리**
  - **중위 순회(Inorder)**: **왼쪽 서브트리 → 루트 → 오른쪽 서브트리**
  - **후위 순회(Postorder)**: **왼쪽 서브트리 → 오른쪽 서브트리 → 루트**
  
  > 순회 시, 왼쪽 자식을 먼저 방문하는 것이 일반 규칙

- 전위순회
  
  - 수행 방법
  
  - 1. 현재 노드 n 방문하여 처리 : V
    
    2. 현재 노드 n의 왼쪽 서브트리로 이동 : L
    
    3. 현재 노드 n의 오른쪽 서브트리로 이동 : R
  
  ```python
  def preorder_traverse(T):               # 전위 순회
      if T:                               # T is not None
          visit(T)
          preorder_traverse(T.left)
          preorder_traverse(T.right)
  ```
  
  - 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-36-45-image.png" title="" alt="" data-align="center">

- 중위순회
  
  - 수행 방법
  
  - 1. 현재 노드 n의 왼쪽 서브트리로 이동: L
    
    2. 현재 노드 n을 방문하여 처리 : V
    
    3. 현재 노드 n의 오른쪽 서브트리로 이동: R
  
  ```python
  def inorder_traverse(T):                # 중위 순회
      if T:                               # T is not None
          inorder_traverse(T.left)
          visit(T)
          inorder_traverse(T.right)
  ```
  
  - 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-39-02-image.png" title="" alt="" data-align="center">

- 후위순회
  
  - 수행 방법
  
  - 1. 현재  노드 n의 왼쪽 서브트리로 이동: L
    
    2. 현재 노드 n의 오른쪽 서브트리로 이동: R
    
    3. 현재 노드 n을 방문하여 처리: V
  
  ```python
  def postorder_traverse(T):              # 후위 순회
      if T:                               # T is not None
          postorder_traverse(T.left)
          postorder_traverse(T.right)
          visit(T)
  ```
  
  - 예시
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-14-40-30-image.png" title="" alt="" data-align="center">

- 이진 트리의 순회
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-19-36-image.png" title="" alt="" data-align="center">
  
  - 전위 순회  : B > D -> H -> I -> E -> J
  
  - 중위 순회 : H -> D -> I -> B -> J -> E 
  
  - 후위 순회 : H -> I -> D -> J -> E -> B

## Binary Tree Expression(이진 트리 표현)

- 배열 이용한 이진 트리의 표현
  
  - 이진 트리에 각 노드 번호를  다음과 같이 부여
  
  - 루트의 번호를 1로 함
  
  - 레벨 n에 있는 노드에 대해 왼쪽부터 오른쪽으로 2^n부터 2^n+1 - 1 까지 번호를 차례로 부여
  
  - **포화 이진 트리, 완전 이진 트리에 적합**
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-24-23-image.png" title="" alt="" data-align="center">

- 노드 번호의 성질
  
  - 노드 번호가 i인 노드의 부모 노드 번호?   i //2
  
  - 노드 번호가 i인 노드의 왼쪽 자식 노드 번호?  2*i
  
  - 레벨 n의 노드 번호 시작 번호는?    2^n
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-25-40-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-25-52-image.png" title="" alt="" data-align="center">
  
  1. **배열 사용**
     - 인덱스 i를 노드 번호로 활용
     - 노드 i의 **부모**는 `i//2`, **왼쪽 자식**은 `2*i`, **오른쪽 자식**은 `2*i + 1` (1-based 인덱스)
     - 포화 이진 트리나 완전 이진 트리에서 인덱스 사용이 편리
     - 하지만, 노드 수가 동적으로 변할 때 비효율
  2. **연결 리스트(링크 구조) 활용**
     - 각 노드가 `left`, `right` 포인터(또는 참조)를 지님
     - 노드 추가·삭제가 유연 (포인터만 수정)
     - 일반 트리에서도 `children` 리스트로 표현 가능

- 배열 이용한 이진 트리의 표현
  
  - 노드 번호를 배열의 인덱스로 사용
  
  - 높이가 h인 이진 트리를 위한 배열의 크기는?
    
    - 레벨 i의 최대 노드 수는?  2^i
    
    - 따라서 2^h+1 - 1
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-31-45-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-32-04-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-32-22-image.png" title="" alt="" data-align="center">

## Binary Tree Expression 2

- 부모 번호를 인덱스로 자식 번호를 저장
  
  - 정점의 개수 == 간선의 개수 + 1
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-33-02-image.png" title="" alt="" data-align="center">

- 자식 번호를 인덱스로 부모 번호를 저장
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-33-46-image.png" title="" alt="" data-align="center">

- 루트 찾기, 조상 찾기
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-34-09-image.png" title="" alt="" data-align="center">

- 배열을 이용한 이진 트리 표현의 단점
  
  - 편향 이진 트리의 경우에 사용하지 않는 배열 원소에 대한 메모리 공간 낭비 발생
  
  - 트리의 중간에 새로운 노드를 삽입하거나 기존의 노드를 삭제할 경우 배열의 크기 변경 어려워 비효율적

- 단점 보완 위해 연결리스트 이용하여 트리 표현

- 연결 자료구조를 이용한 이진 트리의 표현
  
  - 이진 트리의 모든 노드는 최대 2개의 자식 노드를 가지므로 일정한 구조의 단순 연결 리스트 노드를 사용하여  구현
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-35-50-image.png" title="" alt="" data-align="center">

- 완전 이진 트리의 연결 리스트 표현
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-47-19-image.png" title="" alt="" data-align="center">

- 수식 트리
  
  - 수식을 표현하는 이진 트리
  
  - 수식 이진 트리(Expression Binary Tree)라고도 부름
  
  - 연산자는 루트 노드이거나 가지 노드
  
  - 피연산자는 모두 잎 노드
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-48-45-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-04-15-49-13-image.png" title="" alt="" data-align="center">
  
  - 증위 순회 : A / B * C * D + E (중위 표기법)
  
  - 후위 순회 : A B / C * D * E + (후위 표기법)
  
  - 전위 순회 : + * * / A B C D E (전위 표기법)





# Binary Search Tree(이진 탐색 트리)

- 개념
  
  - 탐색작업을 효율적으로 하기 위한 자료구조
  
  - 모든 원소는 서로 다른 유일한 키를 가짐
  
  - key(왼쪽 서브트리)<key(루트 노드)<key(오른쪽 서브트리)
  
  - 왼쪽 서브트리와 오른쪽 서브트리도 이진 탐색 트리
  
  - 중위 순회하면 오름차순으로 정렬된 값 얻을 수 있음
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-05-09-37-32-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-05-09-37-43-image.png" title="" alt="" data-align="center">

- **탐색연산**
  
  - 루트에서 시작
  
  - 탐색할키 값 x를 루트 노드의 키 값과 비교
    
    - (키 값x  = 루트 노드의 키 값)인 경우 : 원하는 원소를 찾았으므로 탐색연산 성공
    
    - (키 값x < 루트 노드의 키 값)인 경우 : 루트 노드의 왼쪽 서브트리에 대해서 탐색연산 수행
    
    - (키 값x > 루트 노드의 키 값)인 경우 : 루트 노드의 오른쪽 서브트리에 대해서 탐색연산 수행
  
  - 서브트리에 대해서 순환적으로 탐색연산 반복
  
  - 13 탐색
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-05-09-39-50-image.png" title="" alt="" data-align="center">

- **삽입연산**
  
  - 먼저 탐색 연산 수행
    
    - 삽입할 원소와 같은 원소가 트리에 있으면 삽입할 수 없으므로, 같은 원소가 트리에 있는지 탐색하여 확인
    
    - 탐색에서 탐색 실패가 결정되는 위치가 삽입 위치가 됨
  
  - 탐색 실패한 위치에 원소 삽입
  
  - 5 삽입
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-05-09-40-46-image.png" title="" alt="" data-align="center">

- 탐색, 삽입, 삭제 시간은 트리의 높이만큼 시간이 걸림
  
  - O(h), h : BST의 깊이(height) 

- 평균의 경우
  
  - 이진 트리가 균형적으로 생성되어 있는 경우
  
  - O(log n)

- 최악의 경우
  
  - 한쪽으로 치우친 경사 이진트리의 경우
  
  - O(n)
  
  - 순차탐색과 시간복잡도가 같음

- 검색 알고리즘의 비교
  
  - 배열에서의 순차 검색 : O(N)
  
  - 정렬된 배열에서의 순차 검색 : O(N)
  
  - 정렬된 배열에서의 이진 탐색 : O(logN)
    
    -  고정 배열 크기와 삽입, 삭제 시 추가 연산 필요
  
  - 이진 탐색 트리에서의 평균 : O(logN)
    
    - 최악의 경우 : O(N)
    
    - 완전 이진 트리 또는 균형 트리로 바꿀 수 있다면 최악의 경우 없앨 수 있음
      
      - 새로운 원소 삽입할 때 삽입 시간 줄임
      
      - 평균과 최악의 시간이 같음.O(logN)
  
  - 해쉬 검색 : O(1)
    
    - 추가 저장 공간 필요

- **삭제연산**
  
  - 예시
  
  - 13, 12, 9 차례로 삭제해보기
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-05-09-44-40-image.png" title="" alt="" data-align="center">
