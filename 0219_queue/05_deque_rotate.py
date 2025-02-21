from collections import deque

dq = deque([1, 2, 3, 4, 5])

dq.rotate(1)  # 오른쪽으로 1칸 이동
print(dq)  # deque([5, 1, 2, 3, 4])

dq.rotate(-2)  # 왼쪽으로 2칸 이동
print(dq)  # deque([2, 3, 4, 5, 1])


# 회전 예시
dq1 = deque([1, 2, 3, 4, 5])

K = 3

dq1.rotate((-K))

print(dq1)  # deque([4, 5, 1, 2, 3])


# rotate를 사용하지 않고 직접 회전
dq2 = deque([1, 2, 3, 4, 5])
for _ in range(K):
    dq2.append(dq2.popleft())
print(dq2)  # deque([4, 5, 1, 2, 3])
