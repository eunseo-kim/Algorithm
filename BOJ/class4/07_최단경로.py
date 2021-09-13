# 언어 : Python
# 날짜 : 2021.09.03
# 문제 : BOJ > 최단경로 (https://www.acmicpc.net/problem/1753)
# 티어 : 골드 5
# ===========================================================================
from collections import defaultdict
import heapq

INF = int(10e9)


def solution():
    dist = [INF for i in range(V + 1)]
    queue = [[0, start]]
    cnt = 0

    while queue:
        if cnt == V:
            break

        weight, node = heapq.heappop(queue)

        if dist[node] == INF:
            dist[node] = weight
            cnt += 1

            candidates = edges[node]
            for w, v in candidates:
                if dist[v] == INF:
                    heapq.heappush(queue, [weight + w, v])

    for i in range(1, V + 1):
        print(dist[i]) if dist[i] != INF else print("INF")


V, E = map(int, input().split())
start = int(input())
edges = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append([w, v])
solution()

# V, E = 4, 4
# start = 1
# edges = {1: [[7, 2], [5, 4]], 2: [[3, 3]], 3: [[7, 4]], 4: []}
