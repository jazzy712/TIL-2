from collections import deque

dq = deque()

# 뒤쪽으로 삽입
dq.append(1)
dq.append(2)
dq.append(3)
print(dq)               # deque([1, 2, 3])

# 앞쪽으로 삽입
dq.appendleft(0)
print(dq)               # deque([0, 1, 2, 3])

# 뒤쪽에서 삭제
dq.pop()
print(dq)               # 3

# 앞쪽에서 삭제
dq.popleft()
print(dq)               # deque([1, 2])
