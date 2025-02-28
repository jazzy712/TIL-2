class Stack:
    def __init__(self, size):
        self.size = size
        # 고정 크기 배열 사용
        self.capacity = [None] * size
        # 초기 top 포인터는 -1
        self.top = -1

    def push(self, item):
        # 삽입 전에 스택이 가득 찼는지를 확인
        if self.top == self.size - 1:
            return "Stack Overflow"
        self.top += 1
        # top 위치에 값 저장장
        self.capacity[self.top] = item

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
        # top 포인터가 -1이면 스택이 비어있음
        # return self.top == -1

    def pop(self):
        # 스택이 비어있지 않은지를 확인
        # 비어있다면
        if self.is_empty():
            return "Stack Underflow"
        item = self.capacity[self.top]
        self.capacity[self.top] = None
        # top 포인터 감소
        self.top -= 1
        return item
        

    def peek(self):
        # 비어있다면
        if self.is_empty():
            return "스택이 비어있습니다" 
        # top 위치 값 반환
        return self.capacity[self.top]


# 사용 예제
stack = Stack(3)
stack.push(5)
stack.push(10)
stack.push(15)
print(stack.push(100))
print(stack.pop())  # 15
print(stack.pop())  # 10
print(stack.pop())  # 5
print(stack.pop())  # Stack Underflow
