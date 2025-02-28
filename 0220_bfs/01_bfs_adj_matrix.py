import sys
from pprint import pprint

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접 행렬 생성
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]
pprint(adj_matrix)
# 간선 정보를 바탕으로 인접 행렬에 기록(무방향 그래프)
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

pprint(adj_matrix)

def BFS_matrix(start):
    # 방문 여부를 표기할 리스트
    visited = [0] * (V + 1)
    # 큐 초기화
    q = []

    # enqueue
    # 방문처리 -> 큐에 삽입
    # '큐에 넣었다' 는 것은 '이 노드를 이미 발견, 방문해서 다음에 처리할 예정이다'
    visited[start] = 1
    q.append(start)

    # 큐가 빌 때까지 진행
    while q:
        # dequeue
        current_node = q.pop(0)
        print(current_node, end=' ')

        # 현재 노드에서 인접한 노드를 탐색
        for next_node in range(1, V + 1):
        # 인접해있어야 하고 and 아직 방문을 하지 않았다면(인큐 조건)
            if adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0:
                # 방문 처리
                visited[next_node] = 1
                # 다음 노드를 큐에 넣음
                q.append(next_node)
# BFS 실행
BFS_matrix(1)
