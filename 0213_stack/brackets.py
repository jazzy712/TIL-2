import sys

sys.stdin = open('input.txt')


def check_brackets(string):
    # 빈 스택
    stack = []

    # 입력된 문자열을 순회하면서,
    for char in string:
        # 1. 여는 괄호라면?
        # if char == '(' or char == '{' or char == '[':
        if char in '({[':
            stack.append(char)
        # 2. 닫는 괄호라면?
        elif char in ')}]':

            # 2.1 스택이 비어있는지 확인해야함(pop 전에)
            # 비어있으면 길이가 0임
            if len(stack) == 0:
                # 비어있다면 짝이 불일치
                return -1
            
            # 2.2 스택이 비어있지 않다면, pop 진행
            # pop은 제거하고 반환 !!!!
            top_char = stack.pop()

            # 2.3 pop해서 나온 여는 괄호와 지금의 닫는 괄호 비교
            # 비교를 했지만 짝이 맞지 않는 경우
            if char == ')' and top_char != '(':
                return -1
            elif char == '}' and top_char != '{':
                return -1
            elif char == ']' and top_char != '[':
                return -1

        # 3. 괄호가 아니라면?
        # 무시하고 다음 반복으로 이동(continue)
        else:
            continue

    # 4. 입력된 문자열을 모두 처리 후, 
    # 스택이 비어있다면 -> 성공(짝이 맞음)
    if len(stack) == 0:
        return 1
    # 스택에 무언가 남았다면 -> 실패(짝이 맞지 않음)
    else:
        return -1
    


T = int(input().strip())
for tc in range(1, T + 1):
    line = input().strip()
    result = check_brackets(line)
    print(f'#{tc} {result}')
