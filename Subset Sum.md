## Subset Sum(부분힙합의 합)

- 유한 개의 정수로 이루어진 집합이 있을 때, 이 집합의 부분집합 중에서 그 집합의 원소를 모두 더한 값이 0이 되는 경우가 있는지를 알아내는 문제

- 예를 들어, [-7, -3, -2, 5, 8] 라는 집합이 있을 때, [-3, -2, 5]는 이 집합의 부분집합이면서 (-3)+(-2)+5=0 이므로 이 경우의 답은 참이 된다

- **완전검색** 기법으로 **부분집합의 합** 문제를 풀기 위해서는, 우선 집합의 모든 부분집합 생성 후에 각 부분집합의 합 계산

- 집합의 부분집합 생성 방법??

- 부분집합의 수
  
  - 집합의 원소가 n개일 때, 공집합을 포함한 부분집합의 수는 2의 n 제곱(개)이다
  
  - 이는 각 원소를 부분집합에 포함시키거나 포함시키지 않는 2가지 경우를 모든 원소에 적용한 경우의 수와 동일

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-07-10-40-04-image.png" title="" alt="" data-align="center">


