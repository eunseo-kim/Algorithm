# 언어 : Python
# 날짜 : 2022.3.8
# 문제 : BOJ > Four Squares (https://www.acmicpc.net/problem/17626)
# 티어 : 실버 4
# =================================================================


def solution():
    dp = [float("inf") for _ in range(N + 1)]
    dp[0] = 0
    for i in range(N+1):
        for num in range(N+1):
            if i + num * num > N:
                break
            else:
                new_num = i + num * num
                dp[new_num] = min(dp[new_num], dp[i] + 1)

    print(dp[N])


N = int(input())
solution()