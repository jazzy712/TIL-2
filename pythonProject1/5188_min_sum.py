# 가능한 모든 경로 탐색하므로 dfs
def


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    # NxN 행렬
    matrix = [list(map(int, input().split())) for _ in range(N)]

