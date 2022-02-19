# 언어 : Python
# 날짜 : 2022.2.19
# 문제 : BOJ > 지뢰 찾기 (https://www.acmicpc.net/problem/4396)
# 티어 : 실버 5
# =========================================================================

moves = [[0, 1], [1, 0], [-1, 0], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]


def solution():
    result = [["." for _ in range(N + 2)] for _ in range(N + 2)]
    is_open = False

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            if open_graph[row][col] == "x":
                if board[row][col] == "*":
                    is_open = True
                else:
                    count = 0
                    for move in moves:
                        if board[row + move[0]][col + move[1]] == "*":
                            count += 1
                    result[row][col] = count
    if is_open:
        for land_mine in land_mines:
            result[land_mine[0]][land_mine[1]] = "*"

    return result


# 입력 및 출력
N = int(input())

board = [["." for _ in range(N + 2)]]
for _ in range(N):
    board.append(["."] + list(input()) + ["."])
board.append(["." for _ in range(N + 2)])

land_mines = []
for r in range(1, N + 1):
    for c in range(1, N + 1):
        if board[r][c] == "*":
            land_mines.append([r, c])


open_graph = [["." for _ in range(N + 2)]]
for _ in range(N):
    open_graph.append(["."] + list(input()) + ["."])
open_graph.append(["." for _ in range(N + 2)])

result = solution()

for row in range(1, N + 1):
    for col in range(1, N + 1):
        print(result[row][col], end="")
    print()