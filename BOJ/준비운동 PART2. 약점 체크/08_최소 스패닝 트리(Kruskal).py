# 언어 : Python
# 날짜 : 2021.07.16
# 문제 : BOJ > 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 티어 : 골드 4
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : Kruskal
# ============================================================================
from collections import defaultdict


def kruskal():
    edges.sort()  # 비용을 기준으로 정렬함
    total_weight = 0
    for edge in edges:
        w, u, v = edge
        if find(u) != find(v):  # 서로 다른 집합이면 연결
            union(u, v)
            total_weight += w

    return total_weight


def union(u, v):
    u = find(u)  # 부모 탐색
    v = find(v)
    if u == v:
        return
    if rank[u] > rank[v]:
        parent[v] = u  # 작은 것을 큰 것에 붙임
    else:
        parent[u] = v
        if rank[u] == rank[v]:
            rank[v] += 1


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


# 입력 및 실행
V, E = map(int, input().split())
edges = []
for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append([w, u - 1, v - 1])
# parent는 자기 자신으로 초기화
parent = [i for i in range(V)]
# rank는 0으로 초기화
rank = [0 for _ in range(V)]

result = kruskal()
print(result)