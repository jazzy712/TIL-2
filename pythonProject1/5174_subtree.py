def pre_order(tree):
    global cnt
    # 노드가 존재하면
    if tree:
        # 왼쪽 자식 방문
        pre_order(left[tree])
        # 오른쪽 자식 방문
        pre_order(right[tree])
        # 방문 노드 1씩 증가
        cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 정점 개수(V)는 E+1
    V = E + 1
    # 간선 정보 받을 리스트 생성
    arr = list(map(int, input().split()))
    # 왼쪽 자식 저장
    left = [0] * (V + 1)
    # 오른쪽 자식 저장
    right = [0] * (V + 1)
    # 서브 트리에 속한 노드 개수 초기화
    cnt = 0

    # 간선 E 개에서
    for i in range(E):
        # 부모 노드 p와 자식 노드 c
        p, c = arr[2*i], arr[2*i+1]
        # 왼쪽 자식이 없으면?
        if left[p] == 0:
            # 왼쪽 자식으로 설정
            left[p] = c
        # 왼쪽 자식이 있으면
        else:
            # 오른쪽 자식으로 설정
            right[p] = c
    # 노드 N을 루트로 하는 서브 트리 노드 수 계산
    res = pre_order(N)
    print(f'#{tc} {res}')