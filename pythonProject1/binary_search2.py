def binary_search(a, n, key):
    start = 0                       # 검색 구간 설정
    end = n-1
    while start <= end:             # 검색 구간에 1개 이상의 원소가 있으면
        middle = (start + end) // 2 # 기준 위치 계산
        if a[middle] == key:        # 검색 성공!
            return middle
        elif a[middle] > key:       # key보다 크면 왼쪽 구간 선택
            end = middle - 1
        else:                       # a[middle] < key, key보다 작으면 오른쪽 구간 선택
            start = middle + 1
    return  -1                      # 검색 구간이 남아있지 않으면, 검색 실패


arr = [2, 4, 7, 9, 11, 19, 23]       # 오름차순 정렬된 배열
print(binary_search(arr, len(arr), 19))
print(binary_search(arr, len(arr), 100))
print(binary_search(arr, len(arr), 1))