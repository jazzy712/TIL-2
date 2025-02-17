T = 10                                                                  # 주어진 10개의 테스트 케이스

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]         # 100x100 크기의 2차원 배열 생성

    dr = [0, 0, -1]                                                     # 도착점에서 역으로 출발점으로 올라가는 방향
    dc = [-1, 1, 0]                                                     # 좌,우,상

    r = 99
    c = arr[99].index(2)
    while r > 0:
        # 왼쪽 확인
        if c > 0 and arr[r][c - 1] == 1:
            while c > 0 and arr[r][c - 1] == 1:
                c -= 1
            r -= 1
        # 오른쪽 확인
        elif c < 99 and arr[r][c + 1] == 1:
            while c < 99 and arr[r][c + 1] == 1:
                c += 1
            r -= 1
        # 위로 이동
        else:
            r -= 1
    print(f'#{tc} {c}')










