def maze_dis(start_r, start_c):
    # 깊이 정보도 담고 있는 방문 여부 행렬 생성
    # 방문하지 않은 상태를 -1로 나타냄
    visited = [[-1] * N for _ in range(N)]
    # 큐 생성
    q = [(start_r, start_c)]
    # 시작점 방문 표시
    # 시작점으로부터의 깊이(거리)가 0
    visited[start_r][start_c] = 0
    # 상.하.좌.우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 큐가 빌 때까지 반복
    while q:
        # 현재 위치 dequeue
        c_r, c_c = q.pop(0)
        # 4방향 탐색
        for i in range(4):
            # 다음 위치 계산
            nr = c_r + dr[i]
            nc = c_c + dc[i]
            # 벽을 세우고
            if 0 <= nr < N and 0 <= nc < N:
                # 도착 지점을 찾으면
                if maze[nr][nc] == 3:
                    # 현재까지의 깊이(거리) 반환
                    return visited[c_r][c_c]
                # 다음 노드를 방문하지 않았고 다음 노드가 통로(0)라면
                if visited[nr][nc] == -1 and maze[nr][nc] == 0:
                    # 다음 위치의 깊이(거리) = 현재 위치의 깊이(거리) + 1
                    # 누적하면서 거리를 계산
                    visited[nr][nc] = visited[c_r][c_c] + 1
                    # 인큐
                    q.append((nr, nc))
    # 갈 수 없는 경우 0 반환
    return 0


T = int(input())
for tc in range(1, T+1):
    # 미로의 크기 N
    N = int(input())
    # NxN 크기의 미로
    maze = [list(map(int, input())) for _ in range(N)]
    # 출발 좌표 최초값 0
    start_r, start_c = 0, 0
    # NxN 크기의 미로에서
    for r in range(N):
        for c in range(N):
            # 2는 출발
            if maze[r][c] == 2:
                # 출발점 좌표 할당
                start_r, start_c = r, c
                # 좌표 찾았으니 끝
                break

    print(f'#{tc} {maze_dis(start_r, start_c)}')



