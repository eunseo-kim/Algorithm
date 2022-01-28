# 언어 : Python
# 날짜 : 2022.1.28
# 문제 : BOJ > 바이러스(https://www.acmicpc.net/problem/2606)
# 티어 : 실버 3
# 시간 : 9분
# ① HOW - BFS
# ② NEW - X
# ✔시간복잡도
# 1 <= N <= 100
# O(|V|+|E|)
# ============================================================================

from collections import defaultdict


def solution():
    queue = [1]

    while queue:
        node = queue.pop(0)

        if not visited[node]:
            visited[node] = True

        for neighbor in edges[node]:
            if not visited[neighbor]:
                queue.append(neighbor)

    answer = -1
    for i in range(1, V + 1):
        if visited[i]:
            answer += 1

    return answer


V = int(input())  # N <= 100
E = int(input())
edges = defaultdict(list)
for _ in range(E):
    v, w = map(int, input().split())
    edges[v].append(w)
    edges[w].append(v)

visited = [False for _ in range(V + 1)]
print(solution())