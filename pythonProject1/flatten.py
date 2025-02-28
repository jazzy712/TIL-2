T = 10

for tc in range(1, T+1):
    # 덤프 횟수 dp
    dp = int(input())
    # 박스 높이 box_len(입력받은 값 정수 리스트로 나열)
    box_len = list(map(int, input().split()))

    # 덤프 횟수 x번 동안
    for x in range(dp):
        # 상자 높이의 최댓값
        max_len = max(box_len)
        # 상자 높이의 최댓값의 인덱스
        max_idx = box_len.index(max(box_len))
        # 상자 높이의 최솟값
        min_len = min(box_len)
        # 상자 높이의 최솟값의 인덱스
        min_idx = box_len.index(min(box_len))
        # 최댓값 - 최솟값이 1 이하면 중단
        if max_len - min_len <= 1:
            break
        # 수행마다 상자 높이의 최댓값은 1씩 줄고, 최솟값에서 1씩 늘음
        max_len -= 1
        min_len += 1
        # 상자 높이의 최댓값과 최솟값을 다시 갱신시켜야함
        box_len[max_idx] = max_len
        box_len[min_idx] = min_len

    result = max(box_len) - min(box_len)

    print(f'#{tc} {result}')
