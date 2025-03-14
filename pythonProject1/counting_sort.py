'''
0<=DATA[i]<=4 조건
'''
DATA = [0, 4, 1, 3, 1, 2, 4, 1]
N = len(DATA)

COUNTS = [0] * 5  # max(DATA) + 1 , 크기에 주의 !!

TEMP = [0] * N    # 정렬 결과 저장

for i in range(N):              # 각 숫자의 개수
    COUNTS[DATA[i]] += 1

print(COUNTS)

for i in range(1, 5):           # COUNTS[i]까지의 합계
    COUNTS[i] += COUNTS[i-1]

print(COUNTS)

for i in range(N-1, -1, -1):
    COUNTS[DATA[i]] -= 1        # DATA[i] 까지의 개수 1개 감소
    # DATA[i]까지 차지한 칸 수 중 가장 오른쪽에 DATA[i] 기록
    COUNTS[DATA[i]] = DATA[i]

print(TEMP)

