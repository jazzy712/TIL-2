## BackTracking

- 백트래킹
  
  - 해를 찾는 도중에 '막히면'(즉, 해가 아니면) 되돌아가서 다시 해를 찾아 가는 기법
  
  - 최적화 문제와 결정 문제 해결 가능
  
  - 결정 문제 : 문제의 조건을 만족하는 해가 존재하는지의 여부를 'yes' 또는 'no'가 답하는 문제
    
    - 미로 찾기
    
    - n-Queen 문제
    
    - Map coloring
    
    - 부분 집합의 합(Subset sum)
  
  - 깊이 우선 탐색과의 차이
    
    - 어떤 노드에서 출발하는 경로가 해결책으로 이어질 것 같지 않으면 더 이상 그 경로를 따라가지 않음으로써 시도의 횟수를 줄임(Prunning 가지치기)
    
    - 깊이 우선 탐색이 모든 경로를 추적하는데 비해 백트래킹은 불필요한 경로를 조기에 차단
    
    - 깊이 우선 탐색을 가하기에는 경우의 수가 너무 많음, 즉 N! 가지의 경우의 수를 가진 문제에 대해 깊이 우선 탐색을 가하면 당연히 처리 불가능한 문제
    
    - 백트래킹 알고리즘을 적용하면 일방적으로  경우의 수가 줄어들지만 역시 최악의 경우에는 여전히 지수함수 시간(Exponential Time)을 요하므로 처리 불가능
  
  - 어떤 노드의 유망성을 점검 후에 유망(promising) 하지 않다고 결정되면 그 노드의 부모로 되돌아가(backtracking) 다음 자식 노드로 감
  
  - 어떤 노드를 방문하였을 때 그 노드를 포함한 경로가 해답이 될 수 없으면 그 노드는 유망하지 않다고 하며, 반대로 해답의 가능성이 있으면 유망하다고 함
  
  - 가지치기(pruning) : 유망하지 않는 노드가 포함되는 경로는 더 이상 고려하지 않음
  
  - 1. 상태 공간 트리의 깊이 우선 검색 실시
    
    2. 각 노드가 유망한지 점검
    
    3. 만일 그 노드가 유망하지 않으면, 그 노드의 부모 노드로 돌아가서 검색 계속
  
  - 미로 찾기
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-27-35-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-27-55-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-28-08-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-28-22-image.png" title="" alt="" data-align="center">
  
  ```py
  def checknode(v):
      if promising(v):
          if there is a solution at v:
              write the solution
          else:
              for u in each child of v:
                  checknode(u)
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-29-54-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-30-05-image.png" title="" alt="" data-align="center">
  
  - 상태 공간 트리
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-17-15-30-26-image.png)
