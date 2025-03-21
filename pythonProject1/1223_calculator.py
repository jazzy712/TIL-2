# 먼저 중위 표기법을 후위 표기법으로 변환
def converter(expression):
    # 연산자 우선순위 할당
    # '*'(곱하기)는 '+'(더하기)보다 우선
    operator = {'+' : 1, '*' : 2}

    # 연산자 저장할 스택 생성
    stack = []
    # 후위표기식 저장
    res = []

    # 수식 내 문자 확인
    for char in expression:
        # 숫자를 찾으면?
        if char.isdigit():
            # 후위표기식에 저장
            res.append(char)
        # 연산자를 찾으면?
        else:
            # 현재 연산자의 우선순위가 스택 top 에 있는 연산자의 우선순위보다 낮거나 같으면 pop(+가 스택의 top 에 있으면)
            # operator 에서 연산자에 할당한 우선순위가 낮을 때까지 반복
            while stack and operator[char] <= operator[stack[-1]]:
                # 후위표기식에 스택에서 pop 한 것 저장
                res.append(stack.pop())
            # 스택에 현재 연산자 저장
            stack.append(char)
    # 스택이 빌 때까지 반복
    while stack:
        # 스택에 남아있는 연산자 후위표기식에 저장
        res.append(stack.pop())
    # 각 문자(숫자와 연산자)를 후위표기식에 저장할 리스트에 개별적으로 추가함
    # 리스트의 모든 요소를 하나의 문자열로 결합해야 후위표기식이 도출됨
    return ''.join(res)


# 이제 후위표기식 계산
def calculator(expression):
    # 숫자 저장할 스택 생성
    num = []

    # 수식 내 문자 확인
    for char in expression:
        # 숫자를 찾으면?
        if char.isdigit():
            # 문자열을 정수로 변환 후 숫자 저장 스택에 추가
            num.append(int(char))
        # 연산자를 찾으면?
        else:
            # 스택에서 2개 pop 해서 계산
            b = num.pop()
            a = num.pop()
            # b를 먼저 pop 했으니 b가 두 번째 피연산자이고 a가 첫 번째 피연산자가 됨
            # 만약 문자가 '+'(더하기)라면
            if char == '+':
                result = a + b
            # 문자가 '*'(곱하기)라면
            elif char == '*':
                result = a * b
            # 계산 결과 스택에 넣기
            num.append(result)
    # 마지막에 스택에 남은 값이 결과!
    return num.pop()


T = 10
for tc in range(1, T+1):
    # 문자열의 길이
    N = int(input())
    # 입력받은 문자열
    s = list(input())
    # 입력받은 문자열을 중위 표기법을 후위 표기법으로 변환
    postfix = converter(s)
    # 변환한 후위 표기법 계산
    ans = calculator(postfix)

    print(f'#{tc} {ans}')