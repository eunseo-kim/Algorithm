# 언어 : Python
# 날짜 : 2022.2.16
# 문제 : BOJ > 큰 수 구성하기 (https://www.acmicpc.net/problem/18511)
# 티어 : 실버 5
# =========================================================================

import sys

sys.setrecursionlimit(10 ** 9)


def dfs(path, number, idx):
    global max_number

    if number > N:
        return

    if number <= N and number > max_number:
        max_number = number

    for i in range(K):
        dfs(path + [nums[i]], number * 10 + int(nums[i]), i)


max_number = 0
N, K = map(int, input().split())
nums = list(map(int, input().split()))

dfs([], 0, 0)

print(max_number)