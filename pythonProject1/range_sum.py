T = int(input())            # 테스트 케이스(T)의 갯수 입력

for i in range(1, T+1):          # 1부터 T까지 반복하는 테스트 케이스
    N, M = map(int, input().split())    # N : 정수의 갯수, M : 구간의 크기, 공백으로 구분해 입력
    num = list(map(int, input().split()))   # N개의 숫자 리스트로 입력

    max_sum = min_sum = sum(num[:M])                    # 첫 번째 구간의 합(0 ~ M-1)을 최댓값/최솟값으로 설정


    for j in range(1, N-M+1):                           # 두 번째 구간인 1부터 N-M까지 순회
        temp = sum(num[j:j+M])                          # 현재 구간의 합(temp) j부터 j+M 계산


        if max_sum < temp:
                max_sum = temp

        if min_sum > temp:
               min_sum = temp                           # minmax 이용해서 최댓값.최솟값 저장

    result = max_sum - min_sum                          # 구하고자 하는 (최댓값-최솟값) 할당
    print(f"#{i} {result}")                             # 테스트 케이스 번호(i)와 함께 result 출력
