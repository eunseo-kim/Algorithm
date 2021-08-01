# ======================================================================
# 언어 : Python
# 날짜 : 2021.07.31 - 08.01
# 문제 : BOJ > 파이프 옮기기 (https://www.acmicpc.net/problem/17070)
# 티어 : 골드 5
# ======================================================================
# 풀이 방법 : dp
# 0 → ─, 1 → /, 2 → |
# 더 자세한 풀이는 블로그 => https://velog.io/@eunseokim/BOJ-17070%EB%B2%88-%ED%8C%8C%EC%9D%B4%ED%94%84-%EC%98%AE%EA%B8%B0%EA%B8%B0-1-dp-%ED%92%80%EC%9D%B4-python
# ======================================================================


def solution():
    # 0 → ─, 1 → /, 2 → |
    dp[0][0][1] = 1
    for i in range(2, N):
        if board[0][i] == 0:
            dp[0][0][i] = dp[0][0][i - 1]

    for r in range(1, N):
        for c in range(1, N):
            if board[r][c] == 0 and board[r][c - 1] == 0 and board[r - 1][c] == 0:
                dp[1][r][c] = dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]

            if board[r][c] == 0:
                dp[0][r][c] = dp[0][r][c - 1] + dp[1][r][c - 1]
                dp[2][r][c] = dp[2][r - 1][c] + dp[1][r - 1][c]

    print(sum(dp[i][N - 1][N - 1] for i in range(3)))


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
solution()
