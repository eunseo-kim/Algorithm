# 언어 : Python
# 날짜 : 2022.3.7
# 문제 : BOJ > 특정 거리의 도시 찾기 (https://www.acmicpc.net/problem/18352)
# 티어 : 실버 2
# =========================================================================

from collections import defaultdict
from collections import deque


def solution():
    dist = [-1 for _ in range(N + 1)]
    answer = []
    queue = deque()
    queue.append([start, 0])
    while queue:
        curr, distance = queue.popleft()

        if dist[curr] == -1:
            if distance == key:
                answer.append(curr)
            dist[curr] = distance
            for edge in edges[curr]:
                if dist[edge] == -1:
                    queue.append([edge, distance + 1])

    return answer


N, M, key, start = map(int, input().split())
edges = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    edges[a].append(b)
result = solution()
result.sort()

if result == []:
    print(-1)
else:
    for re in result:
        print(re)