# 언어 : Python
# 날짜 : 2022.7.18
# 문제 : BOJ > 네트워크 연결 (https://www.acmicpc.net/problem/1967)
# 티어 : 골드 4
# =========================================================================

import sys

from collections import defaultdict

sys.setrecursionlimit(10 ** 6)


def dfs(node, weight):
    child_weights = []
    for child, w in graph[node]:
        child_weight = dfs(child, w)
        child_weights.append(child_weight)

    max_child_weight = 0
    child_weights.sort(reverse=True)
    if len(child_weights) >= 1:
        max_child_weight = child_weights[0]
        diameter[node] += child_weights[0]
    if len(child_weights) >= 2:
        diameter[node] += child_weights[1]

    return weight + max_child_weight


n = int(input())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, input().split(" "))
    graph[u].append([v, w])

ROOT = 1
diameter = [0 for _ in range(n + 1)]
dfs(ROOT, 0)
print(max(diameter))