T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = list(map(int, input().split()))

    for _ in range(M):
        a, b, c = map(int, input().split())
        b -= 1
        # 기준번호 b 번 기준으로 앞뒤로 i번 상태 같으면 바꿈, 다르면 그대로
        # 범위 c 이내에서
        for i in range(1, c+1):
            # 왼쪽, 오른쪽 인덱스
            left = b - i
            right = b + i
            # 인덱스가 유효한 경우에만
            if left >= 0 and right < N:
                # 상태 같으면 바꿔주기
                if flag[left] == flag[right]:
                    flag[left] = 1 - flag[left]
                    flag[right] = 1 - flag[right]

    print(f'#{tc}', *flag)