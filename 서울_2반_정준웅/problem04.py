############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장 함수 set, sum 등 사용 시 감점

def analyze_items(items_list):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not items_list:
        return ([], (0,0))
    unique_items = []
    for item in items_list:
        if item not in unique_items:
            unique_items.append(item)

    sum_numbers = 0
    min_number = None
    has_number = False
    
    for item in items_list:
        if isinstance(item, (int, float)):  # 숫자인 경우
            has_number = True
            sum_numbers += item
            if min_number is None or item < min_number:
                min_number = item
    
    # 숫자가 없는 경우
    if not has_number:
        return (unique_items, (0, 0))
    
    return (unique_items, (sum_numbers, min_number))


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(analyze_items([2, 2, 2, "a", "a", 3, 0, -2]))
# 예시 결과: ([2, "a", 3, 0, -2], (5, -2))

print(analyze_items([]))
# 예시 결과: ([], (0, 0))

print(analyze_items(["apple", "apple", "banana"]))
# 예시 결과: (["apple", "banana"], (0, 0))
#####################################################
