class Queue:
    def __init__(self, capacity=10):
        self.capacity = capacity        # 큐의 최대 용량 설정
        self.items = [None] * capacity  # 큐를 저장할 리스트 초기화
        self.front = -1
        self.rear = -1

    def is_empty(self):
        # front 와 rear 가 같으면 큐가 비어있다
        return self.front == self.rear

    def is_full(self):
        # rear 가 큐의 최대 인덱스(capacity - 1)에 도달하면 큐가 가득 참
        return self.rear == self.capacity - 1

    def enqueue(self, item):
        # 큐가 가득 찼다면
        if self.is_full():
            # raise : Error 일으키는 명령어
            raise IndexError("큐가 가득 찼습니다.")
        # 삽입 일어났으므로 rear 인덱스가 1 증가
        self.rear += 1
        # 새 항목을 rear 위치에 삽입
        self.items[self.rear] = item

    def dequeue(self):
        # 큐가 비어있다면
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        # front 값이 하나 이동
        self.front += 1
        # front 위치의 항목을 가져옴
        item = self.items[self.front]
        # 해당 위치를 None 으로 설정("지웠다")
        self.items[self.front] = None
        return item

    def peek(self):
        # 큐가 비어있다면
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self.items[self.front + 1]

    def get_size(self):
        # 요소의 개수 = rear 의 값 - front 의 값
        return self.rear - self.front


queue = Queue(5)
print(queue.items)                      # [None, None, None, None, None]

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.items)                      # [1, 2, 3, 4, None, None]

print("Dequeued:", queue.dequeue())     # Dequeued: 1
print("Dequeued:", queue.dequeue())     # Dequeued: 2
print(queue.items)                      # [None, None, 3, 4, None]

queue.enqueue(5)
queue.enqueue(6)                        # IndexError: 큐가 가득 찼습니다.
