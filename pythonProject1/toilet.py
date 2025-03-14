people = [15, 30, 50, 10]
n = len(people)

# 접근법. 최소 시간인 사람부터 화장실로 들어가자.
# 오름차순 정렬
people.sort()
# 전체 대기 시간
total_time = 0
# 대기 인원 수
remain_people = n - 1

for turn in range(n):
    time = people[turn]
    total_time += time * remain_people
    remain_people -= 1
print(total_time)