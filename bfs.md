## BFS

- 너비 우선 탐색(BFS)
  
  - 탐색 시작점의 인접한 정점들을 먼저 모두 차례로 방문한 후에, 방문했던 정점을 시작점으로 하여 다시 인접한 정점들을 차례로 방문
  
  - 인접한 정점들에 대해 탐색을 한 후, 차례로 다시 너비우선탐색을 진행해야 하므로, **선입선출** 형태의 자료구조인 큐를 활용
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-04-29-image.png" title="" alt="" data-align="center">
  
  ```python
  def BFS(G, v):                          # G : 그래프, v : 탐색 시작점
      visited = [0] * (n + 1)             # n :  정점 개수
      queue = []                          # 큐 생성
      queue.append(v)                     # 시작점 v를 큐에 삽입
      while queue:                        # 큐가 비어있지 않은 경우
          t = queue.pop(0)                # 큐의 첫번째 원소 반환
          if not visited[t]:              # 방문하지 않은 곳이라면
              visited[t] = True           # 방문한 것으로 표시
              visit(t)                    # 정점 t에서 할 일
              for i in G[t]:              # t와 연결된 모든 정점에 대해
                  if not visited[i]:      # 방문하지 않은 곳이라면
                      queue.append(i)     # 큐에 넣기
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-14-52-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-15-05-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-15-18-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-15-33-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-15-47-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-15-59-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-16-10-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-16-21-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-16-33-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-16-44-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-16-57-image.png" title="" alt="" data-align="center">

- BFS 예제
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-20-09-28-47-image.png" title="" alt="" data-align="center">
  
  ```python
  def BFS(G, v, n):                        # G : 그래프, v : 탐색 시작점
      visited = [0] * (n + 1)              # n :  정점 개수
      queue = []                           # 큐 생성
      queue.append(v)                      # 시작점 v를 큐에 삽입
      visited[v] = 1
      while queue:                         # 큐가 비어있지 않은 경우
          t = queue.pop(0)                 # 큐의 첫번째 원소 반환
          visit(t)
          for i in G[t]:                   # t와 연결된 모든 정점에 대해
              if not visited[i]:           # 방문하지 않은 곳이라면
                  queue.append(i)              # 큐에 넣기
                  visited[i] = visited[t] + 1  # n 으로부터 1만큼 이동
  ```
