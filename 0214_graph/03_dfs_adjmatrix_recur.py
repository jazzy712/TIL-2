import sys
from pprint import pprint

sys.stdin = open('input.txt')

V, E = map(int, input().split())
data = list(map(int, input().split()))

# 인접행렬 생성 (V+1 크기)
adj_matrix = [[0] * (V + 1) for _ in range(V + 1)]

# 간선 정보를 인접행렬에 저장
for i in range(E):
    n1, n2 = data[i * 2], data[i * 2 + 1]
    adj_matrix[n1][n2] = 1
    adj_matrix[n2][n1] = 1

visited = [0] * (V + 1)  # 방문 여부 배열


def DFS_recursive(start):
    '''
    재귀 함수를 이용한 DFS (깊이 우선 탐색)

    - start: 현재 방문할 노드
    - visited[start] = 1로 방문 처리 후,
      인접 노드들을 재귀적으로 방문
    '''
    pass


# DFS 실행
DFS_recursive(1)


"""
동작 과정 예시

1. DFS_recursive(1) 호출
2. 1번 노드 방문 표시 및 출력
3. 1번 노드의 인접 노드 중 방문하지 않은 2번 노드 발견
4. DFS_recursive(2) 호출
5. 2번 노드 방문 표시 및 출력
6. 2번 노드의 인접 노드 중 방문하지 않은 4번 노드 발견
7. DFS_recursive(4) 호출
8. ...
9. 마지막 노드에서 더 이상 방문할 인접 노드가 없음
10. 이전 호출로 돌아가며 남은 인접 노드 확인
11. 모든 노드 방문 완료 시 전체 DFS 종료
==> 명시적인 종료 조건 없이도 그래프의 모든 연결된 노드를 방문한 후 DFS가 자연스럽게 종료됨
"""


"""
DFS_recursive 함수의 종료 조건
1. 암묵적 종료 조건
  - 현재 노드에서 더 이상 방문할 수 있는 인접 노드가 없을 때 함수가 종료
  - for 루프가 모든 노드를 검사했지만 조건을 만족하는 노드를 찾지 못했을 때 발생
2. 방문 여부 확인
  - if adj_matrix[start][next_node] == 1 and visited[next_node] == 0: 조건에서, 
  모든 인접 노드가 이미 방문되었다면 재귀 호출이 더 이상 일어나지 않음
"""
