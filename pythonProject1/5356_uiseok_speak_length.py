T = int(input())

for tc in range(1, T+1):
    # 문자열 배열 생성
    string = [list(map(str, input())) for _ in range(5)]
    # 출력해낼 글자
    word = []
    # 가장 길이가 긴 단어 초기화
    max_length = 0
    # 각 단어의 길이 저장할 리스트
    lengths = []
    # 문자열 순회하며 리스트에 각각의 길이 추가
    for char in string:
        lengths.append(len(char))
    # 가장 긴 단어의 길이 갱신
    max_length = max(lengths)
    # 갱신 후 세로로 읽을 예정
    for i in range(max_length):
        # 단어 5개 중에서
        for j in range(5):
            # 가장 긴 단어보다 단어가 짧다면
            if i < lengths[j]:
                # 리스트에 추가
                word.append(string[j][i])
    result = ''.join(word)
    print(f'#{tc} {result}')

