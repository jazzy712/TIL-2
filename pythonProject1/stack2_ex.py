
stack = [0] * 100
top = -1

icp = {'(':3, '*':2, '/':2, '+':1, '-':1}       # 토큰의 우선순위
isp = {'(':0, '*':2, '/':2, '+':1, '-':1}       # 스택 내부에서의 우선순위

fx = '(6+5*(2-8)/2)'
susik = ''
for x in fx:
    if x not in '(+-*/)':                       # 피연산자
        susik += x
    elif x == ')':
        while stack[top] != '(':                # peek
            susik += stack[top]
            top -= 1                            # '('버림. pop
        top -= 1
    else:                                       # '(+-*/'
        if top == -1 or isp[stack[top]] < icp[x]:   # 토큰의 우선순위가 더 높으면
            top += 1                            # push
            stack[top] = x
        else:
            if top == -1 or isp[stack[top]] < icp[x]:
                top += 1
                stack[top] = x
            elif isp[stack[top]] >= icp[x]:
                while top > -1 and isp[stack[top]] >= icp[x]:
                    susik += stack[top]
                    top -= 1
                top += 1                        # push x(token)
                stack[top] = x

print(susik)

