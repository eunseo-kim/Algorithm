def find_route():
    route = [[float("inf") for _ in range(N)] for _ in range(N)]
    cases = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    check = [[False for _ in range(N)] for _ in range(N)]
    check[0][0] = True

    if board[0][0] == 1:
        route[0][0] = 1

    queue = [[0, 0]]
    while queue:
        i, j = queue.pop(0)

        if i == N - 1 and j == N - 1:
            break

        if board[i][j] == 1:
            for case in cases:
                ni = i + case[0]
                nj = j + case[1]

                if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == 1:
                    route[ni][nj] = min(route[ni][nj], route[i][j] + 1)
                    if not check[ni][nj]:
                        check[ni][nj] = True
                        queue.append([ni, nj])

    return route[N - 1][N - 1]


def solution():
    if dist <= 3:
        return dist - 1
    else:
        return (dist - 3) * 3 + 2


# 입력 및 출력
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
dist = find_route()

if dist == float("inf"):
    print(-1)
else:
    print(solution())