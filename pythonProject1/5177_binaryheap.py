import heapq

def sum_calculate(heap, index):
    # 조상 노드에 저장된 정수의 합 초기화
    sum = 0
    # 루트(index 1)에 갈 때까지 반복
    while index > 1:
        # 부모 노드의 인덱스는 자식 노드를 2로 나눈 몫
        index //= 2
        # 조상 노드(부모 노드)의 합은 부모 노드의 인덱스만큼 증가
        sum += heap[index]
    return sum


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 입력받은 숫자로 리스트 만들기
    nums = list(map(int, input().split()))
    # 빈 힙 생성
    heap = []

    # 숫자들 heappush(이진 최소힙에 저장)
    # heapq 는 최소 힙 제공(부모 노드 값 < 자식 노드 값)
    for i in nums:
        heapq.heappush(heap, i)

    res = sum_calculate(heap)

    print(f'#{tc} {res}')
