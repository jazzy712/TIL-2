# 주어진 예시를 보면 후위 순회
def post_order(node):
    # 노드가 존재할 때만 실행
    if node:
        # 왼쪽 자식 노드 방문
        post_order(left[node])
        # 오른쪽 자식 노드 방문
        post_order(right[node])
        # 현재 노드 방문
        # 현재 노드가 연산자이면
        if operator[node] != '0':
            if operator[node] == '+':
                return left + right
            elif operator[node] == '-':
                return left - right
            elif operator[node] == '*':
                return left * right
            elif operator[node] == '/':
                return left / right
        # 정수이면
        else:
            return float(node_info[node-1][1])


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 각각의 정점 정보 저장할 배열 생성
    node_info = [list(map(str, input().split())) for _ in range(N)]
    # 왼쪽 자식 저장
    left = [0] * (N+1)
    # 오른쪽 자식 저장
    right = [0] * (N+1)
    # 노드에 해당하는 연산자 저장할 리스트
    operator = ['0'] * (N+1)
    # 정점 정보 순회하며 저장할 예정
    for info in node_info:
        # 정점이 정수면 정점 번호와 양의 정수가 주어지고(정점 정보의 길이는 2)
        # 정점이 연산자이면 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가 차례대로 주어진다.
        # 현재 정점 번호
        node_num = int(info[0])
        # 정점 정보의 길이가 2가 넘어간다는 것은 정점이 연산자라는 뜻
        if len(info) > 2:
            # 연산자 저장 리스트에 추가
            operator[node_num] = info[1]
            # 왼쪽 자식 추가
            left[node_num] = info[2]
            # 오른쪽 자식 추가
            right[node_num] = info[3]
        else:
            operator[node_num] = '0'

    # 루트 노트 번호는 항상 1
    result = post_order(1)
    print(f'#{tc} {result}')
