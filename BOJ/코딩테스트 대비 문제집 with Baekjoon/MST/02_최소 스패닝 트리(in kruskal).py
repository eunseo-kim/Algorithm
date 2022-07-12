# 언어 : Python
# 날짜 : 2022.7.11
# 문제 : BOJ > 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 티어 : 골드 4
# =========================================================================


def findParent(v):
    if parent[v] != v:
        parent[v] = findParent(parent[v])
    return parent[v]


def union(v1, v2):
    parent1 = findParent(v1)
    parent2 = findParent(v2)

    if parent1 == parent2:
        return

    # +) union-by-rank로 효율적으로 구현해봅니다.
    if rank[parent1] >= rank[parent2]:  # rank가 큰 것에 작은 것을 붙입니다.
        parent[parent2] = parent1
    else:
        parent[parent1] = parent2


def kruskal():
    total_weight = 0

    # [1] 간선들을 가중치가 작은 순서대로 오름차순 정렬합니다.
    edges.sort()

    # [2] 간선들을 하나씩 추출하여 연결합니다.
    for weight, v1, v2 in edges:
        if findParent(v1) != findParent(v2):
            union(v1, v2)
            total_weight += weight

    return total_weight


V, E = map(int, input().split(" "))

parent = [i for i in range(V + 1)]
rank = [0 for _ in range(V + 1)]

edges = []
for _ in range(E):
    v1, v2, w = map(int, input().split(" "))
    edges.append([w, v1, v2])
    edges.append([w, v2, v1])

answer = kruskal()
print(answer)