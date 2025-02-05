## List

- Algorithm
  
  - 문제를 해결하기 위한 절차나 방법
  
  - 의사코드
    
    - 정확성 중요
  
  ```python
  CalcSum(n)
     sum <- 0
      for i : 1 -> n
          sum <- sum + i
      return sum;
  ```

- Big-O Notation(빅-오 표기법)
  
  - 시간 복잡도 함수 중에서 가장 큰 영향력을 주는 n에 대한 항만을 표시
  
  - 계수는 생략하여 표시
  
  - n개의 데이터를 입력받아 저장한 후 각 데이터에 1씩 증가시킨 후 각 데이터를 화면에 출력하는 알고리즘의 시간 복잡도는? -> O(n)
  
  - 요소 수가 증가함에 따라 각기 다른 시간 복잡도의 알고리즘
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-23-49-image.png)

```python
O(3n +2) = O(3n) = O(n)    # 최고차항(3n)만 섣택, 계수(n) 3 제거
```



- 배열
  
  - 일정한 자료형의 변수들을 하나의 이름으로 열거하여 사용하는 자료구조
  
  - 6개의 변수를 사용해야 하는 경우, 배열로 바꾸어 사용하는 예
  
  - 다수의 변수로는 하기 힘든 작업을 쉽게 가능
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-26-26-image.png)

- 1차원 배열
  
  - 프로그램에서 사용할 배열의 이름이 필요
  
  - **알고리즘 공부할 때는 그림 그려가면서 하기 !!**
  
  - 인덱스에 가져다 놔야지만 변수의 역할 가능
  
  ```python
  arr[0] = 10 #'배열 arr의 0번 원소에 10을 저장하라'
  arr[idx] = 20 # '배열 arr의 idx번 원소에 20을 저장하라'
  ```



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-27-51-image.png)

- 입력받은 정수를 1차원 배열에 저장하는 법
  
  - 첫 줄에 양수의 개수 N이 주어짐 (5<= N <= 1000)
  
  - 다음 줄에 빈칸으로 구분된 N개의 양수 Ai가 주어짐(1 <= Ai <= 1000000)



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-36-07-image.png)

-> input()으로 받은 숫자들을 빈칸을 기준으로 구분하고 이를 정수형으로 저장하여 list 형태로 반환



- 배열 원소의 합 s 계산

```python
s = 0
for i in range(N):     # for x in arr:
    s += arr[i]        #       s += x
```



![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-38-36-image.png)

- 배열 원소 중 최댓값 max_v 찾기

```python
max_v = arr[0]      # 첫 원소를 최대로 가정
for i in range(1, N):
    if max_v < arr[i]:
        max_v = arr[i]     # arr[i]가 더 크면 max_v 갱신
```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-45-45-image.png)

- 배열 원소 중 최댓값의 인덱스 max_idx 찾기
  
  - 최댓값이 여러 개인 경우 -> **가장 왼쪽의 최댓값 인덱스**

```python
max_idx = 0         # 첫 원소를 최대로 가정
for i in range(1, N):
    if arr[max_idx] < arr[i]:     # 더 큰 값을 만나면 
        max_idx = i               # max_idx 갱신 
```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-14-49-39-image.png)

- 최댓값이 여러 개인 경우 마지막 인덱스 max_idx 찾기

```python
max_idx = 0         # 첫 원소를 최대로 가정
for i in range(1, N):
    if arr[max_idx] < arr[i]:     # 더 큰 값 또는 같은 값이
        max_idx = i               # max_idx 갱신 
```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-15-03-37-image.png)

- 찾는 값이 배열에 있으면 해당 원소의 인덱스, 없으면 -1을 idx에 넣기

```python
idx = -1                     # 찾는 값이 없다고 가정
for i in range(N):
    if arr[i] == V:          # arr[i]가 찾는 값이면 
        idx = i              # 인덱스 저장
        break                # for i
```

![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-15-06-00-image.png)



- 정렬 방식 종류
  
  - **버블 정렬**
  
  - **카운팅 정렬**
  
  - **선택 정렬**
  
  - **퀵 정렬**
  
  - 삽입 정렬
  
  - **병합 정렬**



## Bubble Sort

- 버블 정렬
  
  - 인접한 두 개의 원소를 비교하며 자리를 계속 교환
  
  - 정렬 과정
    
    - 첫 번째 원소부터 인접한 원소끼리 계속 자리를 교환하면서 맨 마지막 자리까지 이동
    
    - 한 단계가 끝나면 가장 큰 원소가 마지막 자리로 정렬
  
  - 시간 복잡도
    
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-05-15-38-05-image.png)

    BubbleSort(a, N)                        # 정렬할 배열과 배열의 크기 
        for i : N-1 -> 1                    # 정렬할 구간의 끝 
            for j : 0 -> i-1                # 비교할 원소 중 왼쪽 원소의 인덱스 
                if a[j] > a[j+1]            # 왼쪽 원소가 더 크면
                    a[j] <-> a[j+1]         # 오른쪽 원소와 교환

    def BubbleSort(a, N):                     # 정렬할 List, N 원소 수
        for i in range(N-1, 0, -1)             # 범위의 끝 위치
            for j in range(i):                  # 비교할 왼쪽 원소 인덱스
                if a[j] > a[j+1]: 
                    a[j], a[j+1] = a[j+1], a[j]


