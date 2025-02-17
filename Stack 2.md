## Stack 2

- 계산기 1
  
  - 문자열로 된 계산식이 주어질 때, 스택을 이용하여 이 계산식의 값을 계산할 수 있음
  
  - 문자열 수식 계산의 일반적 방법
    
    - 중위 표기법의 수식을 후위 표기법으로 변경(스택 이용)
    
    - 후위 표기법의 수식을 스택을 이용하여 계산
  
  - 중위 표기법
    
    - 연산자를 피연산자의 가운데 표기하는 방법
    
    - A + B
  
  - 후위 표기법
    
    - 연산자를 피연산자 뒤에 표기
    
    - AB+
  
  - 중위 표기법의 수식을 후위 표기법으로 변경
    
    - 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현
    
    - 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동
    
    - 괄호 제거
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-06-08-image.png" title="" alt="" data-align="center">
    
    - 1. 입력 받은 중위 표기식에서 토큰 읽음
      
      2. 토큰이 피연산자이면 토큰 출력
      
      3. 토큰이 연산자(괄호 포함)일 때, 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push함. 만약 top에 연산자가 없으면 push 함
      
      4. 토큰이 오른쪽 괄호 ')'이면 스택 top에 왼쪽 괄호 '('가 올 때까지 스택에 pop 연산을 수행하고 pop한 연산자 출력. 왼쪽 괄호 만나면 pop만 하고 출력 x
      
      5. 중위 표기식에 더 읽을 것이 없다면 중지, 더 있으면 1부터 다시 반복
      
      6. 스택에 남아있는 연산자 모두 pop하여 출력
         
         1. 스택 밖의 왼쪽 괄호는 우선 순위가 가장 높으며, 스택 안의 왼쪽 괄호는 우선 순위가 가장 낮음
    
    - 우선 중위 표기법에서 후위 표기법으로 변환
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-11-40-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-11-56-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-26-03-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-26-15-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-26-26-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-26-42-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-26-53-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-27-04-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-27-14-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-27-27-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-27-38-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-27-50-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-28-01-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-28-16-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-28-27-image.png" title="" alt="" data-align="center">

- 계산기2
  
  - 후위 표기법의 수식을 스택을 이용하여 계산
    
    - 1. 피연산자를 만나면 스택에 push
      
      2. 연산자를 만나면 필요한 만큼의 피연산자를 스택에서 pop하여 연산하고, 연산결과를 다시 스택에 push
      
      3. 수식이 끝나면, 마지막으로 스택을 pop하여 출력
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-05-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-17-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-27-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-36-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-47-image.png" title="" alt="" data-align="center">
    
    <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-17-14-31-55-image.png" title="" alt="" data-align="center">
    
    ![](C:\Users\SSAFY\AppData\Roaming\marktext\images\2025-02-17-14-32-06-image.png)
