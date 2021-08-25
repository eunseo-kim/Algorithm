# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 바이러스 (https://www.acmicpc.net/problem/2606)
# 티어 : 실버 3
# 걸린 시간 : 9"
# ======================================================================
from collections import defaultdict


def dfs(node, visited):
    global count

    if not edges[node]:
        return

    candidates = edges[node]
    for candidate in candidates:
        if candidate not in visited:
            visited += [candidate]
            dfs(candidate, visited)
            count += 1


N = int(input())
E = int(input())
edges = defaultdict(list)
for _ in range(E):
    r, v = map(int, input().split())
    edges[r].append(v)
    edges[v].append(r)

count = 0
dfs(1, [1])
print(count)