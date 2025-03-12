def dfs(start):
    stack = [start]
    visited = [0] * (V + 1)
    while stack:
        current_node = stack.pop()
        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end='')
            for next_node in range(V, 0, -1):
                if matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                    stack.append(next_node)


V, E = map(int, input().split())
info = list(map(int, input().split()))
matrix = [[0] * (V + 1) for _ in range(V + 1)]
for i in range(E):
    ni, nj = info[i * 2], info[i * 2 + 1]
    matrix[ni][nj] = 1
    matrix[nj][ni] = 1

dfs(1)
