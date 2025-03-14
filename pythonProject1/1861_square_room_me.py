from collections import deque

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [list(map(int, input().split())) for _ in range(N)]

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 최대 이동 방 개수
    max_room = 0
    # 가장 많은 개수의 방을 이동해야 하므로 처음 값이 작아야함
    # 처음 방의 숫자 초기화
    start_room = 0

    # 모든 행과 열 탐색
    for r in range(N):
        for c in range(N):
            # 방문여부 배열과 큐 생성
            visited = [[0] * N for _ in range(N)]
            q = deque([(r, c)])
            visited[r][c] = 1
            # 이동한 방의 개수
            cnt = 1
            # 큐가 빌 때까지 반복
            while q:
                c_r, c_c = q.popleft()
                # 상하좌우 이동
                for i in range(4):
                    nr = c_r + dr[i]
                    nc = c_c + dc[i]
                    # 벽 세우고 방문하지 않았다면
                    if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                        # 다음 칸은 현재 칸에서 거리가 1이면
                        if room[nr][nc] == room[c_r][c_c] + 1:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
                            cnt += 1
            # 최대 이동 방 개수 갱신
            if cnt > max_room:
                max_room = cnt
                # 초기 숫자 갱신
                start_room = room[r][c]
            # 최대 이동 방 개수 똑같아도
            # 더 작은 초기 값이 있을 수도 있음
            elif cnt == max_room and room[r][c] < start_room:
                start_room = room[r][c]

    print(f'#{tc} {start_room} {max_room}')




