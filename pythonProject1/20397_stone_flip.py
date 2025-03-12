T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 돌의 초기상태 저장
    info = list(map(int, input().split()))
    for _ in range(M):
        i, j = map(int, input().split())
        i -= 1
        for s in range(1, j+1):
            left = i - s
            right = i + s
            if left >= 0 and right < N:
                if info[left] == info[right]:
                    info[left] = 1 - info[left]
                    info[right] = 1 - info[right]

    print(f'#{tc}', *info)