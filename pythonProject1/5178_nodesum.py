T = int(input())
for tc in range(1, T+1):
    # 노드 개수 N, 리프 노드 개수 M, 출력 노드번호 L
    N, M, L = map(int, input().split())
    # 리프 노드 번호 저장 리스트
    leaf_node = list(map(int, input().split()))
    # 값 저장
    tree = [0] * (N+1)
    