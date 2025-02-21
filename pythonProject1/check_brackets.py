def check_brackets(str):
    # stack 이 비어있다고 가정
    # stack 이 비어있으면 유효한 인덱스가 없으므로 top 을 -1로 초기화함
    top = -1
    stack = [0] * 100
    # 괄호의 짝이 맞다고 가정
    result = 1

    # 입력받은 문자열 하나씩 검사
    for i in str:
        # 여는 괄호를 만나면?
        if i == '(':
            # 스택에 채워졌으므로 top 에 1 증가
            top += 1
            # 스택의 top 위치에 채워진 여는 괄호 저장
            stack[top] = i
        # 닫는 괄호를 만나면?
        elif i == ')':
            # 그런데 스택이 비어있으면?
            if top == -1:
                # 닫는 괄호가 먼저 나와 짝이 맞지 않아서 0 저장하고 반복문 종료
                result = 0
                break
            # 스택에 여는 괄호가 있다면?
            else:
                # top 1 감소시켜 여는 괄호 제거(pop)
                top -= 1
    # 검사가 끝났는데 스택에 여는 괄호가 남아있다면?
    if top > -1:
        # 짝이 맞지 않으므로 0 저장
        result = 0
    # 결과 반환
    return result


T = int(input())

for tc in range(1, T+1):
    # 괄호 문자열 입력
    str = input()
    result = check_brackets(str)
    print(f'#{tc} {result}')