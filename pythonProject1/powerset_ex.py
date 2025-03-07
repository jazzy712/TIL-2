# 3개의 사용 위치
# depth : 현재 원소를 선택 하냐 마냐를 가리키는 index
def create_subset(depth, included):
    if depth == len(input_list):
        cnt_subset = [input_list[i] for i in range(len(input_list)) if included[i]]
        subsets.append(cnt_subset)
        return
    # 선택하지 않는 경우
    included[depth] = False
    create_subset(depth + 1, included)

    # 선택하는 경우
    included[depth] = True
    create_subset(depth + 1, included)


# 주어지는 집합
input_list = [1, 2, 3]
# 구한 부분집합 저장할 변수
subsets = []
# selected 와 같은 역할
# 각 위치의 값을 선택하나/마나를 저장할 변수
# n = 3 -> [False, False, False]
init_included = [False] * len(input_list)
# 재귀적으로 들어감
create_subset(0, init_included)
print(subsets)