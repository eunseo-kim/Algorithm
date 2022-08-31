# 직선 도로 하나를 만들 때는 100원이 소요되며, 코너를 하나 만들 때는 500원이 추가로 듭니다.

from collections import deque

# directions
RIGHT = [0, 1]
LEFT = [0, -1]
UP = [-1, 0]
DOWN = [1, 0]

# costs
STRAIGHT_COST = 100
CORNER_COST = 500


def solution(board):
    N = len(board)
    directions = {0: RIGHT, 1: LEFT, 2: UP, 3: DOWN}

    # initialize cost
    cost = [[[float("inf") for _ in range(4)] for _ in range(N)] for _ in range(N)]  # cost[row][col][방향]
    for i in range(4):
        cost[0][0][i] = 0

    # initialize queue
    queue = deque()
    for direction in range(4):
        row, col = directions[direction]
        if 0 <= row < N and 0 <= col < N and board[row][col] == 0:
            cost[row][col][direction] = STRAIGHT_COST
            queue.append([row, col, direction, STRAIGHT_COST])

    while queue:
        row, col, curr_dir, curr_cost = queue.popleft()
        for next_dir in range(4):
            move_r, move_c = directions[next_dir]
            new_r, new_c = row + move_r, col + move_c

            if not (0 <= new_r < N and 0 <= new_c < N):
                continue

            if board[new_r][new_c] == 1:
                continue

            if curr_dir == next_dir:
                additional_cost = STRAIGHT_COST
            else:
                additional_cost = STRAIGHT_COST + CORNER_COST

            new_cost = curr_cost + additional_cost
            if new_cost < cost[new_r][new_c][next_dir]:
                cost[new_r][new_c][next_dir] = new_cost
                queue.append([new_r, new_c, next_dir, new_cost])

    return min(cost[N - 1][N - 1])


board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
result = solution(board)
print(result)
