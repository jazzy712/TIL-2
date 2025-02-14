import sys
from pprint import pprint

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 빈 인접 리스트 생성
adj_list = [[] for _ in range(V + 1)]
# pprint(adj_list)

# 간선 정보(data)를 기반으로 인접 리스트에 간선 정보를 입력
for i in range(E):
    n1 = data[i * 2]
    n2 = data[i * 2 + 1]
    adj_list[n1].append(n2)
    adj_list[n2].append(n1)

# pprint(adj_list)

# 방문 순서를 결정하기 위해 인접 리스트 내부의 간 간선 정보를 내림차순으로 정렬
# 내림차순이면, 스택에서 pop 할때 작은 번호를 먼저 방문할 수 있기 때문
for i in range(1, V + 1):
    # 내림차순 : sort(reverse=True)
    adj_list[i].sort(reverse=True)

# pprint(adj_list)

def DFS_stack_adj_list(start):
    '''
    스택을 활용한 DFS - 인접 리스트 버전

    - start: 탐색을 시작할 노드 번호
    - adj_list: 각 노드별 연결된 노드 목록 (내림차순 정렬 상태)
    - visited: 노드 방문 여부를 기록하는 리스트
    '''
    # 시작 노드를 스택에 넣음 / 방문 기록지 생성
    stack = [start]
    visited = [0] * (V + 1)

    # 스택이 빌 때까지
    while stack:
        current_node = stack.pop()
        if visited[current_node] == 0:
            visited[current_node] = 1
            print(current_node, end='')

            # 다음 가야 할 곳을 탐색
            # 현재 노드의 인접 노드들을 스택에 push
            # 그런데 이미 인접 리스트가 내림차순 정렬되어 있으므로
            # 그대로 순회하면 작은 번호가 스택 top에 올라가 있어서 먼저 방문 가능함
            for next_node in adj_list[current_node]:
                if visited[next_node] == 0:
                    stack.append(next_node)



# 실제 DFS 실행 (예: 시작 노드 1)
DFS_stack_adj_list(1)
