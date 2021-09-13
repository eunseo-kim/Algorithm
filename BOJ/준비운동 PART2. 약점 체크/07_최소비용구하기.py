# 언어 : Python
# 날짜 : 2021.07.15
# 문제 : BOJ > 최소비용 구하기 (https://www.acmicpc.net/problem/1916)
# 티어 : 골드 5
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : 다익스트라
# - 시작 값에서 각 노드로 가는 최소 거리를 구한다.
# ============================================================================
from collections import defaultdict
import heapq


def solution():
    distance = [float("inf") for _ in range(N)]
    distance[start] = 0
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))  # 시작 값을 heapq에 넣어 해당 start에서 각 노드로의 최소 거리를 구함
    visited = []

    while priority_queue:
        weight, cur_node = heapq.heappop(priority_queue)
        if cur_node not in visited:  # heapq에 넣을 때는 visited에 없어서 넣었지만 또 그새 visited 됐을 수도 있어서 한번 더 검사
            distance[cur_node] = weight
            visited.append(cur_node)
            for next_node, w in graph[cur_node]:
                if next_node not in visited:
                    heapq.heappush(priority_queue, (weight + w, next_node))
    return distance[end]


# 입력 및 초기화
N = int(input())
M = int(input())
graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])  # graph[from] = [to, weight]
start, end = map(int, input().split())
start, end = start - 1, end - 1
answer = solution()
print(answer)