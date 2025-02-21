import sys
from pprint import pprint
sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 리스트 생성
adj_list = [[] for _ in range(V + 1)]
pprint(adj_list)
# 간선 정보를 바탕으로 인접 리스트에 기록(무방향)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)
pprint(adj_list)

# 방문 시 작은 번호부터 접근하기 위해 각 간선정보 리스트를 오름차순 정렬
for i in range(1, V + 1):
    adj_list[i].sort()
pprint(adj_list)

def BFS_list(start):
    visited = [0] * (V + 1)
    q = []

    # enqueue(방문처리 후 삽입)
    visited[start] = 1
    q.append(start)

    while q:
        # dequeue
        current_node = q.pop(0)
        print(current_node, end=' ')

        # current_node 와 인접한 노드 탐색
        for next_node in adj_list[current_node]:
            # 방문하지 않았다면 -> 방문 후 큐에 삽입(enqueue)
            if visited[next_node] == 0:
                visited[next_node] = 1
                q.append(next_node)


# BFS 실행
BFS_list(1)
