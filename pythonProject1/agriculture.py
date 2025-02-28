T = int(input())

for tc in range(1, T+1):
    # 농장의 크기 N
    N = int(input())
    # NxN 크기의 2차원 배열(각 빈칸은 공백없이 채워지기 때문에 split은 쓸 필요 없음)
    farm = [list(map(int, input())) for _ in range(N)]

    # 정가운데 행 기준으로 상,하로 나누어 마름모 내 농장의 수익을 구하고자 함
    # 정가운데 행은 모두 마름모, 즉 농장에 포함
    # 정 가운데 행의 인덱스 값
    mid_row = N // 2
    # 농장 전체 수익
    earn_farm = 0

    # 정 가운데 행은 모두 마름모(수확 범위)에 포함되므로 수익에 모두 더함
    earn_farm += sum(farm[mid_row])

    # 중앙의 행 기준 마름모 위쪽 순회(0부터 정 가운데 행전까지의 범위)
    for i in range(mid_row):
        # 시작점은 중앙에서 현재 행만큼 뺀 위치
        start = mid_row - i
        # 끝 점은 중앙에서 현재 행만큼 더하고 1을 더함(다음 함수에서 end-1 까지만 순회하므로)
        end = mid_row + i + 1
        # 수확 범위 설정
        for j in range(start, end):
            # 수익 계산
            earn_farm += farm[i][j]

    # 중앙의 행 기준 마름모 아래쪽 순회(정 가운데 행 다음부터 끝 범위까지)
    for i in range(mid_row + 1, N):
        # 각 행에서 수확할 범위?
        # 시작점은 현재 행에서 중앙값을 뺀 위치
        start = i - mid_row
        # 끝점은 현재 행에서 전체 크기 N에서 (현재 행 - 중앙값)을 뺀 위치
        end = N - (i - mid_row)
        # 수확 범위 설정
        for j in range(start, end):
            # 수익 계산
            earn_farm += farm[i][j]

    print(f'#{tc} {earn_farm}')


