import sys

sys.stdin = open('input2.txt')


def dfs_adjlist_another_input(V, E):
    '''
    스택을 활용한 DFS (인접 리스트 & 다른 input 형태)
    - 정점이 0부터 (V-1)까지 번호를 갖지만,
      실제 출력 시에는 각 노드에 +1을 하여 1~V 범위로 출력.
    - 예) 노드 0 -> 출력 "1", 노드 1 -> 출력 "2", ...
    '''
    # 인접 리스트 생성
    adj_list = [[] for _ in range(V)]

    # 간선 정보 (양방향)
    for _ in range(E):
        n1, n2 = map(int, sys.stdin.readline().split())
        adj_list[n1].append(n2)
        adj_list[n2].append(n1)

    # 작은 번호 노드를 우선 방문하기 위해, 인접 리스트를 '내림차순' 정렬
    # => 스택에 push 시 작은 노드가 먼저 pop되도록
    for i in range(V):
        adj_list[i].sort(reverse=True)

    stack = [0]  # 시작 노드(0)로 설정
    visited = [0] * V
    result = []  # 방문 순서 기록

    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = 1
            # 여기서 current+1을 출력(문자열로)
            result.append(str(current + 1))  # 숫자 -> 문자열로 변환

            # 인접 노드들을 스택에 push (아직 방문 안 한 노드만)
            for nxt in adj_list[current]:
                if not visited[nxt]:
                    stack.append(nxt)

    # 방문 순서를 이어붙여 문자열로 반환
    return ''.join(result)


# -------------------------------
V = int(input().strip())  # 정점 개수
E = int(input().strip())  # 간선 개수

# DFS 실행
dfs_result = dfs_adjlist_another_input(V, E)
print(dfs_result)
