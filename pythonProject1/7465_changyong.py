from collections import deque


def bfs(N, neighbor):
    # 무리 수 초기화
    group = 0
    # 체크 여부 리스트 생성
    check = [0] * (N + 1)
    # 마을 전체 인원 N 명 중에서 순회
    for i in range(1, N+1):
        if check[i] == 0:
            q = deque([i])
            check[i] = 1

            while q:
                # 현재 사람 큐에서 pop
                cur_p = q.popleft()
                # 지인 리스트에서 현재 사람과 알고 있는 다음 사람 탐색
                for next_p in neighbor[cur_p]:
                    if check[next_p] == 0:
                        check[next_p] = 1
                        q.append(next_p)
            group += 1
    return group


T = int(input())

for tc in range(1, T+1):
    # 창용 마을 인구 N, 서로 알고 있는 사람 수 M
    N, M = map(int, input().split())
    # 서로 알고 있는(연결된) 사람들 저장
    neighbor = [[] for _ in range(N + 1)]

    for _ in range(M):
        ni, nj = map(int, input().split())
        # ni 와 nj 는 서로 알고 있음
        neighbor[ni].append(nj)
        neighbor[nj].append(ni)

    result = bfs(N, neighbor)
    print(f'#{tc} {result}')


