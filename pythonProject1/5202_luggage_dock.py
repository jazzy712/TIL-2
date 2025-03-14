def luggage_dock(time_info):
    # 종료 시간 이른 순서로 정렬
    time_info.sort(key=lambda x : x[1])
    # 작업 횟수 초기화
    dock = 0
    # 종료 시간 초기화
    end_time = 0

    # 리스트 내 시작 시간(s)과 종료 시간(e) 순회
    for s, e in time_info:
        # 작업 종료하면 바로 다음 작업 시작한다 했음
        # 시작 시간이 종료 시간 다음이면
        if s >= end_time:
            # 작업 +1
            dock += 1
            # 종료 시간 갱신
            end_time = e
    return dock


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 작업 시작 시간과 종료 시간 입력받을 리스트
    time_info = [list(map(int, input().split())) for _ in range(N)]

    result = luggage_dock(time_info)
    print(f'#{tc} {result}')