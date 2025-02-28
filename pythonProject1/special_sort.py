def special_sort(a, N):                                 # 입력받은 리스트 a와 리스트 길이 N
    for i in range(N-1):                                # 선택 정렬로 오름차순 정렬
        min_idx = i                                     # 현재 위치 최솟값으로 초기화
        for j in range(i+1, N):                         # 현재 위치 다음부터 끝까지 반복
            if a[min_idx] > a[j]:                       # 현재의 값이 최솟값보다 작다면
                min_idx = j                             # 최솟값 업데이트
        a[i], a[min_idx] = a[min_idx], a[i]             # 현재 위치와 업데이트된 최솟값 위치 교환

    result = [0] * N                                    # 결과 지정할 리스트 생성
    left = 0                                            # 왼쪽 인덱스(작은 수) 시작 값 0 설정
    right = N-1                                         # 오른쪽 인덱스(큰 수) 시작 값 N-1 설정

    for k in range(10):                                 # 10개까지의 결과를 구한다고 했으므로 해당 범위 내에서 반복
        if k % 2 == 0:                                  # 짝수 인덱스일 때
            result[k] = a[right]                        # 오른쪽(큰 수)에서 값을 가져옴
            right -= 1                                  # 오른쪽 인덱스 왼쪽으로 한 칸 이동
        else:                                           # 홀수 인덱스일 때
            result[k] = a[left]                         # 왼쪽(작은 수)에서 값을 가져옴
            left += 1                                   # 왼쪽 인덱스 오른쪽으로 한 칸 이동
    return result[:10]                                  # 처음 10개의 값 반환

T = int(input())                                        # 테스트 케이스 개수
for tc in range(1, T+1):
    N = int(input())                                    # 리스트 길이(N)
    ai = list(map(int, input().split()))                # 숫자들을 리스트로 입력받음(ai)
    result = special_sort(ai, N)                        # 리스트 ai의 모든 요소를 처리하기 위해 마지막 인덱스인 N-1까지의 범위 함수 호출
    print(f'#{tc}', *result)
