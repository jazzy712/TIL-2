# import sys
# sys.stdin = open('input.txt')

def hex_to_binary(hex_str):
    # 변환할 2진수
    bin_str = ''
    for char in hex_str:
        # 16진수 문자열 10진수로 변환
        decimal_num = int(char, 16)
        # 변환한 10진수 문자열 2진수로 변환
        bin_str += format(decimal_num, '04b')
    return bin_str


T = int(input())
for tc in range(1, T+1):
    N, hex_str = map(str, input().split())

    res = hex_to_binary(hex_str)
    print(f'#{tc} {res}')
