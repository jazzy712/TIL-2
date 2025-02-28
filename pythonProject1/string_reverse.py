def reverse_string(word):
    if not word:                                                # word가 비어있다면
        return  word                                            # 빈 문자열 반환
    return f'{word[-1]}{reverse_string(word[:-1])}'             # 아니라면 현재 문자열의 마지막 문자에 나머지 문자열 재귀로 뒤집은 결과 반환

T = int(input())                                                # 테스트 케이스 개수
for tc in range(1, T+1):
    print(f'{tc} {reverse_string(input())}')                    # 테스트 케이스 번호와 입력받은 문자열 뒤집은 결과 출력