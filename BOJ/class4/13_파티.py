# 언어 : Python
# 날짜 : 2021.09.23
# 문제 : BOJ > 파티 (https://www.acmicpc.net/problem/1238)
# 티어 : 골드 3
# 주의점
# N = 1000이므로 플로이드 와샬을 사용하는 문제가 아니다. (1000^3 = 10^9번 계산 no!)
# 다익스트라로 풀어야 되는 문제!
# ===========================================================================

import heapq
from collections import defaultdict


def dijkstra(start, graph):
    distances = [float("inf") for _ in range(N + 1)]
    queue = []
    heapq.heappush(queue, (0, start))
    distances[start] = 0

    while queue:
        dist, node = heapq.heappop(queue)

        if distances[node] < dist:
            continue

        candidates = graph[node]
        for cand in candidates:
            next_dist, next_node = cand[1], cand[0]
            cost = dist + next_dist
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(queue, (cost, next_node))

    return distances


N, M, X = map(int, input().split())
graph = defaultdict(list)
reversed_graph = defaultdict(list)
for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u].append([v, w])
    reversed_graph[v].append([u, w])

re1 = dijkstra(X, graph)
re2 = dijkstra(X, reversed_graph)

answer = 0
for i in range(1, N + 1):
    answer = max(answer, re1[i] + re2[i])
print(answer)