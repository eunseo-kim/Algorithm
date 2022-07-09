# 언어 : Python
# 날짜 : 2022.7.9
# 문제 : BOJ > 색종이 만들기 (https://www.acmicpc.net/problem/2630)
# 티어 : 실버 2
# =========================================================================

BLUE_COLOR = 1


def divide_and_conquer(n, row, col):
    global blue_color, white_color

    block_color = board[row][col]
    for r in range(row, row + n):
        for c in range(col, col + n):
            if board[r][c] != block_color:
                # 4등분 후 검사
                divide_and_conquer(n // 2, row, col)
                divide_and_conquer(n // 2, row + n // 2, col)
                divide_and_conquer(n // 2, row, col + n // 2)
                divide_and_conquer(n // 2, row + n // 2, col + n // 2)
                return

    if block_color == BLUE_COLOR:
        blue_color += 1
    else:
        white_color += 1
    return


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split(" "))))

blue_color, white_color = 0, 0
divide_and_conquer(N, 0, 0)
print(white_color)
print(blue_color)