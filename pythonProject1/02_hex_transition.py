# 16진수를 2진수로 바꾸기
def hex_to_binary(hex_str):
    # 바꿀 2진수
    bin_str = ''
    for char in hex_str:
        # 먼저 16진수를 10진수로 바꾸기
        dec_num = int(char, 16)
        bin_str += format(dec_num, '04b')
    return bin_str


# 바꾼 2진수를 7bit 씩 묶어 다시 10진수로 바꾸기
def bin_to_decimal(bin_str):
    # 결과 담을 리스트
    result = []
    # 7bit 씩 자른 묶음
    chunk = ''
    # 바꾼 2진수 순회
    for bit in bin_str:
        # 묶음에 bit 추가
        chunk += bit
        # 묶음 길이가 7이 되고
        if len(chunk) == 7:
            # 자른 7bit 가 '0000000' 인 경우
            if chunk == '0000000':
                # 앞 0 4개 버림
                chunk = chunk[4:]
            # 아닌 경우
            else:
                # 10진수 변환
                dec_str = int(chunk, 2)
                result.append(dec_str)
                # chunk 초기화
                chunk = ''
    # 남은 chunk 가 있다면
    if chunk:
        # chunk 길이가 7이 되도록 0 추가
        while len(chunk) < 7:
            chunk = '0' + chunk
        dec_str = int(chunk, 2)
        result.append(dec_str)

    return ' '.join(map(str, result))


T = int(input())
for tc in range(1, T+1):
    # 입력받을 16진수
    hex_str = input()
    bin_str = hex_to_binary(hex_str)
    ans = bin_to_decimal(bin_str)
    print(f'#{tc} {ans}')

