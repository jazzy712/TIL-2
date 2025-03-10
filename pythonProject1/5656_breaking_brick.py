'''
경우의 수를 다 봐야함
-> DFS
'''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def shoot(cnt, remains, now_arr):
    global min_blocks

    # 구슬을 모두 발사 or 남은 벽돌이 0이면
    if cnt == N or remains == 0:
        min_blocks = min(min_blocks, remains)
        return
    # 한 줄씩 떨구자
    for col in range(W):
        # 방법 1
        # 1. col 위치에 떨구기 전 상태를 복사(얕은 복사 주의)
        # 2. 복사한 리스트에 col 위치에 떨구기
        # 3. cnt+1 번 상태로 이동(다음 재귀 호출)
        # 4. 떨구기 전 상태로 복구

        # 방법 2(복구 시간이 없으니 더 효율적)
        # 1. col 위치에 떨구기 전 상태 복사
        # 2. 복사한 리스트에 col 위치에 떨구기
        # 3. cnt+1 번 사애로 이동 + col 위치에 떨군 상태를 함께 전달
        copy_arr = [row[:] for row in now_arr]

        # col 위치에 구슬 떨어뜨리기
        # 구슬을 쏘는 열에서 가장 위를 찾기
        row = -1
        for r in range(H):
            # 벽돌이 있으면
            if copy_arr[r][col]:
                row = r
                break
        # 벽돌이 없는 열이면 다음 열 확인
        if row == -1:
            continue
        # 깨질 벽돌들을 리스트에 담아야함
        # 행, 열, 숫자
        q = [(row, col, copy_arr[row][col])]
        # 남은 벽돌들을 계산할 변수
        now_remains = remains - 1
        # 구슬이 처음 만나는 벽돌 자리
        copy_arr[row][col] = 0
        # 주변 벽돌들이 깨짐
        while q:
            r, c, p = q.pop()
            # 숫자만큼 반복하면서 벽돌들이 깨짐
            for k in range(1, p):
                for i in range(4):
                    ny = r + (dy[i] * k)
                    nx = c + (dx[i] * k)
                    if ny < 0 or ny >= H or nx < 0 or nx >= W:
                        continue
                    if copy_arr[ny][nx] == 0:
                        continue
                    # 다음 벽돌 추가
                    q.append((ny, nx, copy_arr[ny][nx]))
                    # 벽돌 깨짐
                    copy_arr[ny][nx] = 0
                    # 숫자 감소
                    now_remains -= 1
            # 빈칸을 메꿔주어야 함
            for c in range(W):
                # 벽돌이 위치할 index
                idx = H - 1
                for r in range(H-1, -1, -1):
                    if copy_arr[r][c]:
                        copy_arr[r][c], copy_arr[idx][c] = copy_arr[idx][c], copy_arr[r][c]
                        idx -= 1
            shoot(cnt + 1, now_remains, copy_arr)


T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())

    # 1. 최소 벽돌 개수
    # 2. 현재 벽돌이 다 깨지면 더 이상 할 필요없음 -> 현재 벽돌 수 관리하자
    # 3. N번 굴리면 끝남
    # - 0번부터 시작, N 번까지 반복
    # - 무조건 몯 굴려보아야 정답이 나옴(DFS)
    # - 한 번 굴렸을 때 벽돌들이 연쇄로 깨짐
    #   - 현재 기준으로 퍼져나가면서 탐색(BFS)

    arr = [list(map(int, input().split())) for _ in range(M)]
    min_blocks = 1e9
    blocks = 0
    # 현재 벽돌 수 계산
    for row in arr:
        for el in row:
            # 1보다 크면 벽돌
            if el:
                blocks += 1

    shoot(0, blocks, arr)

    print(f'#{tc} {min_blocks}')