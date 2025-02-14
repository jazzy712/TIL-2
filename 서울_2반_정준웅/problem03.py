############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 제공 메서드 count 사용 시 감점

def find_most_populated(animal_map):
    

    # 여기에 코드를 작성하여 함수를 완성합니다.
    if not animal_map:
        return None
    max_count = -1
    max_animal = None

    for animal,count in animal_map.items():
        if count > max_count:
            max_count = count
            max_animal = animal
        # 개체수가 같은 경우, 사전순으로 더 앞선 동물을 선택
        elif count == max_count and (max_animal is None or animal < max_animal):
            max_animal = animal
    
    return max_animal

    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하거나 수정하지 마세요.
# 모든 책임은 삭제 혹은 수정한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
print(find_most_populated({"lion": 5, "tiger": 3, "elephant": 10}))  # 예시: "elephant"
print(find_most_populated({}))                                       # None
print(find_most_populated({"wolf": 4, "wolfdog": 4, "hyena": 4}))     # "wolf"
#####################################################
