# 언어 : Python
# 날짜 : 2022.2.14
# 문제 : BOJ > DFS와 BFS (https://www.acmicpc.net/problem/1260)
# 티어 : 실버 2
# =========================================================================

from collections import defaultdict


def dfs(node):
    if not edges[node]:
        return node

    candidates = edges[node]
    for c in sorted(candidates):
        if c not in visited:
            visited.append(c)
            dfs(c)


def bfs():
    visited = []
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            candidates = edges[node]
            for c in sorted(candidates):
                if c not in visited:
                    queue.append(c)

    return visited


N, M, start = map(int, input().split())
edges = defaultdict(list)
visited = [start]
for _ in range(M):
    e1, e2 = map(int, input().split())
    edges[e1].append(e2)
    edges[e2].append(e1)

dfs(start)
dfs_result = visited
bfs_result = bfs()

print(" ".join(str(e) for e in dfs_result))
print(" ".join(str(e) for e in bfs_result))
