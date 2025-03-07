import sys
sys.stdin = open("input.txt")

def ladder(ladder_map):
    min_cnt = 10000
    pos_x = -1

    for start_c in range(100):
        if ladder_map[0][start_c] == 1:
            r, c = 0, start_c
            cnt = 0
            visited = [[0] * 100 for _ in range(100)]
            visited[r][c] = 1

            while r < 99:
                if c > 0 and ladder_map[r][c - 1] == 1 and not visited[r][c - 1]:
                    c -= 1
                elif c < 99 and ladder_map[r][c + 1] == 1 and not visited[r][c + 1]:
                    c += 1
                else:
                    r += 1

                visited[r][c] = 1
                cnt += 1

            if cnt <= min_cnt:
                min_cnt = cnt
                pos_x = start_c

    return pos_x


T = 10
for tc in range(1, T + 1):
    _ = input()  # 테스트 케이스 번호 입력 (사용하지 않음)
    ladder_map = [list(map(int, input().split())) for _ in range(100)]
    res = ladder(ladder_map)
    print(f'#{tc} {res}')
