def container_move(wi, ti):
    # 화물 무게와 적재용량 내림차순
    wi.sort(reverse=True)
    ti.sort(reverse=True)
    # 총 무게 초기화
    total_weight = 0
    # # 트럭 수 만큼 반복
    # for i in range(M):
    # 화물이 더 많을 수도 있고, 트럭이 더 많을 수도 있음
    # 둘 중 작은 값만큼 반복
    for i in range(min(len(wi), len(ti))):
        # 화물 무게들을 순회하면서 찾기
        for j in range(len(wi)):
            # 적재용량보다 무게가 작다면 운반
            if wi[j] <= ti[i]:
                total_weight += wi[j]
                # 운반했으면 화물 리스트에서 빼고 다음 트럭으로 넘어감
                wi.pop(j)
                break

    return total_weight


T = int(input())

for tc in range(1, T+1):
    # 컨테이너 수 N, 트럭 수 M
    N, M = map(int, input().split())
    # 화물 무게 wi, 트럭 적재용량 ti
    wi = list(map(int, input().split()))
    ti = list(map(int, input().split()))

    result = container_move(wi, ti)
    print(f'#{tc} {result}')
