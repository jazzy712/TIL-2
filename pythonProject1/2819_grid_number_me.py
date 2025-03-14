# 가로 값과 세로 값, 그리고 할당된 숫자
def number_push(r, c, num):
    # 상하좌우
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    # 숫자가 7개가 되면 결과 집합에 추가하고 return
    if len(num) == 7:
        result.add(num)
        return
    # 델타 이동
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # 벽 세우기
        if 0 <= nr < 4 and 0 <= nc < 4:
            # 계속 숫자 붙임
            number_push(nr, nc, num + grid[nr][nc])


T = int(input())
for tc in range(1, T+1):
    grid = [input().split() for _ in range(4)]
    # 출력할 결과 집합
    result = set()

    # 격자 내에서 함수 실행
    for r in range(4):
        for c in range(4):
            number_push(r,c, grid[r][c])

    print(f'#{tc} {len(result)}')

