T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 돌의 초기상태 저장
    info = list(map(int, input().split()))
    for _ in range(M):
        # i 번째부터 j 개의 돌
        i, j = map(int, input().split())
        i -= 1
        for s in range(i, min(i+j, N)):
            info[s] = info[i]

    print(f'#{tc}', *info)