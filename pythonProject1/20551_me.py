def eat_candy(A, B, C):
    # A,B,C 순서로 개수가 커져야 함
    # C = 2이면 B = 1이 되고 혹은 C값과 상관없이 B = 1이면, A는 0밖에 될 수 없음
    # 조건에서 모든 상자에 사탕이 하나씩 들어있어야 한다고 함
    # 불가능하므로 -1
    if B <= 1 or C <= 2:
        return -1
    # 이미 조건이 만족되어 있으면 사탕을 먹을 필요 없으므로 0
    if A < B < C:
        return 0
    # 먹은 사탕 갯수 초기화
    candy = 0
    # 두 번째 상자부터 계산하면 불필요한 계산 줄일 수 있음
    # 두 번째 상자가 세 번째 상자보다 사탕 갯수가 이상이라면
    if B >= C:
        # 먹은 갯수 추가
        candy += (B - (C - 1))
        # B는 C보다 하나만큼 더 작게 됨
        B = C - 1
    # 첫 번째 상자가 두 번째 상자보다 사탕 갯수가 이상이라면
    if A >= B:
        # 위와 동일
        candy += (A - (B - 1))
        A = B - 1

    return candy


T = int(input())

for tc in range(1, T+1):
    A, B, C = map(int, input().split())
    res = eat_candy(A, B, C)
    print(f'#{tc} {res}')
