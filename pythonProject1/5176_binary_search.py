# 완전이진 트리 만들기
def make_tree(N):
    for node in range(1, N+1):
        # 왼쪽 자식 노드 번호
        left[node] = 2 * node
        # 오른쪽 자식 노드 번호
        right[node] = 2 * node + 1


# 중위순회
def in_order(node):
    global cnt
    if node <= N:
        # 왼쪽 자식 노드 방문
        in_order(left[node])
        # 현재 노드에 값 할당
        tree[node] = cnt
        # 다음 값 계산 위해서는 cnt 1씩 증가
        cnt += 1
        # 오른쪽 자식 노드 방문
        in_order(right[node])


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 왼쪽 자식 저장
    left = [0] * (N + 1)
    # 오른쪽 자식 저장
    right = [0] * (N + 1)
    # 각 노드의 값 저장할 리스트
    tree = [0] * (N + 1)
    # 루트값 1
    root = 1
    # 노드에 할당할 값 cnt 1부터 시작
    cnt = 1
    # 완전 이진 트리 만들기
    make_tree(N)
    # 중위 순회
    in_order(root)

    # 루트 노트(1번) 값과 N/2번 노드의 값
    print(f'#{tc} {tree[1]} {tree[N // 2]}')
