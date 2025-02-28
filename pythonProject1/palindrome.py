def reverse_string(word):
    if not word:                                            # word가 비어있다면
        return word                                         # 빈 문자열 반환
    return f'{word[-1]}{reverse_string(word[:-1])}'         # 아니라면 현재 문자열의 마지막 문자에 나머지 문자열 재귀로 뒤집은 결과 반환

T = int(input())                                            # 테스트 케이스 개수
for tc in range(1, T+1):
    word = input()                                          # 검사할 word 입력
    reverse_word = reverse_string(word)                     # 입력받은 word 위 정의한 함수 활용하여 뒤집기
    if word == reverse_word:                                # word와 뒤집은 word가 같다면(회문이라면)
        result = 1                                          # 1 출력
    else:                                                   # 아니라면
        result = 0                                          # 0 출력
    print(f'#{tc} {result}')                                # 테스트 케이스 번호와 결과 출력