def pw_creator(arr):
    #  초기값 1부터
    i = 1
    # 계속 반복
    while True:
        # 맨 앞 숫자 i씩 감소
        front = arr[0] - i
        # 첫 번째 숫자 제거하고
        arr.pop(0)
        # 숫자가 0보다 클 때
        if front > 0:
            # 맨 뒤에 숫자 추가
            arr.append(front)
        # 0보다 작다면
        else:
            # 맨 뒤에 0 추가
            arr.append(0)
            # 0 추가 됐으므로 중단
            break
        # i가 1부터 5까지 순환해야함
        i = (i % 5) + 1
    # 이 때, 8자리의 숫자 값이 결과
    # arr 은 정수 형태이므로 문자열로 변환
    # 하나의 문자열로 결합해서 반환
    return ' '.join(map(str, arr))


T = 10

for tc in range(1, T+1):
    # 입력받은 데이터 N
    N = int(input())
    # 8개 숫자 입력
    arr = list(map(int, input().split()))

    res = pw_creator(arr)
    print(f'#{tc} {res}')
