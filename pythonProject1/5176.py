# 완전이진 트리 만들기
def make_tree(node, N):
    if node <= N:
        # 왼쪽 자식 할당
        left[node] = 2 * node
        # 오른쪽 자식 할당
        right[node] = 2 * node + 1


# 중위순회
def in_order(node):
    global count
    if node <= N:
        in_order(left[node])
        tree[node] = count
        count += 1
        in_order(right[node])


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    # 왼쪽 자식 저장
    left = [0] * (N + 1)
    # 오른쪽 자식 저장
    right = [0] * (N + 1)
    # 노드 값 저장
    tree = [0] * (N + 1)
    # 루트값 1
    root = 1
    # 값을 할당하기 위한 카운트
    count = 1

    # 노드 개수 N 만큼
    for i in range(1, N + 1):
        # 완전 이진 트리 만들기
        make_tree(i, N)

    # 중위 순회하며 값 할당
    in_order(root)

    # 루트 노드(1번)의 값과 N/2번 노드의 값 출력
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
