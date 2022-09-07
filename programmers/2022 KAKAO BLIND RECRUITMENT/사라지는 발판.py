# 승리하는 플레이어는 최소한의 이동으로 승리하고,
# 패배하는 플레이어는 최대한의 이동으로 패배해야 합니다.

moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def in_range(R, C, r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def is_finished(r, c, board):
    R, C = len(board), len(board[0])
    for m_row, m_col in moves:
        n_row, n_col = m_row + r, m_col + c
        if in_range(R, C, n_row, n_col) and board[n_row][n_col] == 1:
            return False
    return True


def in_same_board(ar, ac, br, bc):
    if ar == br and ac == bc:
        return True
    return False


def turn(board, my_row, my_col, other_row, other_col):
    R, C = len(board), len(board[0])

    # case1. 움직일 차례인데 캐릭터의 상하좌우 주변 4칸이 모두 발판이 없을때 → 내가 Lose
    if is_finished(my_row, my_col, board):
        return [False, 0]  # 내가 짐 (더이상 이동할 수 없음 = 0 리턴)

    # case2. 두 캐릭터가 같은 발판 위에 있을 때 → 상대방 Lose
    if in_same_board(my_row, my_col, other_row, other_col):
        return [True, 1]  # 내가 이김 (1번 이동하면 게임이 끝남 = 1 리턴)

    ###
    I_win = False
    max_turns, min_turns = 0, float("inf")
    for m_row, m_col in moves:
        n_row, n_col = my_row + m_row, my_col + m_col
        if in_range(R, C, n_row, n_col) and board[n_row][n_col] == 1:
            board[my_row][my_col] = "X"
            other_win, turns = turn(board, other_row, other_col, n_row, n_col)
            board[my_row][my_col] = 1

            if other_win:
                max_turns = max(max_turns, turns)
            else:
                I_win = True
                min_turns = min(min_turns, turns)

    turns = min_turns if I_win else max_turns
    return [I_win, turns + 1]


def solution(board, aloc, bloc):
    arow, acol = aloc
    brow, bcol = bloc
    result = turn(board, arow, acol, brow, bcol)
    return result[1]


result = solution([[1, 1, 1, 0], [1, 1, 0, 1], [1, 0, 1, 1], [0, 1, 1, 1]], [0, 0], [3, 3])
print(result)