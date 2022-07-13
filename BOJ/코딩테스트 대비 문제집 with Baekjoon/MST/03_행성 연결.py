# 언어 : Python
# 날짜 : 2022.7.13
# 문제 : BOJ > 행성 연결 (https://www.acmicpc.net/problem/16398)
# 티어 : 골드 4
# =========================================================================

from collections import defaultdict
import heapq


def prim():
    total_weight = 0

    queue = [[0, 0]]
    visited = set()

    while queue:
        weight, node = heapq.heappop(queue)
        if node not in visited:
            visited.add(node)
            total_weight += weight

            for edge in edges[node]:
                if edge[1] not in visited:
                    heapq.heappush(queue, edge)

            if len(visited) == N:
                break

    return total_weight


# 입력 및 실행
N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(" "))))

edges = defaultdict(list)
for i in range(N):
    for j in range(N):
        if i != j:
            edges[i].append([graph[i][j], j])

result = prim()
print(result)