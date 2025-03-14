def find_zero_sum(arr):
    # 출력해낼 부분 집합
    power_set = []

    # 모든 부분 집합 생성
    for i in range(1 << n):
        # 현재 부분 집합
        subset = []
        for j in range(n):
            if i & (1 << j):
                subset.append(arr[j])
        power_set.append(subset)

    # 부분 집합의 합이 0인 경우 출력
    for subset in power_set:
        if sum(subset) == 0:
            print(subset)


arr = [-1, 3, -9, 5, -7, -6, 1, 5, 4, -2]
n = len(arr)
find_zero_sum(arr)
