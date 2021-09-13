# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 숨바꼭질2 (https://www.acmicpc.net/problem/13549)
# 티어 : 골드 5
# 걸린 시간 : 45"
# ======================================================================

from collections import deque

MAX_LOC = 100001


def solution():
    stack = deque()
    stack.append(N)
    seconds = [-1 for _ in range(MAX_LOC)]
    seconds[N] = 0

    while stack:
        location = stack.popleft()
        second = seconds[location]

        if location == K:
            print(second)
            break

        for new_loc in [location * 2, location - 1, location + 1]:
            if new_loc >= 0 and new_loc < MAX_LOC and seconds[new_loc] == -1:
                if new_loc == location * 2:
                    stack.append(new_loc)
                    seconds[new_loc] = seconds[location]
                else:
                    stack.append(new_loc)
                    seconds[new_loc] = seconds[location] + 1


N, K = map(int, input().split())
if N == K:
    print(0)
elif N > K:
    print(N - K)
else:
    solution()
# N, K = 5, 237
# N, K = 1, 4