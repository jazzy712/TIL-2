T = int(input())                            # 테스트 케이스 갯수 입력

for i in range(1, T+1):                     # 1부터 T까지 순회
    N = int(input())                        # 카드 장수 N
    ai = list(map(int, input()))            # 문자열을 정수로 받고 리스트 형태로 저장

    count_num = [0] * 10                    # 0~9의 숫자 담을 리스트(count_num) 설정
    for j in range(N):
        count_num[ai[j]] += 1               # 리스트 ai의 숫자를 인덱스를 사용해서 개수 세기

        max_num = 0                         # 최다 카드의 숫자 0이라 설정
        max_cnt = 0                         # 최다 카드의 장 수 0이라 설정

        for tc in range(10):                # 0부터 9까지 순회
            if count_num[tc] >= max_cnt:    # 현재 카드의 개수가 최다 카드의 장 수보다 이상이면
                max_cnt = count_num[tc]     # 최다 카드 장 수 업데이트
                max_num = tc                # 자동으로 최다 카드 숫자가 현재 카드 숫자로 업데이트
    print(f"#{i} {max_num} {max_cnt}")   # 구하고자 하는 최다 카드의 숫자와 장 수를 테스트 케이스 번호에 맞춰 출력




'''            
가장 많은 카드의 숫자와 장 수
'''
'''
3
5
49679
5
08271
10
7797946543
'''
