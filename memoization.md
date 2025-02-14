## Memoization

- 컴퓨터 프로그램 실행할 때 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 하여 전체적인 실행속도 향상

- '메모리에 넣기'

```python
# memo를 위한 배열을 할당하고, 모두 0으로 초기화
# memo[0]을 0으로 memo[1]는 1로 초기화한다

def fibo1(n):
    global memo 
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo1(n-1) + fibo1(n-2)
    return memo[n]


memo = [0] * (n+1)
memo[0] = 0
memo[1] = 1
```

- 피보나치 수열의 call tree

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-09-12-49-image.png" title="" alt="" data-align="center">

## DP(dynamic programming)

- 동적 계획 알고리즘
  
  - 최적화 문제 해결
  
  - 입력 크기 작은 부분 문제들을 모두 해결 후 그 해들을 이용하여 보다 큰 크기의 부분 문제들 해결하여, 최종적으로 원래 주어진 입력의 문제를 해결하는 알고리즘
  
  - 1. 문제를 부분 문제로 분할
    
    2. 부분 문제로 나눴으면 가장 작은 부분 문제부터 해를 구함
    
    3. 결과는 테이블에 저장하고, 테이블에 저장된 부분 문제의 해를 이용하여 상위 문제의 해를 구함 
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-14-09-25-27-image.png" title="" alt="" data-align="center">
  
  ```python
  def fibo2(n):
      f = [0] * (n+1)
      f[0] = 0
      f[1] = 1
      for i in range(2, n+1):
          f[i] = f[i-1] + f[i-2]
  
      return f[n]
  ```
  
  - 구현 방식
    
    - recursive 방식 : fib1()
    
    - iterative 방식 : fib2()
    
    - memoization을 재귀적 구조에 사용하는 것보다 반복적 구조로 dp를 구현한 것이 성능 면에서 보다 효율적
    
    - 재귀적 구조는 내부에 시스템 호출 스택을 사용하는 오버헤드가 발생하기 때문
