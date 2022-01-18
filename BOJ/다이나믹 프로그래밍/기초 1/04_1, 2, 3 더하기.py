# 언어 : Python
# 날짜 : 2022.1.18
# 문제 : BOJ > 1, 2, 3 더하기 (https://www.acmicpc.net/problem/9095)
# 티어 : 실버
# =================================================================


def solution(dp, n):
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp[0] = 1
    dp[1] = 1
    dp[2] = 2

    for i in range(3, N + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[N]


for _ in range(int(input())):
    N = int(input())
    dp = [0 for _ in range(N + 1)]
    result = solution(dp, N)
    print(result)