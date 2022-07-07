# 언어 : Python
# 날짜 : 2022.7.7
# 문제 : BOJ > 스도쿠 (https://www.acmicpc.net/problem/2580)
# 티어 : 골드 4
# =================================================================

import sys

input = sys.stdin.readline


def check_row_col(row, col, number):
    for i in range(9):
        if sudoku[row][i] == number:
            return False
        if sudoku[i][col] == number:
            return False
    return True


def check_3x3_box(row, col, number):
    for r in range(row, row + 3):
        for c in range(col, col + 3):
            if sudoku[r][c] == number:
                return False
    return True


def dfs(blank_idx):
    if blank_idx == total_blanks_count:
        for s in sudoku:
            print(*s)
        exit(0)

    row, col = blanks[blank_idx]
    for number in range(1, 10):
        r = row // 3 * 3
        c = col // 3 * 3

        if check_row_col(row, col, number) and check_3x3_box(r, c, number):
            sudoku[row][col] = number
            dfs(blank_idx + 1)
            sudoku[row][col] = 0


# 입력
sudoku = []
for _ in range(9):
    sudoku.append(list(map(int, input().split(" "))))

blanks = []
total_blanks_count = 0
for row in range(9):
    for col in range(9):
        if sudoku[row][col] == 0:
            blanks.append([row, col])
            total_blanks_count += 1

dfs(0)  # blank_idx = 0 부터 채우기 시작
