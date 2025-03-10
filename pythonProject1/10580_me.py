T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # 전선 정보 저장할 배열 생성
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 교차점 세는 변수 초기화
    cnt = 0
    # 교차점은 첫 번째 줄의 시작점이 두 번째 줄보다 아래에 있고 끝점이 두 번째 줄보다 위에 있을때
    # 혹은 첫 번째 시작점이 두 번째보다 위에 있고 끝점이 두 번째보다 밑에 있을 때
    # 생성
    # 전선 개수 N 개 중
    # 첫 번째 전선 i
    for i in range(N):
        # 두 번째 전선 j
        for j in range(i+1, N):
            # 첫 번째 전봇대 Ai 와 두 번째 전봇대 Bi(첫 번째 전선 i)
            Ai, Bi = arr[i][0], arr[i][1]
            # 두 번째 전선 j의 전봇대 값
            Aj, Bj = arr[j][0], arr[j][1]
            # 위에서 말한 교차점의 첫 번째 조건
            if Ai < Aj and Bi > Bj:
                # 교차점 추가
                cnt += 1
            # 두 번째 조건
            if Ai > Aj and Bi < Bj:
                cnt += 1
    print(f'#{tc} {cnt}')



