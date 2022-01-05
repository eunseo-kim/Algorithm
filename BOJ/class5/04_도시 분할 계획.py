# 언어 : Python
# 날짜 : 2022.1.5
# 문제 : BOJ > 도시 분할 계획 (https://www.acmicpc.net/problem/1647)
# 티어 : 골드 4
# 방법 : MST - 프림 알고리즘
# 유지비(가중치)의 합을 최소로 하려면?
# → 최소 신장 트리를 구하고 가중치가 가장 큰 edge를 없앤다.
# [주의] → 가중치가 가장 큰 edge가 꼭 마지막 탐색 노드의 edge이지는 않음
# =======================================================================

import sys, heapq

input = sys.stdin.readline


def prim():
    start = 1
    total_weight, max_weight = 0, 0
    queue = [[0, start]]
    cnt = N

    while cnt > 0:
        weight, node = heapq.heappop(queue)
        if not visited[node]:
            visited[node] = True
            cnt -= 1
            total_weight += weight
            max_weight = max(max_weight, weight)
            for next in edges[node]:
                if not visited[next[1]]:
                    heapq.heappush(queue, next)

    print(total_weight - max_weight)


N, M = map(int, input().split())
edges = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, w = map(int, input().split())
    edges[a].append((w, b))
    edges[b].append((w, a))

visited = [False] * (N + 1)

prim()