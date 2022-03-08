# 언어 : Python
# 날짜 : 2022.3.8
# 문제 : BOJ > 설탕 배달 (https://www.acmicpc.net/problem/2839)
# 티어 : 브론즈 1
# ===============================================================


def solution():
    dp = [float("inf") for _ in range(N + 1)]
    dp[0] = 0
    for i in range(N):
        if i + 3 <= N:
            dp[i + 3] = min(dp[i + 3], dp[i] + 1)
        if i + 5 <= N:
            dp[i + 5] = min(dp[i + 5], dp[i] + 1)
    
    return dp[N]


N = int(input())
result = solution()
if result == float("inf"):
    print(-1)
else:
    print(result)