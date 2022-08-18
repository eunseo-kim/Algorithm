# 언어 : Python
# 날짜 : 2022.8.18
# 문제 : BOJ > 입국 심사 (https://www.acmicpc.net/problem/3079)
# 티어 : 골드 5
# ===============================================================


import sys

input = sys.stdin.readline


def binary_search(start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        total_count = 0

        for time in judge_time:
            total_count += mid // time

        if total_count >= M:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    return result


#
N, M = map(int, input().split(" "))
judge_time = []
for _ in range(N):
    judge_time.append(int(input()))
start = 1
end = max(judge_time) * M
result = binary_search(start, end)
print(result)