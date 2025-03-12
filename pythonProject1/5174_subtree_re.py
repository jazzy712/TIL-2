def subtree(V):
    global cnt
    # 노드가 존재하면
    if V:
        # 왼쪽 자식 방문
        subtree(left[V])
        # 오른쪽 자식 방문
        subtree(right[V])
        # 방문 노드 1씩 증가
        cnt += 1
    return cnt


T = int(input())

for tc in range(1, T+1):
    E, N = map(int, input().split())
    # 노드 개수는 E + 1
    V = E + 1
    # 부모 자식 정보 받을 리스트 생성
    info = list(map(int, input().split()))
    # 왼쪽 자식 정보 저장
    left = [0] * (V + 1)
    # 오른쪽 자식 정보 저장
    right = [0] * (V + 1)
    # 서브 트리에 속한 노드의 개수 초기화
    cnt = 0
    # 간선 E개 중에서
    for i in range(E):
        # 부모 노드(p)와 자식 노드(c) 저장
        p = info[i * 2]
        c = info[i * 2 + 1]
        # 왼쪽 자식이 없으면
        if left[p] == 0:
            # 왼쪽 자식으로 설정
            left[p] = c
        # 있으면
        else:
            # 오른쪽 자식으로 설정
            right[p] = c
    res = subtree(N)
    print(f'#{tc} {res}')