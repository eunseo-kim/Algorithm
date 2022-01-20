# 언어 : Python
# 날짜 : 2022.1.20
# 문제 : BOJ > 가장 먼 노드 (https://programmers.co.kr/learn/courses/30/lessons/49189)
# 레벨 : level 3
# =====================================================================================

from collections import deque, defaultdict, Counter


def solution(n, edge):
    distance = [float("inf") for _ in range(n + 1)]
    distance[0] = -1
    visited = [False for _ in range(n + 1)]
    queue = deque()
    queue.append([0, 1])

    dict = defaultdict(list)
    for e1, e2 in edge:
        dict[e1].append(e2)
        dict[e2].append(e1)

    while queue:
        w, node = queue.popleft()

        if not visited[node]:
            visited[node] = True
            distance[node] = min(distance[node], w)

            for neighbor in dict[node]:
                if not visited[neighbor]:
                    queue.append([w + 1, neighbor])

    counter = Counter(distance)
    return counter[max(distance)]


n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
result = solution(n, edge)
print(result)