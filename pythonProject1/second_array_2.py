'''
문제 시나리오
`N × N` 크기의 정사각형에서, **왼쪽 위 좌표는 `(0, 0)`**, 오른쪽 아래 좌표는 `(4, 4)`이다.
입력으로 `(0, 0)`에서 출발하여 이동할 때 필요한 **방향 정보**가 여러 줄에 걸쳐 주어진다.
방향 문자는 `n, e, w, s` 이며, 각각 한 칸씩만 이동한다. (대각선 이동은 없음)
정사각형 범위를 벗어나는 입력은 없다고 가정한다.
'''
'''
# input.txt

4
e e s s w n
e e s s s s
s s s e e e
s s e e n e
'''
# import sys
# sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    r,c = 0, 0
    dr = [-1, 1, 0, 0]   # n, s, e, w
    dc = [0, 0, 1, -1]
    dir = ['n', 's', 'e', 'w']
    arr = input().split()

    for cmd in arr:
        for i in range(len(dir)):
            if cmd == dir[i]:
                nr = r + dr[i]
                nc = c + dc[i]
                r,c = nr, nc

    print(f'#{tc} {r} {c}')
