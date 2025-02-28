## Generate-and-test(완전 검색)

- 완전 검색
  
  - 문제의 해법으로 생각할 수 있는 모든 경우의 수를 나열해보고 확인하는 기법
  
  - 모든 경우의 수를 테스트한 후, 최종 해법 도출
  
  - 일반적으로 경우의 수가 상대적으로 작을 때 유용
  
  - 모든 경우의 수 생성하고 테스트하기 때문에 수행 속도는 느리지만, 해답을 찾아내지 못할 확률 작다
  
  - **자격검정평가 등에서 주어진 문제를 풀 때, 우선 완전 검색으로 접근하여 해답을 도출한 후, 성능 개선을 위해 다른 알고리즘을 사용하고 해답 확인**

- baby-gin 접근
  
  - 고려할 수 있는 모든 경우의 수 생성
    
    - 6개의 숫자로 만들 수 있는 모든 숫자 나열(중복 포함)
      
      ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-06-09-49-19-image.png)
  
  - 해답 테스트
    
    - 앞의 3자리와 뒤의 3자리 잘라, run과 triplet 여부 테스트하고 최종적으로 baby-gin 판단
      
      ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-06-09-49-58-image.png)

- 순열 
  
  - 서로 다른 것들 중 몇 개를 뽑아서 한 줄로 나열
  
  - 서로 다른 n개 중 r개를 택하는 수열
  
  ```python
  nPr
  ```
  
  - 그리고 nPr은 다음과 같은 식 성립
  
  ```python
  nPr = n * (n-1)*(n-2)*...*(n-r+1)
  ```
  
  - nPn = n!이라고 표기하며 Factorial 이라 부름
  
  ```python
  n != n * (n-1)*(n-2)*...*2*1 
  ```

- {1, 2, 3} 포함하는 모든 순열 생성하는 함수
  
  - 동일한 숫자가 포함되지 않았을 때, 각 자리 수 별로 loop를 이용해 구현

```python
for i1 in range(1, 4):
    for i2 in range(1, 4):
        if i2 != i1:
            for i3 in range(1, 4): 
                if i3 != i1 and i3 != i2:
                    print(i1, i2, i3)
```


