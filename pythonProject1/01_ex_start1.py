# 입력받을 2진수
bin_num = input()
# 결과 담을 리스트
result = []
# 입력받은 2진수 7개씩 묶기
for i in range(0, len(bin_num), 7):
    # 7개씩 묶은 각각의 2진수
    binary = bin_num[i:i+7]
    # 10진수로 변환
    decimal_num = int(binary, 2)
    # 변환한 값 결과 리스트에 담기
    result.append(decimal_num)

print(" ".join(map(str, result)))