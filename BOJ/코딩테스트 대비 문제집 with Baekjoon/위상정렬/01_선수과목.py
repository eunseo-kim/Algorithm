# 언어 : Python
# 날짜 : 2022.7.20
# 문제 : BOJ > 선수 과목 (https://www.acmicpc.net/problem/14567)
# 티어 : 골드 5
# =========================================================================

from collections import deque

import sys

input = sys.stdin.readline


def solution():
    queue = deque()

    for node in range(1, N + 1):
        if entry_counts[node] == 0:
            queue.append(node)

    answer = [1 for _ in range(N + 1)]

    while queue:
        node = queue.popleft()

        for child in subjects[node]:
            answer[child] = max(answer[child], answer[node] + 1)
            entry_counts[child] -= 1
            if entry_counts[child] == 0:
                queue.append(child)

    return answer


#
N, M = map(int, input().split(" "))
entry_counts = [0 for _ in range(N + 1)]

subjects = {}
for i in range(1, N + 1):
    subjects[i] = []

for _ in range(M):
    A, B = map(int, input().split(" "))
    subjects[A].append(B)
    entry_counts[B] += 1

result = solution()
for i in range(1, N + 1):
    print(result[i], end=" ")
