def find_goal(start_r, start_c):




T = 10
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input().split())) for _ in range(16)]
    # 출발 좌표 최초값 0
    start_r, start_c = 0, 0
    # 16x16 크기의 미로에서
    for r in range(16):
        for c in range(16):
            # 2는 출발
            if maze[r][c] == 2:
                # 출발점 좌표 할당
                start_r, start_c = r, c
                # 좌표 찾았으니 끝
                break
