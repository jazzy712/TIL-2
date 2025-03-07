# 전위순회 함수
def pre_order(tree):
    # 노드가 존재한다면
    if tree:
        # 현재 노드를 결과 리스트에 추가
        result.append(str(tree))
        # 왼쪽 자식 노드 방문
        pre_order(left_p[tree])
        # 오른쪽 자식 노드 방문
        pre_order(right_c[tree])


V = int(input())
# 간선 정보 입력할 리스트 생성
arr = list(map(int, input().split()))
# 각 노드의 왼쪽 자식을 저장할 리스트
left_p = [0] * (V+1)
# 각 노드의 오른쪽 자식을 저장할 리스트
right_c = [0] * (V+1)
# 각 노드의 부모를 저장할 리스트
parent = [0] * (V+1)
# 전위순회 결과를 저장할 리스트
result = []

for n in range(V-1):
    # 부모 노드(p)와 자식 노드(c)
    p, c = arr[n*2], arr[n*2+1]
    # 자식 노드의 부모 정보 저장
    parent[c] = p
    # 왼쪽 자식이 없으면 왼쪽 자식으로 설정
    if left_p[p] == 0:
        left_p[p] = c
    # 왼쪽 자식이 있으면 오른쪽 자식으로 설정
    else:
        right_c[p] = c

# 루트 노드 초기값 설정
root = 1
for i in range(1, V+1):
    # 부모가 없으면
    if parent[i] == 0:
        # 루트값 갱신
        root = i
        break

pre_order(root)
print(' '.join(result))
