# 언어 : Python
# 날짜 : 2022.7.28
# 문제 : BOJ > 도시 건설 (https://www.acmicpc.net/problem/21924)
# 티어 : 골드 4
# =========================================================================

import sys

input = sys.stdin.readline


def findParent(node):
    if parent[node] != node:
        parent[node] = findParent(parent[node])
    return parent[node]


def union(n1, n2):
    p1 = findParent(n1)
    p2 = findParent(n2)

    if p1 == p2:
        return False  # Cycle 발생! → cannot union nodes

    if rank[p1] < rank[p2]:
        p1, p2 = p2, p1

    parent[p2] = p1

    if rank[p1] == rank[p2]:
        rank[p1] += 1

    return True


def kruskal(weight):
    edges.sort()

    edge_cnt = 0
    for w, a, b in edges:
        if union(a, b):
            edge_cnt += 1
            weight -= w

    return weight if edge_cnt == N - 1 else -1


# 입력 및 실행
N, M = map(int, input().split(" "))
edges = []
total_weight = 0
for _ in range(M):
    a, b, w = map(int, input().split(" "))
    edges.append([w, a, b])
    total_weight += w

parent = [i for i in range(N + 1)]
rank = [0 for _ in range(N + 1)]


result = kruskal(total_weight)
print(result)
