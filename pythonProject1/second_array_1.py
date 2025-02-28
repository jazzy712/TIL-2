'''
- 문제 시나리오
    - 5×5 크기의 2차원 평면이 있고, 시작점은 `(0, 0)`이라고 하자.
    - 방향 문자열(`N, S, E, W`)이 주어지면 그 방향으로 1칸씩 이동한다.
    - 이동 중 평면을 벗어나는 입력은 주어지지 않는다고 가정한다.
    - 최종적으로 이동이 끝난 뒤의 위치 `(r, c)`를 출력한다.
'''
def move_with_nav(commands):
    r,c = 0, 0                      # 시작점 (0, 0)
    dr = [-1, 1, 0, 0]              # N, S, E, W
    dc = [0, 0, 1, -1]
    dir = ['N', 'S', 'E', 'W']      # 방향 문자열 리스트

    for cmd in commands:
        for i in range(4):
            if cmd == dir[i]:       # i번째 이동 했을 떼 위치 값 구하기
                nr = r + dr[i]      # 이동 후 행
                nc = c + dc[i]      # 이동 후 열
                r,c = nr, nc        # 이동 후 행,열의 값으로 위치
    return r,c


# 테스트
commands = ['E', 'E', 'S', 'W', 'N']
end_r, end_c = move_with_nav(commands)
print(end_r, end_c)  # 0 1
