# 언어 : Python
# 날짜 : 2022.1.4
# 문제 : BOJ > LCS 2 (https://www.acmicpc.net/problem/9252)
# 티어 : 골드 5
# =====================================================================

def LCS():
    for row in range(1, len2 + 1):
        for col in range(1, len1 + 1):
            if s2[row - 1] == s1[col - 1]:
                dp[row][col] = dp[row - 1][col - 1] + [s2[row - 1]]
            else:
                if len(dp[row - 1][col]) > len(dp[row][col - 1]):
                    dp[row][col] = dp[row - 1][col]
                else:
                    dp[row][col] = dp[row][col - 1]

    return dp[len2][len1]


s1 = list(input())
s2 = list(input())
len1, len2 = len(s1), len(s2)
dp = [[[] for _ in range(len1 + 1)] for _ in range(len2 + 1)]

lcs = LCS()
print(len(lcs))
print("".join(map(str, lcs)))