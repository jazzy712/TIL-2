T = 10
for tc in range(1, T+1):
    N, string = input().split()
    # 비밀번호 담을 스택 생성
    pw = []
    # 주어진 문자열 순회
    for char in string:
        # 스택에 없거나 현재 문자와 스택의 마지막 문자가 다르다면
        if not pw or char != pw[-1]:
            # 스택에 추가
            pw.append(char)
        # 스택에 있고 현재 문자와 스택 마지막 문자가 같다면
        else:
            # 스택에서 꺼내기
            pw.pop()

    result = ''.join(pw)
    print(f'#{tc} {result}')

