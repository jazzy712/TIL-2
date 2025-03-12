# Baby Gin 문제를 해결하는 함수
def is_baby_gin():
    # run 또는 triplet 이 있는 경우 카운트
    count = 0
    # 카드 6장 중 3장씩 볼 예정
    for i in range(0, 6, 3):
        a, b, c = current_path[i], current_path[i+1], current_path[i+2]
        # triplet 확인
        if a == b == c:
            count += 1
        # run 확인
        elif a == (b-1) == (c-2):
            count += 1
    return count == 2


# 순열을 생성하는 함수
def generate_permutations(current_count):
    # 카드 6개 고르면 그만
    if current_count == 6:
        # 고른 6개의 카드가 Baby Gin 이라면 1
        if is_baby_gin():
            return 1
        return 0

    # 카드 고르기
    for idx in range(6):
        # 아직 사용하지 않은 카드의 idx 만 추가
        if not used_cards[idx]:
            used_cards[idx] = 1
            current_path.append(input_cards[idx])
            result = generate_permutations(current_count + 1)
            # 결과가 1이라면 즉시 반환
            if result == 1:
                return result
            # 1이 아니면 pop 하고 다시 0 할당
            current_path.pop()
            used_cards[idx] = 0
    # 모든 경우에 결과가 1이 아니면 0 반환
    return 0


# 테스트 케이스 수
T = int(input())

for tc in range(1, T+1):
    # 입력받을 숫자 리스트
    input_cards = list(map(int, input()))
    current_path = []
    used_cards = [0] * 6
    res = generate_permutations(0)

    print(f'#{tc} {res}')
