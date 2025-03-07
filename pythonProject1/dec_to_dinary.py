target = 74

# 10진수 -> 2진수
def dec_to_binary(target):
    binary_number = ""

    while target > 0:
        remain = target % 2
        binary_number = str(remain) + binary_number
        target = target // 2
    print(binary_number)


# 2진수 -> 10진수
def binary_to_decimal(binary_str):
    # 1. binary_str 문자열 뒤에서부터 진행
    # 2. 각 자리에 맞는 수를 곱하면서, 결과에 더한다
    decimal_number = 0
    # 지수
    pow = 0

    for digit in reversed(binary_str):
        if digit == '1':
            decimal_number += 2 ** pow
        pow += 1

    print(decimal_number)


dec_to_binary(target)
binary_to_decimal("1001010")

# 10진수 -> 16진수
def decimal_to_hexadecimal(target):
    hex_digit = "0123456789ABCDEF"
    hex_number = ""

    while target > 0:
        remain = target % 16
        hex_number = hex_digit[remain]
        target //= 16
    print(hex_number)


decimal_to_hexadecimal(256)
