def str_compare(str1, str2):
    # str1,2의 인덱스 i,j
    i = 0
    j = 0
    # str1,2의 길이 N,M
    N = len(str1)
    M = len(str2)
    while i < N and j < M:
        # str1의 i번째 값과 str2의 j번째 값이 다르면
        if str1[i] != str2[j]:
            # 이미 비교했던 자리만큼 뒤로 돌아가서 1 증가
            j = j - i +1
            # 비교군 인덱스는 처음부터 다시 시작
            i = 0
        # 일치한다면
        else:
            # 다음 칸 이동
            i += 1
            j += 1
    # while 문 빠져나와서
    # 인덱스 값이 str1 길이와 일치하게 된다면(str1의 모든 문자와 일치한다면)
    if i == N:
        # 1 출력
        return 1
    # 그렇지 않으면
    else:
        # 0 출력
        return 0

T = int(input())

for tc in range(1, T+1):
    # 입력받을 문자열 str1, str2 설정
    str1 = input()
    str2 = input()
    result = str_compare(str1, str2)
    print(f'#{tc} {result}')
