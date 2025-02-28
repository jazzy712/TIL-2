def find_goal(maze):
    # 16x16 미로 탐색
    for i in range(16):
        for j in range(16):
            # 출발점 찾기
            if maze[i][j] == 2:
                start_r = i
                start_c = j
                


T = 10
for tc in range(1, T+1):
    # 16x16 크기 미로 생성
    maze = [list(map(int, input())) for _ in range(16)]
    
