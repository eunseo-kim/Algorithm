# 언어 : Python
# 날짜 : 2022.06.29
# 문제 : Programmers > 퍼즐 조각 채우기
# 티어 : Lv 3
# ==============================================================

from collections import deque

EMPTY = 0
NOT_EMPTY = 1


def solution(game_board, table):
    total_block_count = 0

    # [1] N x N game board를 순회하면서 empty_blocks를 구합니다.
    empty_blocks = get_target_blocks(game_board, EMPTY)

    # [2] M x M table을 순회하면서 puzzle_blocks 구합니다.
    puzzle_blocks = get_target_blocks(table, NOT_EMPTY)

    # [3] empty_blocks에 딱 맞는 puzzle_blocks가 있는지 구합니다. (회전 여부 고려)
    puzzle_used = [False for _ in range(len(puzzle_blocks))]

    for empty_block in empty_blocks:
        puzzle_found = False

        for idx, puzzle_block in enumerate(puzzle_blocks):
            if not puzzle_used[idx]:
                for _ in range(4):
                    puzzle_block = rotate_puzzle_blocks(puzzle_block)
                    puzzle_block = change_first_block_to_zero(puzzle_block)

                    result = compare_blocks(empty_block, puzzle_block)
                    if result != False:
                        total_block_count += result
                        puzzle_found = True
                        puzzle_used[idx] = True
                        break

            if puzzle_found:
                break

    # [4] 최종 결과를 리턴합니다.
    return total_block_count


def compare_blocks(block1, block2):
    n1 = len(block1)
    n2 = len(block2)
    block_count = 0

    if n1 != n2:
        return False

    for row in range(n1):
        for col in range(n1):
            if block1[row][col] != block2[row][col]:
                return False
            if block1[row][col] == 1:
                block_count += 1

    return block_count


def change_first_block_to_zero(block):
    N = len(block)
    changed = [[0 for _ in range(N)] for _ in range(N)]

    blocks = []
    for i in range(N):
        for j in range(N):
            if block[i][j] == 1:
                blocks.append([i, j])

    min_row = min(blocks, key=lambda x: x[0])[0]
    min_col = min(blocks, key=lambda x: x[1])[1]

    for row, col in blocks:
        row -= min_row
        col -= min_col

        changed[row][col] = 1

    return changed


# 90도로 회전하기
def rotate_puzzle_blocks(board):
    N = len(board)
    s = 0
    gap = N - 1
    n = N - 1
    while gap > 0:
        # 1차원 배열로 추출
        arr = deque()

        for i in range(s, s + gap):
            arr.append(board[s][i])

        for i in range(s, s + gap):
            arr.append(board[i][n])

        for i in range(s + gap, s, -1):
            arr.append(board[n][i])

        for i in range(s + gap, s, -1):
            arr.append(board[i][s])

        # 1차원 배열 회전 (90도)
        for _ in range(s, s + gap):
            tmp = arr.popleft()
            arr.append(tmp)

        # 1차원 => 2차원 배열로 변경
        for i in range(s, s + gap):
            board[s][i] = arr.popleft()

        for i in range(s, s + gap):
            board[i][n] = arr.popleft()

        for i in range(s + gap, s, -1):
            board[n][i] = arr.popleft()

        for i in range(s + gap, s, -1):
            board[i][s] = arr.popleft()

        gap -= 2
        n -= 1
        s += 1

    return board


def get_target_blocks(array, target):
    N = len(array)
    visited = [[False for _ in range(N)] for _ in range(N)]
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def bfs(row, col):
        queue = deque()
        queue.append([row, col])

        empty_block = []
        while queue:
            r, c = queue.popleft()
            visited[r][c] = True
            empty_block.append([r, c])

            for m_r, m_c in moves:
                n_r, n_c = r + m_r, c + m_c
                if 0 <= n_r < N and 0 <= n_c < N and not visited[n_r][n_c] and array[n_r][n_c] == target:
                    queue.append([n_r, n_c])

        return empty_block

    def change_to_standard_zero_block(empty_block):
        min_row = min(empty_block, key=lambda x: x[0])[0]
        min_col = min(empty_block, key=lambda x: x[1])[1]

        max_row_size = max(empty_block, key=lambda x: x[0])[0] - min_row + 1
        max_col_size = max(empty_block, key=lambda x: x[1])[1] - min_col + 1
        standard_N = max(max_row_size, max_col_size)

        new_square_board = [[0 for _ in range(standard_N)] for _ in range(standard_N)]

        for r, c in empty_block:
            r -= min_row
            c -= min_col
            new_square_board[r][c] = 1

        return new_square_board

    target_blocks = []
    for row in range(N):
        for col in range(N):
            if not visited[row][col] and array[row][col] == target:
                empty_block = bfs(row, col)
                new_square_board = change_to_standard_zero_block(empty_block)
                target_blocks.append(new_square_board)

    return target_blocks


game_board = [
    [1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 1, 0],
    [0, 1, 1, 1, 0, 0],
]

table = [
    [1, 0, 0, 1, 1, 0],
    [1, 0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1, 1],
    [0, 0, 1, 0, 0, 0],
    [1, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 0, 0],
]

result = solution(game_board, table)
print("RESULT", result)