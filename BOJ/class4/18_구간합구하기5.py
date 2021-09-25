# 언어 : Python
# 날짜 : 2021.09.25
# 문제 : BOJ > 구간 합 구하기 5 (https://www.acmicpc.net/problem/11660)
# 티어 : 실버 1
# 시간초과 방지: sys.stdin.readline()을 사용하자.
# =====================================================================
import sys


def board_sum(board):
    for i in range(N):
        for j in range(1, N):
            board[i][j] += board[i][j - 1]
    return board


def solution(arr):
    x1, y1, x2, y2 = arr
    answer = 0
    for row in range(x1, x2 + 1):
        if y1 == 0:
            answer += board[row][y2]
        else:
            answer += board[row][y2] - board[row][y1 - 1]
    print(answer)


N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

board = board_sum(board)

cases = []
for _ in range(M):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    solution([x1 - 1, y1 - 1, x2 - 1, y2 - 1])
