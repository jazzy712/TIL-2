## Greedy Algorithm

- 탐욕 알고리즘
  
  - 여러 경우 중 하나를 결정해야 할 때마다 그 순간에 최적이라고 생각되는 것을 선택해 나가는 방식으로 진행해 최종 해답 도달
  
  - 각 선택 시점에서 이루어지는 결정은 지역적으로는 최적이지만, 그 선택들을 계속 수집하여 최종적인 해답을 만들었다고 하여, 최적이라는 보장은 없음
  
  - 머릿속에 떠오르는 생각을 검증없이 구현하면 greedy 접근
  
  - 1. 해 선택 : 현재 상태에서 부분 문제의 최적 해를 구한 뒤, 이를 부분해 집합(Solution Set)에 추가
    
    2. 실행 가능성 검사 : 새로운 부분해 집합이 실행 가능한지 확인, 문제의 제약 조건 위반하지 않는지 검사
    
    3. 해 검사 : 새로운 부분해 집합이 문제의 해가 되는지 확인, 전체 문제의 해가 완성되지 않았다면 해 선택부터 다시 시작
  
  - baby-gin 풀이
    
    - 6개의 숫자는 6자리의 정수 값으로 입력
    
    - counts 배열의 각 원소 체크하여 run과 triplet 및 baby-gin 여부 판단
      
      ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-06-10-24-36-image.png)
      
      ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-06-10-24-49-image.png)
  
  ```python
  num = 456789    # Baby gin 확인할 6자리 수
  c = [0] * 12    # 6자리 수로부터 각 자리수를 추출하여 개수 누적할 리스트
  
  for i in range(6):
      c[num % 10] += 1     # 1의 자리를 알아내는 연산(중요 !) 
      num //= 10           # 1의 자리를 제거하는 연
  i = 0
  tri = run = 0
  while i < 10:
      if c[i] >= 3:       # triplet 조사 후 데이터 삭제
          c[i] -= 3
          tri += 1
          continue;
      if c[i] >= 1 and c[i+1] and c[i+2] >= 1:    # run 조사 후 데이터 삭제
          c[1] -= 1
          c[i+1] -= 1
          c[i+2] -= 1
          run += 1
          continue
      i += 1
  
  if run + tri == 2 : print("Baby Gin")
  else : print("Lose")
  ```
