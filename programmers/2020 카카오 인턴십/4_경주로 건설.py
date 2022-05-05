from collections import deque


def solution(board):
    directions = {
        0: [0, -1],  # left
        1: [0, 1],  # right
        2: [-1, 0],  # up
        3: [1, 0],  # down
    }

    N = len(board)
    if N == 1:
        return 100

    queue = deque()
    score_board = [[[float("inf") for _ in range(N)] for _ in range(N)] for _ in range(4)]

    for dir in range(4):
        score_board[dir][0][0] = 0

    for dir in range(4):
        move = directions[dir]
        next_row, next_col = move[0], move[1]
        if 0 <= next_row < N and 0 <= next_col < N:
            if board[next_row][next_col] != 1:
                score_board[dir][next_row][next_col] = 100
                queue.append([next_row, next_col, dir, 100])

    while queue:
        row, col, dir, score = queue.popleft()
        for direction in range(4):
            move = directions[direction]
            next_row, next_col = row + move[0], col + move[1]
            if 0 <= next_row < N and 0 <= next_col < N:
                if board[next_row][next_col] != 1:
                    if dir == direction:
                        if score_board[direction][next_row][next_col] > score + 100:
                            score_board[direction][next_row][next_col] = score + 100
                            queue.append([next_row, next_col, direction, score + 100])
                    else:
                        if score_board[direction][next_row][next_col] > score + 600:
                            score_board[direction][next_row][next_col] = score + 600
                            queue.append([next_row, next_col, direction, score + 600])

    answer = float("inf")
    for dir in range(4):
        answer = min(answer, score_board[dir][N - 1][N - 1])

    return answer


board = [[0, 0, 1, 0], [0, 0, 0, 0], [0, 1, 0, 1], [1, 0, 0, 0]]

result = solution(board)
print(result)