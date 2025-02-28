T = int(input())                                        # 테스트 케이스 갯수

for tc in range(1, T+1):
    N= int(input())                                     # 각 테스트 케이스
    arr = [[0] * N for _ in range(N)]                   # NxN 크기의 0으로 채워진 매트릭스 생성
    r, c = 0, 0                                         # 시작 위치 (0,0)
    dr = [0, 1, 0, -1]                                  # 행의 시계 방향 이동값
    dc = [1, 0, -1, 0]                                  # 열의 시계 방향(E,S,W,N) 이동값
    r_start = 0                                         # 행 시작점
    r_end = N - 1                                       # 행 끝점
    c_start = 0                                         # 열 시작점
    c_end = N - 1                                       # 열 끝점
    num = 1                                             # 채워넣을 숫자를 1부터 시작

    while r_start <= r_end and c_start <= c_end:        # 칸의 경계값이 서로 교차하기 전까지 반복

        for i in range(c_start, c_end + 1):
            arr[r_start][i] = num
            num += 1                                    # 왼쪽 -> 오른쪽
        r_start += 1                                    # 끝에 다다르면 위쪽 행 경계를 한 칸 내림


        for i in range(r_start, r_end + 1):
            arr[i][c_end] = num
            num += 1                                    # 위쪽 -> 아래쪽
        c_end -= 1                                      # 끝에 다다르면 오른쪽 열 경계 한 칸 왼쪽으로


        if r_start <= r_end:                            # 행의 시작점이 끝점보다 작거나 같을 때
            for i in range(c_end, c_start-1, -1):
                arr[r_end][i] = num
                num += 1                                # 오른쪽 -> 왼쪽
            r_end -= 1                                  # 끝에 다다르면 아래쪽 행 경계 한 칸 올림


        if c_start <= c_end:                            # 열의 시작점이 끝점보다 작거나 같을 때
            for i in range(r_end, r_start-1, -1):
                arr[i][c_start] = num
                num += 1                                # 아래쪽 -> 위쪽
            c_start += 1                                # 끝에 다다르면 왼쪽 열 경계 한 칸 오른쪽으로


    print(f'#{tc}')                                     # 테스크 케이스 번호 출력
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')                   # 한 행의 숫자들 공백으로 구분
        print()                                         # 줄 바꿈

