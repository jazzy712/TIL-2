## DFS(깊이 우선탐색)

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
