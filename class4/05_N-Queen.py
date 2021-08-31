# 언어 : Python
# 날짜 : 2021.08.31
# 문제 : BOJ > N-Queen (https://www.acmicpc.net/problem/9663)
# 티어 : 골드 5
# 분류 :
# 풀이 :
# ===========================================================================


def dfs(row_num):
    global board
    global answer

    if row_num == N:
        answer += 1
        return

    for col_num in range(N):
        if col_num not in board:
            for r in range(row_num):
                if abs(row_num - r) == abs(col_num - board[r]):
                    break
                board[row_num] = col_num
                dfs(row_num + 1)
                board[row_num] = -1


N = int(input())
answer = 0
board = [-1 for _ in range(N)]
dfs(0)
print(answer)