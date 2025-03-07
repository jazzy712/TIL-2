def in_order(node):
    # 노드가 존재할 때만 실행
    if node:
        # 왼쪽 자식 노드 방문
        in_order(left[node])
        # 현재 노드 방문(노드에 저장된 문자 출력)
        print(word[node], end='')
        # 오른쪽 자식 노드 방문
        in_order(right[node])


T = 10
for tc in range(1, T+1):
    N = int(input())
    # 각각의 정점 정보 저장할 배열 생성
    node_info = [list(map(str, input().split())) for _ in range(N)]
    # 왼쪽 자식 저장
    left = [0] * (N+1)
    # 오른쪽 자식 저장
    right = [0] * (N+1)
    # 노드에 해당하는 글자 저장 `
    word = ['0'] * (N+1)

    # 정점 정보 순회하며 노드정보 저장할 예정
    for info in node_info:
        # 정점 정보는 현재 정점 번호, 정점에 해당하는 문자, 왼쪽 자식, 오른쪽 자식 정점 번호 순서로 이루어짐
        # 현재 정점 번호
        node_num = int(info[0])
        # 정점에 해당하는 문자
        word[node_num] = info[1]
        # 왼쪽 자식이 있으면 번호 저장
        if len(info) > 2:
            left[node_num] = int(info[2])
        # 오른쪽 자식이 있으면 번호 저장
        if len(info) > 3:
            right[node_num] = int(info[3])

    print(f'#{tc}', end=' ')
    # 루트 노드 1번부터 중위순회
    in_order(1)
    print()





