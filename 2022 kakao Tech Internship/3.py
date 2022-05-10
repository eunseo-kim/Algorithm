from collections import deque
import heapq

# 정확성만 ..ㅎㅎ


def solution(alp, cop, problems):
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])

    queue = []
    cost = 0
    queue.append([cost, alp, cop])
    heapq.heapify(queue)

    while queue:
        cost, a, c = heapq.heappop(queue)

        if a >= max_alp and c >= max_cop:
            return cost

        if a < max_alp:
            heapq.heappush(queue, [cost + 1, a + 1, c])

        if c < max_cop:
            heapq.heappush(queue, [cost + 1, a, c + 1])

        for p in problems:
            if a >= p[0] and c >= p[1]:
                heapq.heappush(queue, [cost + p[4], a + p[2], c + p[3]])

    return


problems = [[0, 0, 2, 1, 2], [4, 5, 3, 1, 2], [4, 11, 4, 0, 2], [10, 4, 0, 4, 2]]
alp, cop = 0, 0
result = solution(alp, cop, problems)
print(result)