## List 2

- 2차원 배열
  
  - 1차원 list를 묶어놓은 list
  
  - 2차원 이상의 다차원 list는 차원에 따라 index 선언
  
  - 2차원 list 선언 : 세로길이(행의 개수), 가로 길이(열의 개수)를 필요로 함
  
  ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-07-09-03-01-image.png)

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-04-35-image.png" title="" alt="" data-align="center">

```python
N = int(input)             # 배열 행과 열의 크기
arr = [list(map(int, input().split()))for _ in range(N)]
```

<img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-05-28-image.png" alt="" data-align="center">

```python
N = int(input)
arr = [list(map(int, input())) for _ in range(N)]
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-10-42-image.png" title="" alt="" data-align="center">

```python
arr = [[0] * 4 for _ in range(3)]
```

- 배열 순회
  
  - n X m 배열의 n*m 개의 모든 원소를 빠짐없이 조사하는 방법
  
  

- 행 우선 순회

```python
# i 행의 좌표
# j 열의 좌표
for i in range(n):
    for j in range(m):
        f(array[i][j])     # 필요한 연산 수행
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-18-54-image.png" title="" alt="" data-align="center">

- N x M 배열의 크기와 저장된 값이 주어질 때 합을 구하는 방법

   <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-22-00-image.png" title="" alt="" data-align="center">

```python
N, M = map(int, input().split())
arr = [list(map(int, input(). split())) for _ in range(N)]

s = 0
for i in range(N):
    for j in range(M):
        s += arr[i][j]
```



- 열 우선 순회

```python
# i 행의 좌표
# j 행의 좌표

for j in range(m):
    for i in range(n):
        f(array[i][j])  # 필요한 연산 수행 

for i in range(n):
    for j in range(m):
        f(array[j][i]]) 
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-27-11-image.png" title="" alt="" data-align="center">



- 지그재그 순회

```python
# i 행의 좌표
# j 행의 좌표

for i in range(n):
    for j in range(m):
        f(array[i][j + (m-1-2*j) * (i%2)])
```

<img title="" src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-30-43-image.png" alt="" data-align="center">

- Delta를 이용한 2차원 배열 탐색
  
  - 2차 배열의 한 좌표에서 4방향의 인접 배열 요소를 탐색하는 방법
  
  - 인덱스 (i, j)인 칸의 상하좌우 칸(nj, nj)

```python
di[] <- [0, 1, 0, -1]   # 방향별로 더할 값
dj[] <- [1, 0, -1, 0]

for k : 0 -> 3
    ni <- i + di[k]
    nj <- j + dj[k]
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-09-41-50-image.png" title="" alt="" data-align="center">

```python
arr[0...N-1][0...N-1]   # NxN 배열
di[] <- [0, 1, 0, -1]
dj[] <- [1, 0, 1, 0]
for i : 0 -> N-1:
    for j : 0 -> N-1:
        for d in range(4):
                ni <- i + di[d]
                nj <- j + dj[d]
                if 0<=ni<N and 0<=nj<N      # 유효한 인덱스면
                        f(arr[ni][nj])
```

```python
for i in range(N):
    for j in range(M):
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
            ni = i + di
            nj = j + dj
            if 0<=ni<N and 0<=nj<M:
                print(ni, nj)
```



- 델타 응용
  
  - NxN 배열에서 각 원소를 중심으로, 상하좌우 k칸의 합계 중 최댓값(k=2)

```python
max_v = 0
for i in range(N):
    for j in range(N):
        s = arr[i][j]       # i,j를 중심으로
        for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향
            for c in range(1, k+1):                 # 거리별
                ni, nj = i+di*c, j+dj*c
                if 0<=ni<N and 0<=nj<N:
                    s += arr[ni][nj]
        if max_v < s:
            max_v =s
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-16-35-image.png" title="" alt="" data-align="center">

- 전치 행렬

```python
# i : 행의 좌표, len(arr)
# j : 열의 좌표, len(arr[0])
arr = [[1,2,3],[4,5,6],[7,8,9]]     # 3*3 행렬

for i in range(3):
    for j in range(3):              # for j in range(i): 인 경우
        if i < j:                   #       if 문 필요없음
            arr [i][j], arr[j][i] = arr[j][i], arr[i][j]
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-20-54-image.png" title="" alt="" data-align="center">



- i, j의 크기에 따라 접근하는 원소 비교(N x N)

```python
for i in range(N):
    for j in range(N):
        if
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-23-56-image.png" title="" alt="" data-align="center">

```python
for i in range(N):
    f(arr[i][j])
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-24-28-image.png" title="" alt="" data-align="center">

```python
for i in range(N):
    f(arr[i][N-1-i])
```

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-25-03-image.png" title="" alt="" data-align="center">
