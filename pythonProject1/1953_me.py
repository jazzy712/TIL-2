from collections import deque


def catch_fugitive(R, C):
    q = deque([(R, C)])
    # 현재 노드 방문처리
    visited[R][C] = 1
    # 위치 가능한 장소 개수(현재 위치 포함)
    cnt = 1
    # 큐가 빌 때 까지
    while q:
        # 현재 노드의 가로,세로 위치 값 꺼내기
        N_R, N_C = q.popleft()
        # 시간당 거리 1 움직일 수 있다 했으므로 방문처리 수 만큼 시간이 지남
        # 소요된 시간이 L에 이르면 탐색 종료
        if visited[N_R][N_C] == L:
            continue
        # 터널 구조물 타입에 따라 이동 가능한 방향 달라짐
        for dr,dc in types[tunnel_map[N_R][N_C]]:
            # 이동한 위치 값
            nr = N_R + dr
            nc = N_C + dc
            # 벽 세우기
            if 0 <= nr < N and 0 <= nc < M:
                # 0이면 지나갈 수 없음
                if tunnel_map[nr][nc] != 0:
                    # 해당 부분 작성안했더니 테스트케이스 오류가 계속 남
                    # 현재 위치에서 터널 구조물로 이동했을 때 다음 위치에서도
                    # 터널 구조물이 이전 구조물과 연결되어 있는지 확인해야됨
                    if (-dr, -dc) in types[tunnel_map[nr][nc]]:
                        # 방문 하지 않은 곳 이면
                        if visited[nr][nc] == 0:
                            # 현재까지의 시간이 L보다 적으면
                            if visited[N_R][N_C] < L:
                                # 다음 위치 큐에 담고
                                q.append((nr,nc))
                                # 시간 1 늘어남
                                visited[nr][nc] = visited[N_R][N_C] + 1
                                # 카운트 추가
                                cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    # 지하 터널 지도 정보 저장할 배열 생성
    tunnel_map = [list(map(int, input().split())) for _ in range(N)]
    # 지나온 칸 방문여부 체크 생성
    visited = [[0] * M for _ in range(N)]
    # 배열에서 델타 이동 할 예정
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 문제에 제시된 터널 구조물 타입 방향 할당
    types = {
        1: [(-1, 0), (1, 0), (0, -1), (0, 1)],
        2: [(-1, 0), (1, 0)],
        3: [(0, -1), (0, 1)],
        4: [(-1, 0), (0, 1)],
        5: [(1, 0), (0, 1)],
        6: [(1, 0), (0, -1)],
        7: [(-1, 0), (0, -1)]
    }

    res = catch_fugitive(R, C)

    print(f'#{tc} {res}')
