# 언어 : Python
# 날짜 : 2021.08.17
# 문제 : BOJ > BOJ거리 (https://www.acmicpc.net/problem/12026)
# 티어 : 실버 1
# ======================================================================

def solution():
    dp = [float("inf") for _ in range(N)]
    blocks = ["B", "O", "J"]
    dp[0] = 0

    for i, r in enumerate(road):
        for j in range(1, N):
            if i + j < N:
                if road[i + j] == blocks[(blocks.index(r) + 1) % 3]:
                    dp[i + j] = min(dp[i] + pow(j, 2), dp[i + j])

    return dp[-1] if dp[-1] != float("inf") else -1


N = int(input())
road = list(input())
print(solution())
