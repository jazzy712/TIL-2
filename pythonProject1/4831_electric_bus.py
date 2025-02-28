def charge():
    pass

T = int(input())
for tc in range(1, T + 1):
    # 정류장 개수 N, 한 번에 최대 이동 정류장 K, 충전기 설치된 정류장 개수 M
    K, N, M = map(int, input().split())
    # 충전소 위치 목록 받을 리스트 생성
    charge = list(map(int, input().split()))
    # 정류장 배열 리스트(N+1개 만큼)
    station = [0] * (N + 1)

    # 충전소 위치 중
    for i in charge:
        # 정류장에 충전소가 있다면 1 할당
        station[i] = 1
        # 충전 횟수 0으로 초기값 설정
        cnt = 0
        # 현재 위치 0(0번에서 출발)
        now = 0
        # 종점에 이르기까지 반복
        while now < N:
            # 만약 현재 거리에서 최대 거리 이내에 종점이 있다면?
            if now + K >= N:
                # 중단
                break
            # 다음 충전소 위치 next_charge
            # 초기값 0으로 설정하면 출발점이 0부터이므로 범위 이내에 찾지 못했을 때
            # 계속 0(출발점)으로 초기화할 수 있음
            # 따라서 정류장 번호가 아닌 -1로 초기화
            next_charge = -1
            # 다음 위치부터 최대 이동거리까지 충전소 찾기
            for j in range(now + 1, now + K + 1):
                # 종점 이전에 충전소를 찾으면?
                if j <= N and station[j] == 1:
                    # 다음 충전소 위치 현재 위치로 초기화
                    next_charge = j
                    break
            # 충전소 찾지 못했다면?
            if next_charge == -1:
                # 충전 못함
                cnt = 0
                break
            # 충전소 찾았으면 다음 충전소로 이동
            now = next_charge
            # 충전 횟수 1씩 증가
            cnt += 1

    print(f'#{tc} {cnt}')

