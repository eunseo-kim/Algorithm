# 언어 : Python
# 날짜 : 2022.3.10
# 문제 : BOJ > 계단 오르기 (https://www.acmicpc.net/problem/2579)
# 티어 : 실버 3
# =================================================================


def solution():
    dp = [-float("inf") for _ in range(N + 1)]
    dp[0] = 0
    dp[1] = stairs[1]
    dp[2] = stairs[1] + stairs[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i - 3] + stairs[i - 1] + stairs[i], dp[i - 2] + stairs[i])

    return dp[-1]


N = int(input())
stairs = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    stairs[i] = int(input())

if N == 1:
    print(stairs[1])
elif N <= 2:
    print(stairs[1] + stairs[2])
else:
    print(solution())