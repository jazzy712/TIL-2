# 트리 만들고
def make_tree(N):
    for node in range(1, N+1):
        # 노드 개수 N 이내에서
        if node <= N:
            # 왼쪽 자식 저장
            left[node] = 2 * node
            # 오른쪽 자식 저장
            right[node] = 2 * node + 1


# 중위 순회
def in_order(node):
    # 노드 할당 값 받고
    global value
    if node <= N:
        # 왼쪽 자식 노드 방문
        in_order(left[node])
        # 현재 노드에 값 할당
        tree[node] = value
        # 할당된 값은 1씩 늘어남
        value += 1
        # 오른쪽 자식 노드 방문
        in_order(right[node])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 왼쪽 자식 저장
    left = [0] * (N + 1)
    # 오른쪽 자식 저장
    right = [0] * (N + 1)
    # 노드에 할당된 값 저장
    tree = [0] * (N + 1)
    # 루트는 1번
    root = 1
    # 노드에 할당된 값 1부터 시작
    value = 1
    # 이진트리 만들기
    make_tree(N)
    # 중위 순회 하기(루트 1 부터)
    in_order(root)
    # root 에 저장된 값과 N/2번 노드에 저장된 값 출력
    print(f'#{tc} {tree[root]} {tree[N//2]}')
