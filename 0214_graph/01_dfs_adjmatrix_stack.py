import sys
from pprint import pprint

sys.stdin = open('input.txt')

# 정점의 개수(7) / 간선의 개수(8) 저장
V, E = map(int, input().split())
# 간선 정보 저장
data = list(map(int, input().split()))

# 빈 인접행렬 만들기 (V+1 * V+1)
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

pprint(adj_matrix)

# 만든 인접행렬에 간선 정보 입력
# 간선이 8개이기 때문에 간선의 개수만큼 반복
for i in range(E):
    # 형식 암기 !!
    # 간선 정보를 기반으로 인접행렬에 간선 정보 표기
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

pprint(adj_matrix)

def DFS_stack(start):
    '''
    스택을 활용한 DFS

    - start: 시작 노드 번호
    - visited: 방문 여부 확인용 리스트
    - adj_matrix: 인접 행렬 (n1, n2 사이가 연결되면 값 = 1)
    '''
    # 스택에 시작 노드를 삽입 (초기화)
    stack = [start]
    # 각 정점에 방문 여부를 확인할 리스트 
    # 0번은 안쓰기 때문에 길이는 V+1 
    visited = [0] * (V + 1)

    # 탐색 시작
    while stack:    # while len(stack) != 0:
        # 스택의 마지막 원소를 꺼냄
        current_node = stack.pop()

        # 방문하기 전에 지금 현재 위치 정점에 방문하지 않았다면,
        if visited[current_node] == 0:
            # 방문 처리
            visited[current_node] = 1
            print(current_node, end='')

            # 다음에 갈 곳은 어디인가?
            # 현재 노드와 인접한 노드가 누구인지 matrix에서 검색
            # V부터 1까지 역순으로 확인(작은 번호의 노드가 스택의 위쪽에 위치할 수 있기 때문)
            for next_node in range(V, 0, -1):
                # 앞으로 가야할 곳(간선이 있는 곳)을 스택에 넣기 전에, 과거에 들렸던 곳인지 확인해야 함
                if (adj_matrix[current_node][next_node] == 1 and visited[next_node] == 0):
                    stack.append(next_node)

# 실제 DFS 실행
DFS_stack(1)
