# 언어 : Python
# 날짜 : 2022.1.19
# 문제 : BOJ > 카드 구매하기 2 (https://www.acmicpc.net/problem/16194)
# 티어 : 실버 1
# ====================================================================


def solution():
    for i in range(1, N + 1):
        dp[i] = cards[i]

        mid = i // 2
        for j in range(1, mid + 1):
            dp[i] = min(dp[i], dp[j] + dp[i - j])

    return dp[N]


N = int(input())
cards = [0] + list(map(int, input().split()))
dp = [float("inf") for _ in range(N + 1)]
result = solution()
print(result)