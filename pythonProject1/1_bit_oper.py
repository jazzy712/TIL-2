# # print(7 & 5)
# # print(7 | 5)
# # print(bin(7 & 5))
# #
# # # 1. 이진수로 변환
# # # 2. 각 자리를 AND, OR 로 변환
# #
# # # 1 * 3
# # # 16 * 10
# # # 16^2 * 4
# # print(bin(0x4A3 | 25))
# #
# # secret_code = 1004
# # print(7070 ^ secret_code)
# # print(6258 ^ secret_code)
#
# # ---------------shift 연산자
# print(1 << 1), bin(1 << 1)  # 2
# print(1 << 2), bin(1 << 2)  # 4
# print(1 << 3), bin(1 << 3)  # 8
# print(1 << 4), bin(1 << 4)  # 16
#
# print(7 >> 1)               # 0b111 >> 1 -> 0b11 -> 3
#
# num = 1
# for _ in range(5):
#     print(num, bin(num))
#     num = num << 1

# ----------------- bit 연산 응용
# 1. 부분집합의 수를 바로 구할 수 있음
# arr = [1, 2, 3, 4]  # 16개
# # 각 집합에 해당 수를 안쓰거나/쓰거나 경우의 수 계산 -> 2x2x2x2 = 2^4 = 16
# print(f' 부분 집합의 수 : {1 << len(arr)}')
#
# for i in range(1 << len(arr)):
#     for idx in range(len(arr)):
#         # (1 << idx) : 0b1, 0b10, 0b100, 0b1000
#         # i의i idx 번째 bit 가 1인지 확인(부분 집합에 포함되어 있는지 확인)
#         if i & (1 << idx):
#             print(arr[idx], end=" ")
#         print()

# 응용. 합이 10인 부분 집합만 출력해라
# arr = [1, 2, 3, 4, 5, 6]
# for i in range(1 << len(arr)):
#     subset = []
#     total = 0
#     for idx in range(len(arr)):
#         if i & (1 << idx):
#             subset.append(arr[idx])
#             total += arr[idx]
#     if total == 10:
#         print(f' 부분집합 : {subset}')

# ------------------ 음수 표현
print(bin(5))
print(bin(-5))

print(~4, bin(~4))  # -5
print(~(-4))        # 3

