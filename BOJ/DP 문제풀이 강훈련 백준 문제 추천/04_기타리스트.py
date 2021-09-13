# 언어 : Python
# 날짜 : 2021.08.12
# 문제 : BOJ > 기타리스트 (https://www.acmicpc.net/problem/1495)
# 티어 : 실버 1
# ======================================================================
# 소요 시간 :
# 제출 시도 :
# ======================================================================


def solution():
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    dp[0][S] = 1

    for idx, v in enumerate(V):
        for n in range(M + 1):
            if dp[idx - 1][n] == 1:
                if n + v <= M:
                    dp[idx][n + v] = 1
                if n - v >= 0:
                    dp[idx][n - v] = 1

    answer = -1
    for i in range(M, -1, -1):
        if dp[N][i] == 1:
            answer = i
            break
    print(answer)


N, S, M = map(int, input().split())
V = [0] + list(map(int, input().split()))
solution()