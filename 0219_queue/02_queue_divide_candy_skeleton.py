total_candy = 20  # 총 마이쮸 개수
queue = []  # 사람들을 저장할 큐
queue.append((1, 1))  # 첫 번째 사람과 받을 마이쮸 개수를 큐에 추가(tuple)

last_person = None  # 마지막으로 마이쮸를 받은 사람을 저장할 변수
next_person = 2

# 마이쮸가 남아있는 동안 반복
while total_candy > 0:
    # 대기열 맨 앞 사람이 마이쮸를 수령할 예정
    person, count = queue.pop(0)

    # 남은 마이쮸가 현재 사람이 받은 마이쮸 개수보다 적거나 같은 경우
    if total_candy - count <= 0:
        last_person = person
        break

    # 현재 사람이 받은 마이쮸 개수를 총 마이쮸 개수에서 제거
    total_candy = total_candy - count

    # 직전에 마이쮸를 받은 사람이 바로 다시 줄을 섬
    queue.append((person, count + 1))

    # 이 모습을 본 다음 사람이 대기열에 이어서 줄을 섬(처음이니까 받을 마이쮸는 1개)
    queue.append((next_person, 1))
    next_person += 1

# 마지막으로 마이쮸를 받은 사람을 출력
print(f"마지막 마이쮸는 {last_person}번")
