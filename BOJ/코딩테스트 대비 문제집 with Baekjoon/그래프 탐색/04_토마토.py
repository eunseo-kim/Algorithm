# 언어 : Python
# 날짜 : 2022.2.20
# 문제 : BOJ > 토마토 (https://www.acmicpc.net/problem/7576)
# 티어 : 골드 5
# =========================================================================

import sys

input = sys.stdin.readline
moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def is_finished(board):
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if board[r][c] == 0:
                return False
    return True


def solution(queue):
    visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]
    finished = False

    # 예외 처리
    if is_finished(board):
        print(0)
        return

    while True:
        if queue == []:
            break

        if is_finished(board):
            finished = True
            break

        next_tomato = []
        for curr_r, curr_c, days in queue:
            if board[curr_r][curr_c] == 1 and not visited[curr_r][curr_c]:
                visited[curr_r][curr_c] = True
                for move_r, move_c in moves:
                    next_r, next_c = curr_r + move_r, curr_c + move_c
                    if board[next_r][next_c] == 0 and not visited[next_r][next_c]:
                        board[next_r][next_c] = 1
                        next_tomato.append([next_r, next_c, days + 1])
        queue = next_tomato

    if finished:
        print(days)
    else:
        print(-1)


C, R = map(int, input().split())
board = [[-1 for _ in range(C + 2)]]
for _ in range(R):
    board.append([-1] + list(map(int, input().split())) + [-1])
board.append([-1 for _ in range(C + 2)])

tomato = []
for r in range(1, R + 1):
    for c in range(1, C + 1):
        if board[r][c] == 1:
            tomato.append([r, c, 1])

solution(tomato)
