def bit_pattern(arr):
    password = {
         '001101': 0,
         '010011': 1,
         '111011': 2,
         '110001': 3,
         '100011': 4,
         '110111': 5,
         '001011': 6,
         '111101': 7,
         '011001': 8,
         '101111': 9
    }
    # 변환할 2진수
    bin_str = ''
    for char in arr:
        # 10진수로 변환
        dec_num = int(char, 16)
        # 2진수로 변환
        bin_str += format(dec_num, '04b')

    # 결과 저장할 리스트
    result = []
    # 인덱스 0부터
    i = 0
    # 패턴이 6자리이므로 마지막 인덱스가 최소 5가 될 때까지 확인
    while i <= len(bin_str) - 6:
        # 6자리씩 잘라서 확인
        pattern = bin_str[i:i+6]
        # 패턴이 암호비트패턴에 있으면
        if pattern in password:
            # 결과 리스트에 추가
            result.append(password[pattern])
            # 6자리 패턴 확인했으므로 6칸 이동
            i += 6
        # 패턴을 못찾으면
        else:
            # 1칸씩 확인
            i += 1
    return ' '.join(map(str, result))


T = int(input())
for tc in range(1, T+1):
    # 입력받을 배열
    arr = input()
    ans = bit_pattern(arr)
    print(f'#{tc} {ans}')