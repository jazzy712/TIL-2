T = int(input())

for tc in range(1, T+1):
    str = input()
    top = -1
    # 괄호 짝 딕셔너리 설정
    bracket_pair = {'(' : ')', '{' : '}'}

    def check_brackets(str):
        # 빈 리스트 stack 설정
        stack = []
        # 주어진 문자열 내 각 문자 탐색
        for i in str:
            # 만약 문자가 여는 괄호라면?
            if i in '({':
                # 스택 리스트에 추가
                stack.append(i)
            # 만약 문자가 닫는 괄호라면?
            elif i in ')}':
                # 근데 스택이 비어있다면?
                if not stack:
                    # 짝이 맞지 않으므로 0 반환
                    return 0
                # 스택에 가장 최근에 추가된 문자 꺼냄
                j = stack.pop()
                # 만약 현재 닫는 괄호와 꺼낸 문자가 위 괄호 짝 딕셔너리에서 짝이 맞지 않는다면?
                if i != bracket_pair[j]:
                    # 짝이 맞지 않으므로 0 반환
                    return 0
        # 검사가 다 끝나고 스택이 비어있지 않다면?
        if stack:
            return 0
        # 모든 조건 통과하면 1 반환
        return 1

    result = check_brackets(str)
    print(f'#{tc} {result}')



