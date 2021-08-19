# 언어 : Python
# 날짜 : 2021.08.19
# 문제 : BOJ > 1학년 (https://www.acmicpc.net/problem/5557)
# 티어 : 골드 5
# ======================================================================


def solution():
    dp = [[0 for _ in range(21)] for _ in range(N - 1)]
    dp[0][nums[0]] = 1

    for idx in range(1, N - 1):
        for j in range(21):
            if dp[idx - 1][j] > 0:
                # 덧셈
                if j + nums[idx] <= 20:
                    dp[idx][j + nums[idx]] += dp[idx - 1][j]

                # 뺄셈
                if j - nums[idx] >= 0:
                    dp[idx][j - nums[idx]] += dp[idx - 1][j]

    print(dp[N - 2][target])


N = int(input())
nums = list(map(int, input().split()))
target = nums[-1]
solution()