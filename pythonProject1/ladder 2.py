T = 10

for tc in range(1, T+1):
    # 100x100 2차원 배열 생성
    arr = [list(map(int, input().split())) for _ in range(100)]
    N = len(arr)
    # 우,좌,하 방향(아래 방향으로만 이동한다 했으므로 위쪽 탐색 x)
    dr = [1, -1, 0]
    dc = [0, 0, 1]

    # 도착점의 좌표
    end_r = i
    end_c = 99

    # 막대 길이의 최초 값 설정
    ladder_len = 0

    for r in range(i):
        for c in range(N):
            # 도착점의 인덱스 값은 1
            if arr[r][c] == 1:
                # 3 방향 탐색(우,좌,하)
                for i in range(3):
                    nr = r + dr[i]
                    nc = c + dc[i]



