import sys
sys.stdin = open('input.txt')
def reverse_string(arr):
    # 회문 길이는 최대 100까지 늘어남, 최댓값을 구하고자 하므로 100에서 역순으로 진행
    for str_len in range(100, 1, -1):
        # 가로 행 회문 찾기
        for r in range(100):
            # 시작 값
            for c in range(100 - str_len + 1):
                word = [arr[r][c+x] for x in range(str_len)]
                if word == word[::-1]:
                    return str_len

        for r_c in range(100):
            # 시작 값
            for c_c in range(100 - str_len + 1):
                word = [arr[c_c+y][r_c] for y in range(str_len)]
                if word == word[::-1]:
                    return str_len
    return 1

T = 10

for tc in range(1, T+1):
    test_case = int(input())
    # 회문 길이 str_len 의 최솟값 설정
    str_len = 1
    # 100x100 크기의 2차원 배열 생성
    arr = [list(map(str, input())) for _ in range(100)]

    max_str_len = max(str_len, reverse_string(arr))

    print(f'#{test_case} {max_str_len}')








