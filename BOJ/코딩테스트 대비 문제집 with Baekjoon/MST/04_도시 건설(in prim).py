# 언어 : Python
# 날짜 : 2022.7.28
# 문제 : BOJ > 도시 건설 (https://www.acmicpc.net/problem/21924)
# 티어 : 골드 4
# =========================================================================


from collections import defaultdict
import heapq
import sys

input = sys.stdin.readline


def prim(weight):
    start_node = 1
    
    visited = set()
    queue = [[0, start_node]]

    while queue:
        if len(visited) == N:
            break

        w, n = heapq.heappop(queue)
        if n not in visited:
            visited.add(n)
            weight -= w

            for _w, _n in edges[n]:
                if _n not in visited:
                    heapq.heappush(queue, [_w, _n])

    return weight if len(visited) == N else -1


# 입력 및 실행
N, M = map(int, input().split(" "))
edges = defaultdict(list)
total_weight = 0
for _ in range(M):
    a, b, w = map(int, input().split(" "))
    edges[a].append([w, b])
    edges[b].append([w, a])
    total_weight += w

result = prim(total_weight)
print(result)
