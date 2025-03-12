T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 깃발 상태 입력할 배열
    flag = list(map(int, input().split()))
    for _ in range(M):
        a, b, c = map(int, input().split())
        # 기준 번호 1인데 인덱스는 0부터 시작
        # 명령 리스트에 b는 b-1부터 시작
        b -= 1
        # b 번부터 c 명까지 처리
        # 줄 넘어가면 N 번까지
        for i in range(b, min(b+c, N)):
            # 깃발 상태 변경
            flag[i] = 1 - flag[i]

    print(f'#{tc}', *flag)

