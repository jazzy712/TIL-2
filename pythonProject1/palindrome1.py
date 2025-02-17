# 문자열 뒤집는 재귀함수
def reverse_string(word):
    # 빈 문자열이면 그대로 반환
    if not word:
        return word
    # 재귀적으로 뒤집는 방법
    return f'{word[-1]}{reverse_string(word[:-1])}'


# 10개의 테스트 케이스
T = 10

for tc in range(1, T+1):
    # 회문 길이 N
    N = int(input())
    # 8x8 크기의 2차원 배열 생성(글자판에 공백없이 문자가 입력되므로 split() 사용x)
    # 회문을 사용하려면 문자 자체를 비교해야 하므로 map()도 사용하지 않는다
    arr = [list(input()) for _ in range(8)]

    # 회문 갯수 count 하는 변수
    count = 0

    # 가로 행 회문 검사
    for r in range(8):
        # 문자의 첫 위치
        for i in range(8 - N + 1):
            # 길이 N 만큼의 단어 추출
            word = arr[r][i:i+N]
            # 추출한 단어가 회문인지 검사
            # ''.join(word) -> word 리스트를 문자열로 변환
            # 위에서 정의한 reverse_string 함수를 통해 문자열 뒤집음
            # list() -> 뒤집은 문자열 다시 리스트 변환하여 회문인지 비교
            if word == list(reverse_string(''.join(word))):
                # 맞다면 회문 갯수 1씩 증가
                count += 1
    # 세로 열 회문 검사
    for c in range(8):
        # 문자의 첫 위치
        for i in range(8 - N + 1):
            # 행은 이미 연속된 메모리이기 때문에 가로 행은 슬라이싱 통해 접근이 가능하지만
            # 세로 열은 메모리상 연속되어 있지 않아 인위적으로 반복문을 통해 문자를 하나씩 수집해야함
            # 세로 방향 단어 저장할 리스트
            word = []
            # 길이 N 만큼의 문자 수집(현재 위치에서 몇 번째 문자인지)
            for j in range(N):
                # 리스트에 i+j번째 행, c번째 열의 문자 추가
                word.append(arr[i+j][c])
            # 위와 동일한 방법으로 회문인지 검사
            if word == list(reverse_string(''.join(word))):
                # 맞다면 회문 갯수 1씩 증가
                count += 1
    print(f'#{tc} {count}')



