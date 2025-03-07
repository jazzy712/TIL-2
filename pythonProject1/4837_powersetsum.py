# 부분 집합 합 구하기
def set_sum(A, N, K):
    # 조건 만족하는 부분집합 개수 초기값
    cnt = 0
    # A의 부분집합 개수 = 2^12개(원소 개수 12개이므로)
    for i in range(2**12):
        # 부분집합 저장할 리스트
        subset = []
        # 부분집합의 원소의 합 초기값
        total = 0
        # 집합 A의 길이만큼 순회
        for j in range(12):
            # 부분집합의 j번째 비트가 1이면(j번째 원소가 포함된다면)
            if i & (1 << j):
                # 부분집합에 A의 j번째 원소 추가
                subset.append(A[j])
                # A의 j번째 값 만큼 원소 합에 추가
                total += A[j]
        # 집합 A의 부분 집합 중 N개의 원소를 갖고 있고 원소 합이 K라면
        if len(subset) == N and total == K:
            # 조건 만족하므로 개수 1개씩 증가
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    result = set_sum(A, N, K)
    print(f'#{tc} {result}')

