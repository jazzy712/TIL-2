## Selection Sort(선택 정렬)

- 주어진 자료들 중 가장 작은 값의 원소부터 차례대로 선택하여 위치 교환

- 1. 주어진 리스트 중 최솟값 찾음
  
  2. 그 값을 리스트의 맨 앞에 위치한 값과 교환
  
  3. 맨 처음 위치 제외한 나머지 리스트 대상으로 위 과정 반복

- 시간복잡도 : O(n^)

- 저장되어 있는 자료로부터 k번째로 큰 혹은 작은 원소를 찾는 방법
  
  - 최솟값, 최댓값 홋은 중간값 찾는 알고리즘

- 선택 과정
  
  - 정렬 알고리즘 이용한 자료 정렬
  
  - 원하는 순서에 있는 원소 가져오기

```python
SelectionSort(a[], n):
        for i : 0 -> n-2
            a[i],...,a[n-1] 원소 중 최솟값 a[k] 찾음
            a[i]와 a[k] 교환 
```

```python
def selectionSort(a, N):
    for i in range(N-1):            # 정렬 구간의 시작 인덱스
        min_idx = i                 # 첫 원소 최소로 가정
        for j in range(i+1, N):
            if a[min_idx] > a[j]:   # 최소 원소 위치 갱신
                min_idx = j 
        a[i], a[min_idx] = a[min_idx], a[i]     # 구간 최솟값을 구간 맨 앞으로
```

- k번째로 작은 원소를 찾는 알고리즘
  
  - 1번부터 k번째까지 작은 원소들 찾아 배열 앞쪽으로 이동시키고, 배열의 k번째 반환
  
  - k가 비교적 작을때 유용, O(kn)의 수행시간 필요

```python
def select(arr, k):
    for i in range(0, k):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr[k-1]
```

```python
def selection_sort(nums):
    # 마지막 인덱스 전까지만 순회하면 됨
    for i in range(len(nums) - 1):
        # i를 현재 '최솟값 인덱스'로 가정
        min_idx = i

        # i+1부터 끝까지 확인해 더 작은 값이 있으면 min_idx 갱신
        for j in range(i + 1, len(nums)):
            if nums[min_idx] > nums[j]:
                min_idx = j

        # 찾은 최솟값(min_idx)과 i번째 원소를 교환
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

        # 중간 과정 출력(예시)
        # print('기준 자리:', i, nums)

# 예시 리스트
numbers = [2, 5, 1, 3, 4]

print('정렬 전')
print(numbers)
print('---------------------------------')

selection_sort(numbers)

print('---------------------------------')
print('정렬 후')
print(numbers)
```
