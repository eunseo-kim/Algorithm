# 언어 : Python
# 날짜 : 2022.1.17
# 문제 : BOJ > 1로 만들기 (https://www.acmicpc.net/problem/1463)
# 티어 : 실버 3
# =========================================================================


def solution():
    for i in range(1, N + 1):
        if i * 3 <= N:
            dp[i * 3] = min(dp[i * 3], dp[i] + 1)
        if i * 2 <= N:
            dp[i * 2] = min(dp[i * 2], dp[i] + 1)
        if i + 1 <= N:
            dp[i + 1] = min(dp[i + 1], dp[i] + 1)

    return dp[N]


N = int(input())
dp = [float("inf") for _ in range(N + 1)]
dp[1] = 0
result = solution()
print(result)