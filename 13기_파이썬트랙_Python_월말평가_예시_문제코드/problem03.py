############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_user_data_valid(user_data):

    # 여기에 코드를 작성하여 함수를 완성합니다.
      # '아이디'와 '비밀번호'가 빈 문자열인지 확인
    if user_data.get('id') == "" or user_data.get('password') == "":
        return False  # 아이디나 비밀번호가 빈 문자열이면 False 반환
    else:
        return True  # 둘 다 빈 문자열이 아니면 True 반환

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'id': '',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data1)) # False 


user_data2 = {
    'id': 'jungssafy',
    'password': '1q2w3e4r',
}
print(is_user_data_valid(user_data2)) # True
#####################################################