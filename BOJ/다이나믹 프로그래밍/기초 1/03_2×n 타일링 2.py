# 언어 : Python
# 날짜 : 2022.1.17
# 문제 : BOJ > 2xn 타일링 2 (https://www.acmicpc.net/problem/11727)
# 티어 : 실버 3
# =================================================================


def fibonacci():
    dp[0] = 1
    dp[1] = 1

    for i in range(2, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] * 2

    return dp[N] % 10007


N = int(input())
dp = [0 for _ in range(N + 1)]
result = fibonacci()
print(result)