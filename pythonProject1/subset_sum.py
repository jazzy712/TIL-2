# bit = [0, 0, 0, 0]
# for i in range(2):
#     bit[0] = i               # 0번 원소
#     for j in range(2):
#         bit[1] = j           # 1번 원소
#         for k in range(2):
#             bit[2] = k       # 2번 원소
#             for l in range(2):
#                 bit[3] = l   # 3번 원소
#                 print_subset(bit)   # 생성된 부분집합 출력


a= [2, 3, 7]
bit = [0] * 3
for i in range(2):
    bit[0] = i
    for j in range(2):
        bit[1] = j
        for k in range(2):
            bit[2] = k
            # print(bit)
            s = 0                            # 부분집합의 합
            for b in range(3):
                if bit[b]:
                    print(a[b], end = ' ')   # 부분집합에 포함된 원소
                    s += a[b]
            print(bit, s)


# 간결하게 부분집합 생성 방법
arr = [3,6,7,1,5,4]

n = len(arr)            # n : 원소의 개수
for i in range(1<<n):   # 1<<n : 부분집합 개수
    for j in range(n):  # 원소의 수만큼 비트 비교
        if i & (1<<j):  # i의 j번 비트가 1인 경우(0이 아니면)
            print(arr[j], end = ' ')    # j번 원소 출력
    print()
print()