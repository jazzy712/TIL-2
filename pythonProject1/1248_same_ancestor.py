T = int(input())

for tc in range(1, T+1):
    # 정점 개수 V, 간선 개수 E, 공통 조상 찾는 두 개의 정점 번호 i,j
    V, E, i, j = map(int,input().split())
    # 간선 정보
    info = list(map(int, input().split()))
    left = [0] * (V + 1)
    right = [0] * (V + 1)
    