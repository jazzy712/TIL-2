############## 주의 ##############
# 입력을 받기 위한 input 함수는 절대 사용하지 않습니다.
# Python 내장함수 sum, len, min, max, sorted 또는 리스트 sort 메서드 사용 시 감점

def analyze_likes(weekly_like_list):
    
    # 여기에 코드를 작성하여 함수를 완성합니다.
    sum_likes = 0   # 좋아요 합계를 0으로 설정
    for likes in weekly_like_list:     

        sum_likes += likes       # 일주일 간의 좋아요 리스트를 돌아다니며 좋아요 수 만큼 합계 증가

    average =  float(sum_likes / 7)     # 합계를 7로 나눈 실수 형태를 새로운 변수에 할당
    # 최대값 찾기
    max_likes = weekly_like_list[0]
    for likes in weekly_like_list:
        if likes > max_likes:
            max_likes = likes

    # 최소값 찾기
    min_likes = weekly_like_list[0]
    for likes in weekly_like_list:
        if likes < min_likes:
            min_likes = likes
        
# 최대값과 최소값의 차이 계산
    difference = max_likes - min_likes

# 평균과 차이를 튜플로 반환

    return (average, difference)
    
                   
    

    
        

    
        
        
    
# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우
# 모든 책임은 삭제한 본인에게 있습니다.
############## 테스트 코드 삭제 금지 #################
analyze_likes([2, 5, 3, 8, 0, 10, 4])
# 1) 평균 = (2 + 5 + 3 + 8 + 0 + 10 + 4) / 7
#    = 32 / 7 ≈ 4.5714...
# 2) 최소=0, 최대=10, 차이=10
# 결과: (4.5714..., 10)
print(analyze_likes([2, 5, 3, 8, 0, 10, 4]))  # 예시: (4.5714..., 10)
print(analyze_likes([7, 7, 7, 7, 7, 7, 7]))   # (7.0, 0)

#####################################################

