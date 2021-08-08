# 언어 : Python
# 날짜 : 2021.08.08
# 문제 : BOJ > 점프 (https://www.acmicpc.net/problem/1890)
# 티어 : 실버 2
# ======================================================================
# 소요 시간 : 23분
# 제출 시도 : 1 try
# ======================================================================
def solution():
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][0] = 1

    for i in range(n):
        for j in range(n):
            if i < n - 1 or j < n - 1:
                move = board[i][j]
                if i + move < n:
                    dp[i + move][j] += dp[i][j]
                if j + move < n:
                    dp[i][j + move] += dp[i][j]

    print(dp[n - 1][n - 1])


n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
solution()