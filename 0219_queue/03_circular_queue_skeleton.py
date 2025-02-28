class CircularQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity + 1    # 실제 용량은 요청된 용량보다 1 크게 설정
        self.items = [None] * self.capacity  # 큐를 저장할 리스트 초기화
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        # rear 의 다음 위치가 front 와 같으면 가득 참
        return (self.rear + 1) % self.capacity == self.front

    def enqueue(self, item):
        # 큐가 가득 찼다면
        if self.is_full():
            # raise : Error 일으키는 명령어
            raise IndexError("큐가 가득 찼습니다.")
        # rear 를 다음 위치로 이동(원형으로 순환)
        self.rear = (self.rear + 1) % self.capacity
        # 새 항목을 rear 위치에 삽입
        self.items[self.rear] = item

    def dequeue(self):
        # 큐가 비어있다면
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        # front 를 다음 위치로 이동(원형으로 순환)
        self.front = (self.front + 1) % self.capacity
        # front 위치의 항목을 가져옴
        item = self.items[self.front]
        # 해당 위치를 None 으로 설정("지웠다")
        self.items[self.front] = None
        return item

    def peek(self):
        # 큐가 비어있다면
        if self.is_empty():
            raise IndexError("큐가 비어있습니다.")
        return self.items[(self.front + 1) % self.capacity]

    def get_size(self):
        # 현재 큐에 있는 항목의 개수를 계산
        # rear 가 front 보다 앞에 있으면 음수가 되기 때문에 capacity 를 더해서 음수를 방지
        return (self.rear - self.front + self.capacity) % self.capacity


queue = CircularQueue(5)

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
# queue.enqueue(6)              # IndexError : 큐가 가득 찼습니다.
print(queue.items)              # [None, 1, 2, 3, None, None]
print(queue.get_size())         # 5

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.items)              # [None, None, None, None, None, None]

queue.enqueue(4)
print(queue.items)
queue.enqueue(5)
print(queue.items)
queue.enqueue(6)
print(queue.items)              # [6, None, None, None, 4, 5]

