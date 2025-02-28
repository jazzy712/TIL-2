T = int(input())

for tc in range(1, T+1):
    # 입력받을 문자열 str1, str2 설정
    str1 = input()
    str2 = input()
    # 가장 많은 글자 세는 빈 딕셔너리(각 글자마다 key 설정 후 등장 횟수 value 설정)
    char_count = {}

    # str1 내 각 글자에 대해
    for char in str1:
        # key 값 i 글자에 대한 value 값 0 설정
        char_count[char] = 0
    # 동일하게 str2 내 각 글자에 대해
    for char in str2:
        # 딕셔너리 내에 key 값 i 글자가 있다면
        if char in char_count:
            # key 값 i에 대응하는 value 값 1씩 상승
            char_count[char] += 1

    # 딕셔너리에서 value 값이 가장 큰 글자 갯수 max 이용해서 출력
    result = max(char_count.values())
    print(f'#{tc} {result}')