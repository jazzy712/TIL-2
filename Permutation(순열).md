## Permutation(순열)

- 집합 {1, 2, 3}에서 모든 순열을 생성하는 함수
  
  - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop 이용해 아래와 같이 구현
  
  ```python
  for i1 in range(1, 4):
      for i2 in range(1, 4):
          if i2 != i1:
              for i3 in range(1, 4):
                  if i3 != i1 and i3 != i2:
                      print(i1, i2, i3)
  ```
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-18-14-06-42-image.png" title="" alt="" data-align="center">

- backtracking 이용하여 {1, 2, 3, ..., NMAX}에 대한 순열 구하기
  
  - 접근 방법은 앞의 부분집합 구하는 방법과 유사
  
  ```python
  def backtrack(a, k, n):
      c = [0] * MAXCANDIDATES
      
      if k == n:
          for i in range(0, k):
              print(a[i], end='')
          print()
      else:
          ncandidates = construct_candidates(a, k, n, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k+1, n)
  ```
  
  ```python
  def construct_candidates(a, k, n, c):
      in_perm = [False] * (NMAX + 1)
      
      for i in range(k):
          in_perm[a[i]] = True
          
      ncandidates = 0
      for i in range(1, NMAX + 1):
          if in_perm[i] == False:
              c[ncandidates] = i
              ncandidates += 1
      return ncandidates
  ```
  
  ```python
  MAXCANDIDATES = 3
  NMAX = 3
  a = [0] * NMAX
  backtrack(a, 0, 3)
  ```
  
  ```python
  def backtrack(a, k, n):
      c = [0] * MAXCANDIDATES
  
      if k == n:
          process_solution(a, k)
      else:
          ncandidates = construct_candidates(a, k, n, c)
          for i in range(ncandidates):
              a[k] = c[i]
              backtrack(a, k+1, n)
  ```
