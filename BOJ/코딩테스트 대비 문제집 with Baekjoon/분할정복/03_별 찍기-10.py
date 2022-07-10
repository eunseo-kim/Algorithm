# 언어 : Python
# 날짜 : 2022.7.10
# 문제 : BOJ > 별 찍기-10 (https://www.acmicpc.net/problem/18222)
# 티어 : 골드 5
# =========================================================================


def solution(r, c, k):
    if k == 1:
        return

    m = k // 3

    for row in range(r, r + k, m):
        for col in range(c, c + k, m):
            solution(row, col, m)

    for row in range(r + m, r + m + m, 1):
        for col in range(c + m, c + m + m, 1):
            board[row][col] = " "


N = int(input())
board = [["*" for _ in range(N)] for _ in range(N)]
solution(0, 0, N)
for row in board:
    print("".join(map(str, row)))