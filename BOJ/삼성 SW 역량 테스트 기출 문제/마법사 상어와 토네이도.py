"""
마법사 상어와 토네이도(https://www.acmicpc.net/problem/20057)
"""

RATIO = [
    [0, 0, 0.02, 0, 0],
    [0, 0.10, 0.07, 0.01, 0],
    [0.05, 0, 0, 0, 0],
    [0, 0.10, 0.07, 0.01, 0, 0],
    [0, 0, 0.02, 0, 0],
]


def in_range(row, col, N):
    if N <= row < N * 2 and N <= col < N * 2:
        return True
    return False


def rotate(arr):  # arr을 반시계방향으로 회전
    return list(map(list, zip(*arr)))[::-1]


def solution(N, board):
    def move(row, col, ratio):  # 현재 row, col에 대하여 모래바람 이동
        curr_amount = board[row][col]
        left_amount = curr_amount  # 남은 모래 양
        for r in range(5):
            for c in range(5):
                rate = ratio[r][c]
                nr = (row - 2) + r
                nc = (col - 2) + c
                new_amount = int(curr_amount * rate)
                board[nr][nc] += new_amount
                left_amount -= new_amount
        return left_amount

    moves = [[0, -1], [1, 0], [0, 1], [-1, 0]]  # 왼쪽 아래 오른쪽 위

    # 1 ~ N-1 순서대로 토네이도 칸 수 이동
    row, col = N + N // 2, N + N // 2
    move_idx = 0
    ratio = RATIO
    is_first = True
    for i in range(1, N):
        if not is_first:
            ratio = rotate(ratio)
            move_idx = (move_idx + 1) % 4

        is_first = False
        mr, mc = moves[move_idx]
        for j in range(i):
            row += mr
            col += mc

            # 현재 row, col로 모래 바람 이동하기
            curr_amount = board[row][col]
            if curr_amount > 0:
                if in_range(row, col, N):
                    left_amount = move(row, col, ratio)
                    alpha_row = row + mr
                    alpha_col = col + mc
                    board[alpha_row][alpha_col] += left_amount
            board[row][col] = 0

        # 방향 바꿔서 한번 더
        move_idx = (move_idx + 1) % 4
        ratio = rotate(ratio)
        mr, mc = moves[move_idx]

        for j in range(i):
            row += mr
            col += mc

            # 현재 row, col로 모래 바람 이동하기
            curr_amount = board[row][col]
            if curr_amount > 0:
                if in_range(row, col, N):
                    left_amount = move(row, col, ratio)
                    alpha_row = row + mr
                    alpha_col = col + mc
                    board[alpha_row][alpha_col] += left_amount
                board[row][col] = 0

    # ++) N-1은 한번 더
    # 방향 바꿔서 한번 더
    move_idx = (move_idx + 1) % 4
    ratio = rotate(ratio)
    mr, mc = moves[move_idx]
    for j in range(i):
        row += mr
        col += mc

        # 현재 row, col로 모래 바람 이동하기
        curr_amount = board[row][col]
        if curr_amount > 0:
            left_amount = move(row, col, ratio)
            board[row][col] = 0
            alpha_row = row + mr
            alpha_col = col + mc
            board[alpha_row][alpha_col] += left_amount

    answer = 0
    for arr in board:
        answer += sum(arr)

    for row in range(N, N * 2):
        for col in range(N, N * 2):
            answer -= board[row][col]

    return answer


N = int(input())
board = [[0 for _ in range(N * 3)] for _ in range(N * 3)]
for r in range(N, N * 2):
    arr = list(map(int, input().split()))
    for i, num in enumerate(arr):
        board[r][N + i] = num
result = solution(N, board)
print(result)
