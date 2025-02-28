T = int(input())

for tc in range(1, T+1):
    # 테스트 케이스 번호와 단어 갯수 입력
    case_num, N = input().split()
    # 공백으로 구분된 단어들 리스트로 입력
    arr = list(input().split())
    # 각 문자에 맞춘 숫자 짝 딕셔너리 설정
    num_dict = {
                  "ZRO": 0,
                  "ONE": 1,
                  "TWO": 2,
                  "THR": 3,
                  "FOR": 4,
                  "FIV": 5,
                  "SIX": 6,
                  "SVN": 7,
                  "EGT": 8,
                  "NIN": 9,
    }

    # bubble sort 사용하여 정렬
    # 전체 리스트 순회(배열의 모든 요소 정렬)
    for i in range(len(arr)-1):
        # 정렬되지 않은 리스트 순회
        # 한 번 순회마다 가장 큰 값이 맨 뒤로 이동
        # 매 반복마다 이미 정렬된 뒷부분 제외
        for j in range(len(arr)-1-i):
            # 현재 값의 딕셔너리 값이 다음 값의 딕셔너리 값보다 크다면
            if num_dict[arr[j]] > num_dict[arr[j+1]]:
                # 순서 swap
                arr[j], arr[j+1] = arr[j+1], arr[j]

    print(case_num)
    # 리스트 정렬하여 출력
    print(' '.join(arr))






