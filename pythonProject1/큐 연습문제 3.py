def bfs(start):
    q = [start]
    visited = [0] * (V + 1)
    visited[start] = 1
    while q:
        current_node = q.pop(0)
        print(current_node, end=' ')

        for next_node in adj_list[current_node]:
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)


V, E = map(int, input().split())
info = list(map(int, input().split()))
adj_list = [[] for _ in range(V + 1)]
for i in range(E):
    ni, nj = info[i * 2], info[i * 2 + 1]
    adj_list[ni].append(nj)
    adj_list[nj].append(ni)


bfs(1)