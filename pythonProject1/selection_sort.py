def selectionSort(a, N):
    for i in range(N-1):            # 기준위치정(최솟값을 찾는 구간의 시작 인덱스)
        min_idx = i                 # 첫 원소 최소로 가정, 최솟값 인덱스 초기화
        for j in range(i+1, N):
            if a[min_idx] > a[j]:   # 최소 원소 위치 갱신
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]     # 구간 최솟값을 구간 맨 앞으로
        # tmp = a[i]
        # a[i] = a[min_idx]
        # a[min_idx] = temp
arr = [10, 25, 64, 22, 11]
selectionSort(arr, len(arr))
print(arr)

def select(arr, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]