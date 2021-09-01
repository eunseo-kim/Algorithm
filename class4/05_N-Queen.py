# 언어 : Python
# 날짜 : 2021.08.31
# 문제 : BOJ > N-Queen (https://www.acmicpc.net/problem/9663)
# 티어 : 골드 5
# 분류 :
# 풀이 :
# ===========================================================================


def is_valid(row, col):
    global board
    for r in range(row):
        if abs(row - r) == abs(col - board[r]):
            return False
    return True


def dfs(row_num):
    global board
    global answer
    if row_num >= N:
        answer += 1
        return

    for col_num in range(N):
        if col_num not in board:
            if is_valid(row_num, col_num):
                board[row_num] = col_num
                dfs(row_num + 1)
                board[row_num] = -1


N = int(input())
answer = 0

for i in range(N):
    board = [-1 for _ in range(N)]
    board[0] = i
    dfs(1)

print(answer)