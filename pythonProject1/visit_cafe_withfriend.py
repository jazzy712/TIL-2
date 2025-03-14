friend = ['A', 'B', 'C', 'D', 'E']
n = len(friend)
# 모든 부분 집합 중 원소의 수가 2개 이상인 집합의 수
ans = 0


# 1인 bit 수를 반환하는 함수
def visit_cafe(tar):
    cnt = 0
    for i in range(n):
        if tar & 0x1:
            cnt += 1
        tar >>= 1
    return cnt


# 모든 부분집합을 확인
for target in range(1 << n):
    # 만약 원소의 개수가 2개 이상이면 ans += 1
    if visit_cafe(target) >= 2:
        ans += 1

print(ans)