# 언어 : Python
# 날짜 : 2021.08.21
# 문제 : BOJ > 미로 찾기 (https://www.acmicpc.net/problem/2178)
# 티어 : 실버 1
# ======================================================================


def solution():
    count = [[0 for _ in range(C)] for _ in range(R)]
    queue = [[0, 0]]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    while queue:
        x, y = queue.pop(0)

        if x == R - 1 and y == C - 1:
            break

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if count[nx][ny] == 0 and board[nx][ny] == 1:
                    count[nx][ny] = count[x][y] + 1
                    queue.append([nx, ny])

    print(count[R - 1][C - 1] + 1)


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input())))
solution()