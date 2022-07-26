# 언어 : Python
# 날짜 : 2022.7.26
# 문제 : BOJ > 집합의 표현 (https://www.acmicpc.net/problem/1717)
# 티어 : 골드 4
# ===============================================================

import sys

input = sys.stdin.readline


def union(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    if p1 == p2:
        return

    if rank[p1] < rank[p2]:
        p1, p2 = p2, p1
    parent[p2] = p1
    if rank[p1] == rank[p2]:
        rank[p1] += 1


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def is_same_disjoint_set(n1, n2):
    p1 = find(n1)
    p2 = find(n2)

    return "YES" if p1 == p2 else "NO"


#
n, m = map(int, input().split(" "))
parent = [i for i in range(n + 1)]
rank = [0 for _ in range(n + 1)]

for _ in range(m):
    op, n1, n2 = map(int, input().split(" "))
    if op == 0:
        union(n1, n2)
    else:
        result = is_same_disjoint_set(n1, n2)
        print(result)
