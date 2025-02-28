# N = int(input())
# arr = [list(map(int, input(). split())) for _ in range(N)]
#
# for i in range(N):
#     for j in range(M):
#             print(arr[i][j])
#
#
# '''
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# '''
#
# # i 행의 좌표
# # j 행의 좌표
#
# for i in range(n):
#     for j in range(m):
#         f(array[i][j + (m-1-2*j) * (i%2)])
#
# for i in range(n):
#     for j in range(m):
#         if i%2==0:
#             f(array[i][j])
#         elif i%2:
#             f(array[i[m-1-j]])
#
# # 델타를 이용한 2차원 배열
#
# di[] <- [0, 1, 0, -1]   # 방향별로 더할 값
# dj[] <- [1, 0, -1, 0]
#
# for k : 0 -> 3
#     ni <- i + di[k]
#     nj <- j + dj[k]

# di = [0, 1, 0, -1]         # 오른쪽부터 시계방향으로
# dj = [1, 0, -1, 0]
#
#
# i = 2
# j = 3
# for dir in range(4):
#     ni = i + di[dir]
#     nj = j + dj[dir]
#     print(ni, nj)
#
# di = [0, 1, 0, -1]         # 오른쪽부터
# dj = [1, 0, -1, 0]
#
# N = 2
# M = 3
# for i in range(N):
#     for j in range(M):
#         for dir in range(4):
#             ni = i + di[dir]
#             nj = j + dj[dir]
#             if 0<=ni<N and 0<=nj<M:         # 움수의 값이 못 나오게 할 때
#                  print(ni, nj)
#
#
# arr[0...N-1][0...N-1]   # NxN 배열
# di[] <- [0, 1, 0, -1]
# dj[] <- [1, 0, 1, 0]
# for i : 0 -> N-1:
#     for j : 0 -> N-1:
#         for d in range(4):
#                 ni <- i + di[d]
#                 nj <- j + dj[d]
#                 if 0<=ni<N and 0<=nj<N      # 유효한 인덱스면
#                         f(arr[ni][nj])


# N = 2
# M = 3
# for i in range(N):
#     for j in range(M):
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:
#             ni = i + di
#             nj = j + dj
#             if 0<=ni<N and 0<=nj<M:
#                 print(ni, nj)
#
#
# max_v = 0
# for i in range(N):
#     for j in range(N):
#         s = arr[i][j]       # i,j를 중심으로
#         for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:  # 각 방향
#             for c in range(1, k+1):                 # 거리별
#                 ni, nj = i+di*c, j+dj*c
#                 if 0<=ni<N and 0<=nj<N:
#                     s += arr[ni][nj]
#         if max_v < s:
#             max_v =s
#
#
# # 전치 행렬
# # i : 행의 좌표, len(arr)
# # j : 열의 좌표, len(arr[0])
# arr = [[1,2,3],[4,5,6],[7,8,9]]     # 3*3 행렬
#
# for i in range(3):
#     for j in range(3):              # for j in range(i): 인 경우
#         if i < j:                   #       if 문 필요없음
#             arr [i][j], arr[j][i] = arr[j][i], arr[i][j]
#
# # 연습문제1
# # 5x5 2차원 배열에 25개의 숫자를 저장하고,
# # 대각선 원소의 합을 구하시오.
#
# s = 0
# for i in range(5):
#     s += A[i][i]
#     s += A[i][4-i]
#     s -= A[5//2][5//2]      # 행과 열 크기가 홀수인 경우에 필요


# 연습문제2
# 5x5 2차원 배열에 25개의 숫자를 저장하고,
# 25개의 각 요소에 대해서 그 요소와 이웃한 요소와의 차의 절댓값을 구하시오
# 예를 들어 7값의 이웃한 값은 2,6,8,12이며 차의 절댓값의 합은 12이다
# 25개의 요소에 대해서 모두 조사하여 총합을 구하시오
# 벽에 있는 요소는 이웃한 요소가 없을 수 있음을 주의하시오

T = int(input())                                                    # 테스트 케이스 개수

for tc in range(1, T+1):                                            # 1부터 T까지 순회
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0                                                       # 이웃한 요소의 합 0이라 설정

    for i in range(N):
        for j in range(N):
            for di, dj in [[0,1],[1,0],[0,-1],[-1,0]]:              # 행과 열의 이동거리 순회
                ni = i + di                                         # 이동한 행 좌표
                nj = j + dj                                         # 이동한 열 좌표
               if 0<=ni<N and 0<=nj<N:                              # 이동한 행과 열의 좌표가 범위 내에 있다면
                    if arr[ni][nj] < arr[i][j]:                     # 이웃한 값이 현재 값보다 작다면
                        total += (arr[i][j] - arr[ni][nj])          # (현재값 - 이웃한 값) 만큼 더함
                    else:                                           # 반대의 경우
                        total += (arr[ni][nj] - arr[i][j])          # (이웃한 값 - 현재값) 만큼 더함

    print(f'#{tc} {total}')                                         # 테스트케이스 번호와 해당하는 이웃한 값의 합 출력