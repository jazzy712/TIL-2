# 암호코드 패턴과 숫자 매칭
code_dict = [
    [0, 0, 0, 1, 1, 0, 1],
    [0, 0, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 1, 1],
    [0, 1, 1, 0, 0, 0, 1],
    [0, 1, 0, 1, 1, 1, 1],
    [0, 1, 1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1, 1, 1],
    [0, 0, 0, 1, 0, 1, 1]
]

T = int(input())
# 테스트 케이스 수만큼 반복
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    # N 개의 줄에 걸친 2차원 배열
    arr = [list(map(int, input())) for _ in range(N)]

    # 암호코드를 저장할 변수 초기화
    code = []

    # 암호코드가 있는 행 찾기
    for i in range(N):
        # 주어진 예시에서 1은 거의 행의 끝 부분에 위치함
        # 현재 행에서 뒤에서부터 검색
        for j in range(M - 1, -1, -1):
            # 1이 있는 칸을 찾으면
            if arr[i][j] == 1:
                # 암호코드는 56자리이므로 끝 위치에서 55자리 앞부터 끝까지를 추출
                # 유효한 인덱스 범위인지 확인
                if j >= 55:
                    code = arr[i][j - 55:j + 1]
                    break
        # 암호코드를 찾았으면 더 이상 행을 검색할 필요 없음
        if code:
            break

    # 7자리씩 끊어 담을 리스트 생성
    numbers = []

    # 0부터 56까지 7씩 증가하며 반복
    for i in range(0, 56, 7):
        # 7자리씩 슬라이싱
        pattern = code[i:i + 7]
        # 패턴이 암호코드 패턴에 있으면
        if pattern in code_dict:
            # 숫자를 리스트에 추가
            numbers.append(code_dict.index(pattern))
    # 8개의 숫자를 모두 찾으면
    if len(numbers) == 8:
        # 홀수 자리의 합 계산
        odd_sum = numbers[0] + numbers[2] + numbers[4] + numbers[6]
        # 짝수 자리의 합 계산
        even_sum = numbers[1] + numbers[3] + numbers[5] + numbers[7]
        # (홀수 자리의 합 × 3) + 짝수 자리의 합이 10의 배수인지 확인
        if (odd_sum * 3 + even_sum) % 10 == 0:
            # 맞으면 숫자들의 합 출력
            print(f"#{tc} {sum(numbers)}")
        else:
            # 아니라면 0 출력
            print(f"#{tc} 0")
    else:
        # 8개의 숫자를 찾지 못했으면 잘못된 암호코드이므로 0 출력
        print(f"#{tc} 0")

