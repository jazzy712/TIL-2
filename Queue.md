## Queue

- 큐의 특성
  
  - 스택과 마찬가지로 삽입과 삭제의 위치가 제한적인 자료구조
    
    - 큐의 뒤에서는 삽입만 하고, 큐의 앞에서는 삭제만 이루어지는 구조
  
  - **선입선출** 
    
    - 큐에 삽입한 순서대로 원소가 저장되어, 가장 먼저 삽입(First in)된 원소는 가장 먼제 삭제(First out)됨
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-19-09-05-02-image.png" title="" alt="" data-align="center">

- 큐의 기본 연산
  
  - 삽입 : enQueue
  
  - 삭제 : deQueue
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-19-09-08-49-image.png" title="" alt="" data-align="center">

- 큐의 연산 과정
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-19-09-10-41-image.png" title="" alt="" data-align="center">
  
  <img src="file:///C:/Users/SSAFY/AppData/Roaming/marktext/images/2025-02-19-09-10-59-image.png" title="" alt="" data-align="center">

- 선형큐
  
  - 1차원 배열 이용한 큐
    
    - 큐의 크기 = 배열의 크기
    
    - front : 저장된 첫 번째 원소의 인덱스
    
    - rear : 저장된 마지막 원소의 인덱스
  
  - 상태 표현
    
    - 초기 상태 : front = rear = -1
    
    - 공백 상태 : front == rear
    
    - 포화 상태 : rear == n-1(n : 배열의 크기, n-1: 배열의 마지막 인덱스)

- 초기 공백 큐 생성
  
  - 크기 n인 1차원 배열 생성
  
  - front와 rear를 -1로 초기화

- 삽입 : enQueue(item)
  
  - 마지막 원소 뒤에 새로운 원소 삽입하기 위해
    
    - 1) rear 값을 하나 증가시켜 새로운 원소 삽입 자리 마련
      
      2)  그 인덱스에 해당하는 배열원소 Q[rear]에 item 저장

```python
def enQueue(item):
    global rear
    if isFull():
        print("Queue_Full")
    else:
        rear <- rear + 1;
        Q[rear] <- item;
```

- 삭제 : deQueue
  
  - 가장 앞에 있는 원소 삭제하기 위해
    
    - 1. front 값 하나 증가시켜 큐에 남아있는 첫 번째 원소 이동
      
      2. 새로운 첫 번째 원소 리턴 함으로써 삭제와 동일한 기능

    deQueue()ㅔ
        if(isEmpty()): 
            then Queue_Empty();
        else:
            {
            front <- front +1;
            return Q[front];
            }


