def solution(board, moves):
    answer = 0
    stack = []
    ROW_SIZE = len(board)

    for move in moves:
        for row in range(ROW_SIZE):
            if board[row][move - 1] != 0:
                number = board[row][move - 1]
                board[row][move - 1] = 0
                if len(stack) > 0 and stack[-1] == number:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(number)
                break

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
result = solution(board, moves)
print(result)
