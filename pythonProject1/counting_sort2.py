def Counting_Sort(DATA, TEMP, k):
# DATA [] -- 입력 배열(원소는 0 이상 k 이하 정수)
# TEMP [] -- 정렬된 배열
# COUNTS [] -- 카운트 배열

    COUNTS = [0] * (k+1)

    for i in range(len(DATA)):
        COUNTS[DATA[i]] += 1

    for i in range(1, k+1):
        COUNTS[i] += COUNTS[i-1]
    for i in range(len(DATA)-1, -1, -1):
        COUNTS[DATA[i]] -= 1
        TEMP[COUNTS[DATA[i]]] = DATA[i]