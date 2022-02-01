# 언어 : Python
# 날짜 : 2022.2.1
# 문제 : BOJ > 다리 놓기 (https://www.acmicpc.net/problem/1010)
# 티어 : 실버 5
# 시간 : 15분
# 풀이 / DP
# 서쪽 다리 개수가 1개이면 경우의 수는 동쪽 다리(M) 개수
# 서쪽 다리 개수 == 동쪽 다리 개수 이면 경우의 수는 1
# 동쪽 다리가 m개 일때 n개의 서쪽 다리를 놓는 경우 2가지
# 1) m-1개의 동쪽 다리에 n개의 서쪽 다리 놓고 m번째 동쪽 다리는 비워두기
# 2) m-1개의 동쪽 다리에 n-1개의 서쪽 다리 놓고, m번째 동쪽 다리에 n번째 서쪽 다리를 놓기
# ex. 3개의 서쪽 다리를 5개의 동쪽 다리에 배치하는 경우(표)
# | -  1 | 2 | 3 | 4 | 5 |
# ------------------------
# | 1 | 1 / 2 / 3 / 4 / 5 |
# | 2 | 0 / 1 / 3 / 6 / 10|
# | 3 | 0 / 0 / 1 / 4 / 10|
# ==================================================================

# 풀이 1 / 수학(조합)
import math


def combination(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))


# 풀이 #2 / dp
def solution(N, M):
    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if i == 1:
                dp[i][j] = dp[i][j - 1] + 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i - 1][j - 1]

    return dp[N][M]


for _ in range(int(input())):
    N, M = map(int, input().split())
    # solution #1
    print(combination(M, N))
    # solution #2
    print(solution(N, M))
