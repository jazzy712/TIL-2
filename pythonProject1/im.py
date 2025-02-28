# 1. 공굴리기
def rolling_ball(arr, N):
    # 0. 상하좌우 델타 선언
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    max_cnt = 0

    # 1. 각 자리를 전부 돌면서 공굴리기의 스타트 지점으로 계산
    for i in range(N):
        for j in range(N):
            # 이동 칸을 셀 변수
            cnt = 1
            ni = i
            nj = j

            # 1.0 다음 값이 범위를 벗어나지 않을동안 계속 이동
            while 0 <= ni < N and 0 <= nj < N:
                # print(i, j, arr[i][j])
                # 현재 자리의 값
                curr_val = arr[ni][nj]

                # 현재 자리 값보다 작은 값들을 넣을 임시 리스트
                min_dict = {}

                # 1.1 상하좌우를 탐색하면서
                for k in range(4):
                    nni = ni + di[k]
                    nnj = nj + dj[k]

                    # 1.2 만약 범위를 벗어나지 않으면서 현재 값보다 작다면
                    if 0 <= nni < N and 0 <= nnj < N and arr[nni][nnj] < curr_val:
                        # 1.3 임시 변수에 저장 (작은 값이 여러개 일 수 있기 때문)
                        min_dict[arr[nni][nnj]] = [nni, nnj]
                    else:

                        continue

                # 가장 최소값의 인덱스로 이동
                if min_dict:
                    ni, nj = min_dict.get(min(min_dict.keys()))
                    cnt += 1
                else:
                    break

            max_cnt = max(max_cnt, cnt)

    return max_cnt


T = int(input().strip())

for tc in range(1, T + 1):
    N = int(input().strip())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = rolling_ball(arr, N)
    print(f'#{tc} {ans}')