def binary_search(N, key):                      # 전체 페이지 수 : N
    left = 1                                    # 시작 페이지 : 1
    right = N                                   # 검색 범위 끝점 : 전체 페이지 수
    cnt = 0                                     # 탐색 횟수 카운트, 최초 값 0이라 설정
    while left <= right:                        # 왼쪽 페이지가 오른쪽 페이지 이하라면
        cnt += 1                                # 카운트 횟수 1씩 증가
        mid = (left + right) // 2               # 중간값 설정

        if mid == key:                          # 중간 페이지와 찾는 페이지가 일치하면
            return cnt                          # 현재까지의 시도 횟수 반환
        elif mid > key:                         # 중간 페이지가 찾는 페이지보다 크면
            right = mid - 1                     # 오른쪽 범위 조정
        else:                                   # 중간 페이지가 찾는 페이지보다 작으면
            left = mid + 1                      # 왼쪽 범위 조정

    return cnt

T = int(input())                            # 테스트 케이스 개수
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())       # 전체 페이지 수(P)와 A,B가 찾을 페이지 번호
    cnt_a = binary_search(P, Pa)                # A 탐색 횟수
    cnt_b = binary_search(P, Pb)                # B 탐색 횟수
    result = 0

    if cnt_a < cnt_b:                           # A가 B보다 적은 횟수라면
        result = 'A'                            # A 승
    elif cnt_a > cnt_b:                         # 반대라면
        result = 'B'                            # B 승

    print(f'#{tc} {result}')

