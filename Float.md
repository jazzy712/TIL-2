## Float(실수)

- 파이썬에서 실수 출력 방법
  
  - f-string 문법 지향
  
  ```python
  t1 = 10
  t2 = 3.141592
  
  print(f'변수 값은 {t1} 입니다')
  print(f'변수 값은 {t2} 입니다')
  ```

- 소수점 출력 방법
  
  - {t2 : .2f} : t2값을 소수점 둘째 자리에서 **반올림**하여 표현
  
  ```python
  t1 = 10
  t2 = 3.141592
  
  print(f'변수 값은 {t1} 입니다')
  print(f'변수 값은 {t2:.2f} 입니다')
  ```

- 파이썬에서 실수 표현 범위
  
  - 파이썬은 다른 언어와 달리 내부적으로 더 큰 규모의 자료구조를 사용해서 훨씬 넓은 범위의 실수 표현 가능

- **컴퓨터는 실수를 내부적으로 근사적으로 관리**
  
  - 작은 오차가 계산 과정에서 다른 결과 가져옴
  
  ```python
  print(0.1+0.1+0.1 = 0.3)  # False
  ```

- 소수점이 있는 10진수를 2진수로 변환 예시

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-07-10-49-08-image.png" title="" alt="" data-align="center">

- 소수점을 포함한 2진 실수를 10진수로 변환 예시

<img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-07-10-51-04-image.png" title="" alt="" data-align="center">

- 실수의 표현
  
  - 부동소수점(floating-point) 표기법 사용
  
  - 부동소수점 표기
    
    - **소수점의 위치를 고정**시켜 표현
    
    - 소수점의 위치를 왼쪽의 가장 유효한 숫자 다음으로 고정시키고 밑수의 지수승으로 표현
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-03-07-10-52-08-image.png" title="" alt="" data-align="center">

- 12.375를 부동소수점으로 표기
  
  - 12.375를2진수로 변환 : 12는 1100, 0.375는 0.011이므로 **1100.011**
  
  - **1100.011** = 1.**100011**  * 2^3
  
  - 즉 가수는 **10001**이고, 지수는 3

- 지수 + bias : IEEE 754는 bias를 더한 결과로표기
  
  - 3  + 127(bias) = 130(2진수로는 10000010)

- 12.375를 IEEE 754로 표기방법
  
  - 부호 비트 : 0(양수)
  
  - 지수 : 10000010
  
  - 가수 : **100011**000000000000000000 
