def solution(n, clockwise):
    clockwise_move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    counterclockwise_move = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    graph = [[0 for _ in range(n)] for _ in range(n)]
    clockwise_corners = {0: [0, 0], 1: [0, n - 1], 2: [n - 1, n - 1], 3: [n - 1, 0]}
    counterclockwise_corners = {0: [0, 0], 1: [n - 1, 0], 2: [n - 1, n - 1], 3: [0, n - 1]}

    # get checkpoints
    checkpoints = []
    i = n - 1
    while i > 0:
        checkpoints.append(i)
        i -= 2
    if n % 2 == 1:
        checkpoints.append(1)

    # enter graph result
    if clockwise:
        for i in range(4):
            row, col = clockwise_corners[i]
            direction = i
            row -= clockwise_move[direction][0]
            col -= clockwise_move[direction][1]
            num = 1
            for j, check in enumerate(checkpoints):
                while check > 0:
                    row += clockwise_move[(direction + j) % 4][0]
                    col += clockwise_move[(direction + j) % 4][1]
                    graph[row][col] = num
                    check -= 1
                    num += 1
    else:  # counterclockwise
        for i in range(4):
            row, col = counterclockwise_corners[i]
            direction = i
            row -= counterclockwise_move[direction][0]
            col -= counterclockwise_move[direction][1]
            num = 1
            for j, check in enumerate(checkpoints):
                while check > 0:
                    row += counterclockwise_move[(direction + j) % 4][0]
                    col += counterclockwise_move[(direction + j) % 4][1]
                    graph[row][col] = num
                    check -= 1
                    num += 1

    return graph


n = 5
clockwise = False
print(solution(n, clockwise))