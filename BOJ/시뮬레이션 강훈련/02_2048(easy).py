"""
2048(https://www.acmicpc.net/problem/12100)
"""


from copy import deepcopy
import sys

input = sys.stdin.readline

all_cases = []


def get_all_cases(moves, path):  # 5번 이동 경우 구하기
    global all_cases

    if len(path) == 5:
        all_cases.append(path)
        return

    for move in moves:
        get_all_cases(moves, path + str(move))


def move(N, board):  # 왼쪽 방향으로 이동시키기
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    for row in range(N):
        curr_row = []
        for col in range(N):
            if board[row][col] != 0:
                curr_row.append(board[row][col])

        used = [False for _ in range(N)]
        new_row = []
        for col in range(len(curr_row)):
            if col == 0:
                new_row.append(curr_row[col])
            elif curr_row[col] != 0 and curr_row[col] == curr_row[col - 1] and not used[col - 1]:
                new_row.pop()
                new_row.append(curr_row[col] * 2)
                used[col] = True
            else:
                new_row.append(curr_row[col])

        for i in range(len(new_row)):
            new_board[row][i] = new_row[i]

    return new_board


def get_max_number(N, board):
    max_number = 0

    for row in range(N):
        for col in range(N):
            max_number = max(board[row][col], max_number)

    return max_number


def rotate(board):  # 시계방향으로 돌리기
    return list(map(list, zip(*board[::-1])))


def solution(N, board):
    get_all_cases([0, 1, 2, 3], "")  # 5번 이동 가능한 모든 경우

    max_number = 0
    for case in all_cases:
        curr_move_index = 0
        curr_board = deepcopy(board)
        for move_idx in case:
            rotate_count = (int(move_idx) + curr_move_index) % 4
            for _ in range(rotate_count):
                curr_board = rotate(curr_board)
            curr_board = move(N, curr_board)
            curr_move_index = rotate_count

        # rotate한 다음에 이동시키기
        curr_max_number = get_max_number(N, curr_board)
        max_number = max(max_number, curr_max_number)

    return max_number


N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
result = solution(N, board)
print(result)
