'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7
'''

def dfs(v, N):                                 # v 출발, N 마지막 정점
    visited = [0] * (N + 1)                    # visited : 각 정점의 방문 여부를 표시할 리스트(0: 미방문, 1 : 방문)
    stack = []                                 # stack : DFS 실행 시 정점들을 저장할 스택

    while True:
        if visited[v] == 0:                    # 현재 정점 첫 방문이면
            visited[v] = 1                     # 방문 표시
            print(v)                           # 방문한 정점 출력

        for w in adj_list[v]:                  # v에 인접한 모든 정점(w) 확인
            if visited[w] == 0:                # 인접한 정점 중 방문하지 않은 정점이 있다면
                stack.append(v)                # 현재 정점 스택에 push
                v = w                          # 다음 정점인 w로 이동
                break                          # for 루프 종료
        else:
            if stack:                          # 인접한 정점 모두 방문했다면
                v = stack.pop()                # 스택에서 이전 정점 꺼내서 돌아감
            else:
                break                          # 스택이 비어있다면 모든 탐색 끝났으므로 종료


V, E = map(int, input().split())               # V : 점 갯수, E : 간선 갯수
graph = list(map(int, input().split()))        # graph : 간선 정보 담은 리스트 입력
adj_list = [[] for _ in range(V+1)]            # 각 정점별 인접한 장점들을 저장할 리스트

for i in range(E):                             # 입력받은 간선 정보를 인접 리스트 형태로 변환
    v, w = graph[i*2], graph[i*2+1]            # v : 시작 정점, w : 도착 정점

    adj_list[v].append(w)                      # 무방향 그래프이므로 양쪽 정점에 서로 추가
    adj_list[w].append(v)
