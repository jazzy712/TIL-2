def pattern_count(p, t):                # 패턴의 등장 횟수 패턴
    N = len(t)
    M = len(p)
    i = j = 0
    cnt = 0
    while i < N:
        if t[i] != t[j]:                 # 다른 경우
            i = i - j + 1                # i - j 비교를 시작했던 위치
            j = 0
        else:                            # 같은 경우
            i += 1
            j += 1
        if j == M:                       # 패턴을 찾은 경우
            cnt += 1
            i = i - j + 1
            j = 0
    return cnt

t= 'TTTTTATTAATA'
p = 'ATA'

print(pattern_count(p, t))

