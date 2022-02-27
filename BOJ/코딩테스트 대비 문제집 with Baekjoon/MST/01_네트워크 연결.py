# 언어 : Python
# 날짜 : 2022.2.25
# 문제 : BOJ > 네트워크 연결 (https://www.acmicpc.net/problem/1922)
# 티어 : 골드 4
# =========================================================================

from collections import defaultdict
import heapq


def solution():
    visited = [False for _ in range(N + 1)]
    queue = [[0, 1]]  # weight, node
    result = 0
    while queue:
        weight, node = heapq.heappop(queue)
        if not visited[node]:
            visited[node] = True
            result += weight

            for edge in edges[node]:
                if not visited[edge[1]]:
                    heapq.heappush(queue, edge)

    print(result)


N = int(input())
M = int(input())
edges = defaultdict(list)
for _ in range(M):
    a, b, w = map(int, input().split())
    edges[a].append([w, b])
    edges[b].append([w, a])
solution()