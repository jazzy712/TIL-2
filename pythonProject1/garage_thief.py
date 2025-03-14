n = 3
target = 30
# (kg, 가격)
things = [(5, 50), (10, 60), (20, 140)]

# 내림차순
things.sort(key= lambda x:(x[1] / x[0]), reverse=True)

sum = 0
for kg, price in things:
    per_price = price / kg

    # 만약 가방에 남은 용량이 얼마되지 않는다면
    # 물건을 잘라 가방에 넣고 끝냄
    if target < kg:
        sum += target * per_price
        break
    sum += price
    target -= kg

print(int(sum))