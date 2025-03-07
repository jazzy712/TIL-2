# 10진수 -> 2진수(최대 소수 12자리까지)
# 10진수 소수를 2진수로 변환하려면 소수 아래 자리는 2^-1, 2^-2 이런 식이기 때문에
# 2진수로 변환하려면 2를 곱하고 왼쪽으로 한칸씩 땡겨옴
# 이 때, 정수 부분의 값이 해당 소수점 자리의 2진수 값이 됨
def dec_to_binary(N):
    # 변환한 2진수 값 저장
    bin_num = ''
    # 소수점 아래 12자리까지 계산
    for _ in range(12):
        # N을 2배 했을 때
        N = N * 2
        # N이 1 이상이라면
        if N >= 1:
            # 2진수 값에 1 추가하고 1 빼기(정수 부분은 제외)
            bin_num += '1'
            N -= 1
        # 1을 넘지 않는다면
        else:
            # 2진수 값에 0 추가
            bin_num += '0'
        # N이 0이 되면
        if N == 0:
            # 현재까지의 2진수 반환
            return bin_num
    # 12자리 계산 후 N이 0보다 크다면 13자리 이상임
    if N > 0:
        return 'overflow'
    # N이 0보다 작다면 2진수 값 반환
    else:
        return bin_num


T = int(input())
for tc in range(1, T+1):
    # 소수 N
    N = float(input())
    res = dec_to_binary(N)
    print(f'#{tc} {res}')