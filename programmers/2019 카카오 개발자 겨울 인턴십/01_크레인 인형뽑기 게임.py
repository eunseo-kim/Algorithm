# 풀이 시간: 12' 40"


def solution(board, moves):
    stack = []
    answer = 0
    N = len(board)

    for col in moves:
        col -= 1
        for row in range(N):
            if board[row][col] != 0:
                item = board[row][col]
                board[row][col] = 0
                if stack and stack[-1] == item:
                    stack.pop()
                    answer += 2
                else:
                    stack.append(item)
                break

    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
result = solution(board, moves)
print(result)