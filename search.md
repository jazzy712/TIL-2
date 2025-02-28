## Search(검색)

- 목적하는 탐색 키를 가진 항목을 찾는 것

- 탐색 키(seach key) : 자료를 구별하여 인식할 수 있는 키

- 순차 검색(sequential search)

- 이진 검색(binary search)

- 해쉬(hash)

- sequential search
  
  - 일렬로 되어 있는 자료 순서대로 검색하는 방법
    
    - 간단하고 직관적
    
    - 배열이나 연결 리스트 등 순차구조로 구현된 자료구조에서 원하는 항목 찾을 때 유용
    
    - 단순하여 구현이 쉽지만, 검색 대상의 수가 많은 경우 수행시간이 급격히 증가하여 비효율적
  
  - 정렬되어 있지 않은 경우
    
    - 첫 번째 원소부터 순서대로 검색 대상과 키 값이 같은 원소가 있는지 비교
    
    - 키 값이 동일한 원소를 찾으면 그 원소의 인덱스 반환
    
    - 검색 대상 찾지 못하면 실패
    
    - 찾고자 하는 원소의 순서에 따라 비교회수 결정
    
    - 시간 복잡도 : O(n)
  
  ```python
  arr = [4, 9, 11, 23, 19, 7]
  key = -9
  
  for i in range(len(arr)):
      if arr[i] == key:
          print(i, '에 위치하고 있음')
          break
  else:
      print('못찾음')
  ```
  
  ```python
  def unordered_sequential_search(nums, target):
      '''
      정렬되지 않은 리스트(nums)에서
      target을 순차적으로 검색한 뒤
      찾으면 해당 인덱스를, 없으면 -1을 반환
      '''
      index = 0  # 현재 탐색 위치
  
      while index < len(nums):
          if nums[index] == target:
              return index  # 값 발견 시 인덱스 반환
          else:
              index += 1
  
      return -1  # 끝까지 찾지 못했으면 -1
  
  
  
  numbers = [4, 9, 11, 23, 19, 7]
  print(unordered_sequential_search(numbers, -9))  # -1
  print(unordered_sequential_search(numbers, 11))  # 2
  ```
  
  ```python
  def sequential_search(a, n, key)
      i <- 0
      while i<n and a[i]!=key:
              i <- i+1
      if i<n: return i
      else: return -1
  ```
  
  ```python
  for i:0 -> n-1:
      if a[i] == key:
          return i
  return -1
  ```
  
  - 정렬되어 있는 경우
    
    - 자료가 오름차순으로 정렬된 상태에서 순차적으로 검색하면서 키 값을 비교하여, 원소의 키 값이 검색대상의 키 값보다 크면 검색 종료
    
    - 찾고자 하는 원소의 순서에 따라 비교회수 결정
      
      - 정렬이 되어 있으므로, 검색 실패를 반환하는 경우 평균 비교 횟수가 반으로 줄어듬
      
      - 시간 복잡도 : O(n)
  
  ```python
  arr = [4, 7, 9, 11, 19, 23]
  key = 9
  
  for i in range(len(arr)):
      if arr[i] == key:
          print(i, ' 에 위치하고 있음')
          break
      elif arr[i] > key:
          print(i, '번째까지만 탐색하고 종료.')
          break
  else:
      print('못 찾음')
  ```
  
  ```python
  def ordered_sequential_search(nums, target):
      '''
      정렬된 리스트(nums)에서
      target을 순차적으로 검색한 뒤
      찾으면 해당 인덱스를, 없으면 -1을 반환
      '''
      index = 0  # 현재 탐색 위치
  
      while index < len(nums):
          if nums[index] == target:
              return index  # 값 발견 시 인덱스 반환
          else:
              # 정렬된 상태에서 nums[index]가 target보다 커지면
              # 이후 원소들도 더 클 테니 탐색 종료 (더 이상 볼 필요 없음)
              if nums[index] > target:
                  return -1
              else:
                  index += 1
  
      return -1  # 끝까지 찾지 못했으면 -1
  
  
  # 예시 리스트 (정렬된 상태)
  numbers = [4, 7, 9, 11, 19, 23]
  print(ordered_sequential_search(numbers, -9))  # -1
  print(ordered_sequential_search(numbers, 7))   # 1
  ```
  
  ```python
  def sequential_search2(a, n, key)
       i <- 0
       while i<n and a[i]<key:
              i <- i+1
       if i<n and a[i] == key:
              return i
       else:
              return -1
  ```
  
  ```python
  for i:0 -> n-1:
      if arr[i] == key:
          return i
      elif arr[i] > key:
          return -1
  ```

## Binary Search(이진 검색)

- 이진 검색
  
  - 자료의 가운데에 있는 항목의 키 값과 비교하여 다음 검색의 위치를 결정하고 검색을 계속 진행
    
    - 목적 키를 찾을 때까지 이진 검색을 순환적으로 반복 수행함으로써 검색범위를 반으로 줄여가면서 보다 빠르게 검색 수행
  
  - 자료가 정렬된 상태
  
  - 1. 자료 중앙에 있는 원소 선택
    
    2. 중앙 원소 값과 찾고자 하는 목표 값 비교
    
    3. 목표 값이 중앙 원소 값보다 작으면 자료 왼쪽 반에 대해서 새로 검색 수행하고 크다면 자료 오른쪽 반 대해서 새로 검색 수행
    
    4. 값  찾을때까지 반복
  
  - 구현
    
    - 검색 범위 시작점과 종료점 이용하여 검색 반복 수행
    
    - 자료에 삽입이나 삭제가 발생했을 때, 배열의 상태를 항상 정렬 상태로 유지하는 작업 필요

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:             # False가 될 때까지
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid  # 검색 성공 시 인덱스 반환
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1  # 검색 실패 시 -1 반환

# 예시
numbers = [2, 4, 7, 9, 11, 19, 23]
print(binary_search(numbers, 11))  # 4 (인덱스 4)
print(binary_search(numbers, 10))  # -1 (없음)
```

```python
def binarySearch(a, N, key):        # key를 찾으면 인덱스, 실패하면 -1
    start = 0
    end = N-1
    while start <= end:             # 검색 구간의 원소가 1개 이상이면
            middle = (start + end)//2
            if a[middle] == key:    # 검색 성공
                    return middle
            elif a[middle] > key:   # 찾는 값보다 크면
                    end == middle -1   # 왼쪽 구간 선택
            else:                   # 찾는 값보다 작으면
                    start = middle +1  # 오른쪽 구간 선택
    return  -1                      # 검색 실패
```

```python
def binary_search_recursive(arr, left, right, target):
    '''
    재귀 함수를 이용한 이진 검색 (Binary Search)

    - arr  : 정렬된 리스트 (오름차순)
    - left : 현재 검색 범위의 시작 인덱스
    - right: 현재 검색 범위의 끝 인덱스
    - target: 찾고자 하는 값

    반환값:
    - target이 arr 안에 존재하면 해당 인덱스
    - 존재하지 않으면 -1
    '''
    # 1. 검색 범위가 유효한지 확인
    if left > right:
        return -1  # 검색 실패

    # 2. 중앙(mid) 인덱스 계산(반으로 가르)
    mid = (left + right) // 2

    # 3. 중앙 값과 target 비교
    if arr[mid] == target:
        return mid  # 검색 성공
    elif arr[mid] > target:
        # 4. target이 더 작으면 왼쪽 영역을 재귀 탐색
        return binary_search_recursive(arr, left, mid - 1, target)
    else:
        # 5. target이 더 크면 오른쪽 영역을 재귀 탐색
        return binary_search_recursive(arr, mid + 1, right, target)


# 예시
nums = [2, 4, 7, 9, 11, 19, 23]
# 배열의 전체 범위를 첫 호출 시 지정
idx_found = binary_search_recursive(nums, 0, len(nums) - 1, 4)
print("결과 인덱스:", idx_found)  # 예: 결과인덱스 1
```

## Index

- 테이블에 대한 동작 속도 높여주는 자료 구조

- 데이터베이스 인덱스는 **이진 탐색 트리** 구조

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-10-10-19-26-image.png" title="" alt="" data-align="center">

## 
