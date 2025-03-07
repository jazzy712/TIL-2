## Power Set(부분집합) - 마이스터고

- 개념
  
  - 집합에 포함된 원소들 선택
  
  - 중요 알고리즘들이 원소들의 그룹에서 최적의 부분 집합을 찾는데 사용
    
    - ex) 배낭 짐싸기(knapsack)
  
  - 나올 수 있는 모든 조합 구하기

- 부분집합의 수
  
  - N개의 원소를 포함한 집합에서 공집합을 포함한 부분집합의 개수는 2^n개 이다
  
  - 각 원소를 부분집합에 포함하거나 포함하지 않는 2가지 경우를 모든 원소에 적용한 것과 같음

## 구현 : 반복문

- [1,2,3] 집합의 모든 부분 집합을 반복문으로 생성

```python
selected = [0] * 3                     # 선택 여부 저장 공간
for i in range(2):                     # 첫 번째 자리 선택 여부
    selected[0] = i
    for j in range(2):                 # 두 번째 자리 선택 여부
        selected[1] = j
        for m in range(2):             # 세 번째 자리 선택 여부 
            selected[2] = m
            subset = []
            for n in range(3):
                if selected[n] == 1:
                    subset.append(n+1)
            print(subset)

'''
[]
[3]
[2]
[2, 3]
[1]
[1, 3]
[1, 2]
[1, 2, 3]
'''
```

## 구현 : 재귀

```python
# 3개의 사용 위치
# depth : 현재 원소를 선택 하냐 마냐를 가리키는 index
def create_subset(depth, included):
    if depth == len(input_list):
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(cnt_subset)
        return
    # 선택하지 않는 경우
    included[depth] = False
    create_subset(depth + 1, included)

    # 선택하는 경우
    included[depth] = True
    create_subset(depth + 1, included)


# 주어지는 집합
input_list = [1, 2, 3]
# 구한 부분집합 저장할 변수
subsets = []
# selected 와 같은 역할
# 각 위치의 값을 선택하나/마나를 저장할 변수
# n = 3 -> [False, False, False]
init_included = [False] * len(input_list)
# 재귀적으로 들어감
create_subset(0, init_included)
print(subsets)
```

## 구현 : 바이너리 카운팅

- 개념
  
  - 부분집합을 생성하기 가장 자연스러운 방법
  
  - 원소 수에 해당하는 N개의 비트열 이용
  
  - n번 비트값이 1이면 n번 원소가 포함되었음을 의미
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-06-15-33-01-image.png" title="" alt="" data-align="center">
  
  ```python
  arr = [1,2,3]
  n = len(arr)
  subset_cnt = 2 ** n
  
  subsets = []
  for i in range(subset_cnt):
      subset = []
      for j in range(n):
          if i & (1 << j):
              subset.append(arr[j])
      subsets.append(subset)
  
  print(subsets)
  ```
