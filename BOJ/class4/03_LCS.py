# 언어 : Python
# 날짜 : 2021.08.29
# 문제 : BOJ > LCS (https://www.acmicpc.net/problem/9251)
# 티어 : 골드 5
# 분류 : dp
# ===========================================================================


def solution():
    R, C = len(s1), len(s2)
    dp = [[0 for _ in range(C)] for _ in range(R)]

    for r in range(1, R):
        for c in range(1, C):
            if s1[r] == s2[c]:
                dp[r][c] = dp[r - 1][c - 1] + 1
            else:
                dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

    print(dp[R - 1][C - 1])


s1 = " " + input()
s2 = " " + input()
solution()