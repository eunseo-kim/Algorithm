# 언어 : Python
# 날짜 : 2022.2.4
# 문제 : BOJ > 트리의 부모 찾기 (https://www.acmicpc.net/problem/11725)
# 티어 : 실버 2
# 시간 : 7분
# 시간복잡도 / 2 ≤ N ≤ 100,000 / 문제에서 E는 2(N-1)개
# O(N + E)
# ============================================================================

from collections import defaultdict
from collections import deque


def solution():
    parent = [0 for _ in range(N + 1)]
    visited = [False for _ in range(N + 1)]
    queue = deque([1])

    while queue:
        node = queue.popleft()
        if not visited[node]:
            visited[node] = True
            neighbors = graph[node]
            for neighbor in neighbors:
                if not visited[neighbor]:
                    parent[neighbor] = node
                    queue.append(neighbor)

    return parent[2:]


N = int(input())
graph = defaultdict(list)
for _ in range(N - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = solution()
print("\n".join(map(str, answer)))