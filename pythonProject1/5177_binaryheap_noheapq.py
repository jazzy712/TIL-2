# 이진 트리 만들기
def make_tree(N):
    for node in range(1, N + 1):
        # 왼쪽 자식 노드 번호
        left[node] = 2 * node
        # 오른쪽 자식 노드 번호
        right[node] = 2 * node + 1


# 조상 노드들의 합 계산
def sum_ancestors(node):
    # 합 최초값 설정
    sum = 0
    # 루트 노드에 도달할 때까지
    while node > 1:
        # 현재 노드의 부모로 이동
        node = parent[node]
        # 부모 노드의 값 합산
        sum += heap[node]
    return sum


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    # 입력받은 숫자로 리스트 만들기
    nums = list(map(int, input().split()))

    # 왼쪽 자식 저장
    left = [0] * (N + 1)
    # 오른쪽 자식 저장
    right = [0] * (N + 1)
    # 부모 값 저장
    parent = [0] * (N + 1)
    # 힙 저장
    heap = [0] * (N + 1)
    # 힙의 크기 초기화
    heap_size = 0

    # 이진 트리 생성
    make_tree(N)

    for i in range(1, N + 1):
        # 부모 인덱스는 자식 노드를 2로 나눈 몫
        parent[i] = i // 2

    # 힙에 숫자 삽입
    for num in nums:
        # 힙의 크기 1씩 증가
        heap_size += 1
        # 새로운 노드 힙에 추가
        heap[heap_size] = num

        # 자식 노드의 값이 부모 노드의 값보다 작으면 교환
        # 현재 위치를 새로운 노드의 위치로 초기화
        current = heap_size
        # 부모 노드의 인덱스가 현재 노드의 인덱스보다 큰 경우에 계속 반복
        while current > 1 and heap[current] < heap[current // 2]:
            # 위치 교환
            heap[current], heap[current // 2] = heap[current // 2], heap[current]
            # 현재 노드의 위치를 부모 노드의 위치로 갱신
            current //= 2

    result = sum_ancestors(heap_size)
    print(f'#{tc} {result}')
