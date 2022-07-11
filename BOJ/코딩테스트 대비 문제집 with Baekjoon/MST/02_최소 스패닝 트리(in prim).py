# 언어 : Python
# 날짜 : 2022.7.11
# 문제 : BOJ > 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 티어 : 골드 4
# =========================================================================

from collections import defaultdict
import heapq, sys

input = sys.stdin.readline


def prim():
    selected_nodes = set()
    total_weight = 0

    start_node = 1
    edge_list = [[0, start_node]]  # [weight, node]
    while edge_list:
        weight, node = heapq.heappop(edge_list)
        if node in selected_nodes:
            continue

        selected_nodes.add(node)
        total_weight += weight

        for w, n in graph[node]:
            if n not in selected_nodes:
                heapq.heappush(edge_list, [w, n])

        if len(selected_nodes) == V:
            break

    return total_weight


V, E = map(int, input().split(" "))
graph = defaultdict(list)
for _ in range(E):
    a, b, w = map(int, input().split(" "))
    graph[a].append([w, b])
    graph[b].append([w, a])
answer = prim()
print(answer)