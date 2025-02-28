def BubbleSort(arr, N): # 정렬할 List, N 원소 수
    n = len(arr)
    for i in range(N-1, 0, -1):             # 범위의 끝 위치
        for j in range(i):                  # 비교할 왼쪽 원소 인덱스(0부터 구간 마지막 인덱스 -1)
            if arr[j] > arr[j+1]:           # 왼쪽 원소가 크면 자리교환
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

N = int(input())
arr = list(map(int, input(). split()))
BubbleSort(arr, N)
print(arr)