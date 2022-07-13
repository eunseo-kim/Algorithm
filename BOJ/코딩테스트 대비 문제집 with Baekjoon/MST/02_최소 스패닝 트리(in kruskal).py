# 언어 : Python
# 날짜 : 2022.7.11
# 문제 : BOJ > 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 티어 : 골드 4
# =========================================================================


def find(v):
    if parent[v] != v:
        parent[v] = find(parent[v])
    return parent[v]


def union_by_rank(v1, v2):
    p1 = find(v1)
    p2 = find(v2)

    # 같은 집합(트리)에 포함되어 있는 경우입니다.
    if p1 == p2:
        return

    # rank가 큰 트리에 작은 트리를 붙입니다.
    if rank[p1] > rank[p2]:
        parent[p2] = p1
    elif rank[p1] < rank[p2]:
        parent[p1] = p2
    else:  # 만약 rank가 같다면 임의로 p1 트리에 p2 트리를 붙입니다.
        parent[p2] = p1
        rank[p1] += 1


def kruskal():
    total_weight = 0

    # [1] 간선들을 가중치가 작은 순서대로 오름차순 정렬합니다.
    edges.sort()

    # [2] 간선들을 하나씩 추출하여 연결합니다.
    for weight, v1, v2 in edges:
        if find(v1) != find(v2):
            union_by_rank(v1, v2)
            total_weight += weight

    return total_weight


V, E = map(int, input().split(" "))

parent = [i for i in range(V + 1)]
rank = [0 for _ in range(V + 1)]
connected = set()

edges = []
for _ in range(E):
    v1, v2, w = map(int, input().split(" "))
    edges.append([w, v1, v2])

answer = kruskal()
print(answer)