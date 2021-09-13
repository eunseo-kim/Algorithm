# 언어 : Python
# 날짜 : 2021.08.13
# 문제 : BOJ > 크리보드 (https://www.acmicpc.net/problem/11058)
# 티어 : 골드 5
# ======================================================================
# 풀이
# N = 6 까지는 A만 누르는 게 최대
# N >= 7 부터는 max(dp[i], dp[k] * (i - k - 1))로 비교/갱신
# ======================================================================


def solution():
    dp = [i for i in range(N + 1)]

    for i in range(7, N + 1):
        # 에를 들어서 i = 7이면
        # 1*5 vs 2*4 vs 3*3 vs 4*2
        for k in range(1, i - 2):
            dp[i] = max(dp[i], dp[k] * (i - k - 1))

    print(dp[N])


N = int(input())
solution()