# for j : 0-> 8-N:
#     for k: 0-> N//2-1:
#         if s[j+k] != s[j+N-1-k]:
#             break
#     if cnt == N//2:
#         total += 1


# s1 = 'abc'
# s2 = 'ab'
# s3 = 'def'
# s4 = s2 + 'c'
# print(s1, s4)
# print(s1 == s4)
# print(s1 is s4)
# print(s1 is 'abc')
# print(s4 is 'ab' + 'c')             # False
#
# s1 = 'ab'
# s2 = 'ab'
# s3 = 'ac'
# s4 = 'AC'
# s5 = 'abc'
# s6 = '1ab'
# print(s1 == s2)                     # True
# print(s1 < s2)                      # False
# print(s1 < s3)                      # True
# print(s3 < s4)                      # False
# print(ord('a'), ord('A'))           # 97 65
# print(s1 < s5)                      # True
# print(s4 < s6)                      # False
# print('A' < '@')                    # False
#
# def my_strcmp(s1, s2):
#     if s1<s2:
#         return -1
#     elif s1>s2:
#         return 1
#     else:
#         return 0

# a = 'F'
# b = int(a, 16)
# c = '1001'
# d = int(c, 2)
# print(b)
# print(d)
#
# def atoi(s):
#     i = 0
#     for x in s:
#         i = i*10 + ord(x)-ord('0')
#     return i
# s = '123'
# a = atoi(s)
# print(a+1)

N = int(input())
txt = input()
total = 0
for j in range(8-N+1):                  # 회문을 확인하는 구간의 첫 글자 인덱스
    for k in range(N//2):               # 회문의 길이 절반만큼 비교
        if txt[j+k] != txt[j+N-1-k]:
            break                       # 비교하는 위치가 다르면 현재 구간 중지
    else:                               # break에 걸리지 않고 for 종료, 회문이면
        total += 1
print(total)