# 이진 트리 만들기
def make_tree(N):
    for node in range(1, N + 1):
        # 왼쪽 자식 노드 번호
        left[node] = node * 2
        # 오른쪽 자식 노드 번호
        right[node] = node * 2 + 1


# 이진 최소 힙을 생성하고 마지막 노드의 조상 노드 값의 합을 계산하는 함수
def binary_heap(heap, N, numbers):
    # 각 노드의 부모 노드 번호를 계산합니다. 부모 노드 번호는 자식 노드 번호를 2로 나눈 값입니다.
    for i in range(1, N + 1):
        par[i] = i // 2

    # 입력된 숫자를 힙에 삽입합니다.
    for j in range(1, N + 1):
        # j번째 노드에 j-1번째 숫자를 삽입합니다.
        heap[j] = numbers[j - 1]

        # 노드 위치 초기화: 현재 삽입한 노드의 번호
        node = j

        # 최소 힙 조건을 만족하도록 부모 노드와 자식 노드를 교환합니다.
        # while 반복문을 부모 노드 값이 자식 노드 값보다 커질 때까지 돌립니다.
        while node > 1 and heap[node] < heap[par[node]]:
            # 조건 만족할 때까지 부모 노드와 자식 노드를 교환합니다.
            heap[node], heap[par[node]] = heap[par[node]], heap[node]
            # 노드의 위치를 부모 노드로 갱신합니다.
            node = par[node]

    # 마지막 노드의 조상 노드 값의 합을 초기화합니다.
    sum_value = 0
    node = N

    # 마지막 노드에서 시작하여 부모 노드로 이동하며 노드에 저장된 값을 합합니다.
    while node > 1:
        node = par[node]
        sum_value += heap[node]

    return sum_value


# 테스트 케이스의 수를 입력받습니다.
T = int(input())

# 각 테스트 케이스를 처리합니다.
for tc in range(1, T+1):
    # 노드의 개수를 입력받습니다.
    N = int(input())

    # 노드에 할당된 숫자 정보를 저장합니다.
    numbers = list(map(int, input().split()))

    # 왼쪽 자식 노드 번호를 저장할 리스트를 초기화합니다.
    left = [0] * (N + 1)
    # 오른쪽 자식 노드 번호를 저장할 리스트를 초기화합니다.
    right = [0] * (N + 1)
    # 부모 노드 번호를 저장할 리스트를 초기화합니다.
    par = [0] * (N + 1)
    # 힙을 생성합니다.
    heap = [0] * (N + 1)

    # 이진 트리 구조를 생성합니다.
    make_tree(N)

    # 이진 최소 힙을 생성하고 마지막 노드의 조상 노드 값의 합을 계산합니다.
    result = binary_heap(heap, N, numbers)

    # 결과를 출력합니다.
    print(f'#{tc} {result}')
