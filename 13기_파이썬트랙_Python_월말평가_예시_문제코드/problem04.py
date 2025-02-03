############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_id_valid(user_data):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    id_data = user_data.get('id', '')  # 'id' 값을 가져오고 기본값은 빈 문자열
    if id_data:  # id가 비어있지 않으면
        last_char = id_data[-1]  # 마지막 문자
        return '0' <= last_char <= '9'  # 마지막 문자가 '0'에서 '9' 사이의 숫자라면 True
    return False  # id가 비어있다면 False 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': 'jungssafy5',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data1)) # True


user_data2 = {
    'id': 'kimssafy!',
    'password': '1q2w3e4r',
}
print(is_id_valid(user_data2)) # False
#####################################################