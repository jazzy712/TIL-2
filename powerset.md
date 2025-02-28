## Powerset

- 부분집합 
  
  - 어떤 집합의 공집합과 자기 자신을 포함한 모든 부분집합을 powerset이라고 하며 구하고자 하는 어떤 집합의 원소 개수가 n일 경우 부분집합의 개수는 2의 n제곱(개)
  
  - 백트래킹 기법으로 powerset 만들기
    
    - n개의 원소가 들어있는 집합의 2의 n제곱(개)의 부분집합을 만들 때는, true 또는 false 값을 가지는 항목들로 구성된 n개의 배열 만드는 방법 이용
    
    - 배열의 i번째 항목은 i번째의 원소가 부분집합의 값인지 아닌지를 나타내는 값
    
    

- 각 원소가 부분집합에 포함되었는지를 loop 이용하여 확인하고 부분집합 생성방법
  
  ```python
  bit = [0, 0, 0, 0]
  for i in range(2):
    bit[0] = i                      # 0번째 원소
    for j in range(2):
        bit[1] = j                  # 1번째 원소
        for k in range(2):
            bit[2] = k              # 2번째 원소
            for l in range(2):
                bit[3] = l          # 3번째 원소
                print(bit)          # 생성된 부분집합 출력
  ```

- {1, 2, 3}의 부분집합 표현
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-15-48-36-image.png" title="" alt="" data-align="center">

- powerset을 구하는 백트래킹 알고리즘
  
  ```python
  def backtrack(a, k, n):                                 # a : 주어진 배열, k: 결정할 원소, n:원소 갯수
    c = [0] * MAXCANDIDATES
  
    if k == n:
        process_solution(a, k)                          # 답이면 원하는 작업
    else:
        ncandidates = construct_candidates(a, k, n, c)
        for i in range(ncandidates):
            a[k] = c[i]
            backtrack(a, k+1, n)
  ```
  
  ```python
  def construct_candidates(a, k, n, c):
    c[0] = True
    c[1] = False
    return 2
  
  def process_solution(a, k):
    for i in range(k):
        if a[i]:
            print(num[i], end='')
    print()
  ```
  
    MAXCANDIDATES = 2
    NMAX = 4
    a = [0] * NMAX
    num = [1,2,3,4]
    backtrack(a, 0, 3)
