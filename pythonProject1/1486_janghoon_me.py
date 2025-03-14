# 부분집합 !
T = int(input())
for tc in range(1, T+1):
    # 점원 수 N, 선반 높이 B
    N, B = map(int, input().split())
    Hi = list(map(int, input().split()))
    # 탑과 B의 높이 차이 엄청나게 큰 수로 설정
    result = int(21e8)

    # 모든 부분집합(점원으로 이루어진) 생성
    for i in range(1 << N):
        # 부분집합 합 초기화
        subset_sum = 0
        # 부분집합에 점원 1명 이상 있는지 여부 확인
        has_member = 0
        # 점원 수 만큼 반복
        for j in range(N):
            # i 번째 부분집합에 j 번째 점원 포함되어 있는지 확인
            if i & (1 << j):
                # 해당 점원 키 추가
                subset_sum += Hi[j]
                # 점원 있음
                has_member = 1
        # 만들 수 있는 높이가 B(선반 높이) 이상인 탑 중 탑과 B의 높이 차이 최소 구해야됨
        # 점원이 있고 키가 선반 높이 이상이라면
        if has_member == 1 and subset_sum >= B:
            dif = subset_sum - B
            result = min(result, dif)

    print(f'#{tc} {result}')
