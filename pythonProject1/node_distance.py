T = int(input())
for tc in range(1, T +1):
    # V : 노드 개수, E : 간선 개수
    V, E = map(int, input().split())
    # 인접 리스트 생성
    adj_l = [[] for _ in range(V + 1)]
    # 간선 정보 인접 리스트에 저장(무방향!)
    for i in range(E):
        # 무방향이므로 양쪽 노드 모두 추가
        n1, n2 = map(int, input().split())
        adj_l[n1].append(n2)
        adj_l[n2].append(n1)
    # S : 출발 노드, G : 도착 노드
    S, G = map(int, input().split())


    def node_dis(S, G):
        # visited 리스트 생성
        # 깊이의 정보도 담고있다
        # 미방문 상태를 -1로 나타냄
        visited = [-1] * (V + 1)
        # queue 생성
        Q = [S]

        # enqueue(방문처리)
        # 시작점까지의 거리는 0
        visited[S] = 0

        # 큐가 빌 때까지 반복
        while Q:
            # 현재 노드 dequeue
            c_node = Q.pop(0)
            # 현재 노드와 인접한 노드 탐색
            for next_node in adj_l[c_node]:
                # 목적지 G를 만나면
                if next_node == G:
                    # 바로 현재 노드까지의 깊이 +1(방문처리) 반환
                    return visited[c_node] + 1
                # 다음 노드를 방문하지 않았다면
                if visited[next_node] == -1:
                    # 방문 처리
                    # 다음 노드까지의 거리 = 현재 노드까지의 거리 + 1
                    visited[next_node] = visited[c_node] + 1
                    # 큐에 삽입
                    Q.append(next_node)

        # 도착할 수 없다면 0 반환
        return 0

    print(f'#{tc} {node_dis(S, G)}')