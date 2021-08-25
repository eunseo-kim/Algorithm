# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 숨바꼭질2 (https://www.acmicpc.net/problem/12851)
# 티어 : 골드 5
# 걸린 시간 : 1' 12"
# ======================================================================

from collections import deque
from collections import defaultdict

MAX_LOC = 100001


def solution():
    stack = deque()
    stack.append([N, 0])  # location, second
    cnt = 0
    min_sec = float("inf")
    visited = [float("inf") for _ in range(MAX_LOC)]  # 현재 위치까지 오는데 걸리는 최소 시간을 저장

    while stack:
        node = stack.popleft()
        location = node[0]
        second = node[1]

        if second > min_sec:
            break

        if location == K:
            min_sec = second
            cnt += 1

        for new_loc in [location + 1, location - 1, location * 2]:
            if new_loc >= 0 and new_loc < MAX_LOC and second + 1 <= visited[new_loc]:
                visited[new_loc] = second + 1
                stack.append([new_loc, second + 1])

    print(min_sec)
    print(cnt)


N, K = map(int, input().split())
if N == K:
    print(0, 1)
elif N > K:
    print(N - K, 1)
else:
    solution()