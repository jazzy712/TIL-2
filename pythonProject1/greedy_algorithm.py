num = 456789    # Baby gin 확인할 6자리 수
c = [0] * 12    # 6자리 수로부터 각 자리수를 추출하여 개수 누적할 리스트

for i in range(6):
    c[num % 10] += 1
    num //= 10
i = 0
tri = run = 0
while i < 10:
    if c[i] >= 3:       # triplet 조사 후 데이터 삭제
        c[i] -= 3
        tri += 1
        continue;
    if c[i] >= 1 and c[i+1] and c[i+2] >= 1:    # run 조사 후 데이터 삭제
        c[1] -= 1
        c[i+1] -= 1
        c[i+2] -= 1
        run += 1
        continue
    i += 1

if run + tri == 2 : print("Baby Gin")
else : print("Lose")