T = int(input())                                                    # 테스트 케이스 개수

for tc in range(1, T+1):
    N, M = map(int, input().split())                                # 행의 개수(N)와 열의 개수(N) 공백으로 받아 입력받음
    arr = [list(map(int, input().split())) for _ in range(N)]       # N개의 행에 대해 M개의 정수로 2차원 배열 형성

    max_sum = 0                                                     # 꽃가루의 합 최대값의 초기값 설정

    for i in range(N):                                              # 행 순회
        for j in range(M):                                          # 열 순회
            pollen_sum = arr[i][j]                                  # 현재 선택한 풍선의 꽃가루의 개수
            dr = [-1, 1, 0, 0]
            dc = [0, 0, -1, 1]                                      # 상,하,좌,우

            for k in range(4):                                      # 4방향에 대해 확인
                for r in range(1, arr[i][j]+1):                     # 현재 풍선의 꽃가루 개수만큼 각 방향으로 퍼짐

                    ni = i + dr[k] * r                              # r은 1부터 현재 풍선의 꽃가루 개수만큼 증가하므로 이를 고려하면
                    nj = j + dc[k] * r                              # 방향 벡터에 r을 곱해야 현재 꽃가루 개수만큼의 거리 계산 가능

                    if 0 <= ni < N and 0 <= nj < M:                 # 벽의 범위를 세워 범위 내에 있는지 확인
                        pollen_sum += arr[ni][nj]                   # 범위 내 있다면 해당 위치 꽃가루 개수 더함

            max_sum = max(max_sum, pollen_sum)                      # 최대값 계산

    print(f'{tc} {max_sum}')                                        # 테스트 케이스 번호와 함께 꽃가루 최대합 산출
