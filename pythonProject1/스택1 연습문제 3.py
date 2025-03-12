def dfs(start):
    # 시작점 넣은채로 스택 생성
    stack = [start]
    while stack:
        current_node = stack.pop()
        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end='')
            for next_node in range(V, 0, -1):
                if matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                    visited[next_node] = 1
                    stack.append(next_node)


V, E = map(int, input().split())
# 노드와 간선 정보 입력할 리스트
info = list(map(int, input().split()))
# 2차원 배열 생성
matrix = [[0] * (V+1) for _ in range(V+1)]
# 방문 여부 리스트 생성
visited = [0] * (V + 1)
# 간선 정보를 인접 행렬에 입력
for i in range(E):
    ni, nj = info[i * 2], info[i * 2 + 1]
    matrix[ni][nj] = 1
    matrix[nj][ni] = 1

dfs(1)