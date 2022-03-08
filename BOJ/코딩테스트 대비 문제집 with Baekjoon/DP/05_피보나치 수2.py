# 언어 : Python
# 날짜 : 2022.3.8
# 문제 : BOJ > 피보나치 수 2 (https://www.acmicpc.net/problem/2748)
# 티어 : 브론즈 1
# =================================================================


def fibonacci():
    dp = [0 for _ in range(N + 1)]
    dp[0] = 0
    dp[1] = 1
    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    print(dp[N])


N = int(input())
fibonacci()