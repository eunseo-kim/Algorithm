"""
마법사 상어와 블리자드(https://www.acmicpc.net/problem/21611)
"""


def all_in_range(N, left, right, top, bottom):
    if 0 <= left < N and 0 <= right < N and 0 <= top < N and 0 <= bottom < N:
        return True
    return False


d_type = {
    1: [-1, 0],
    2: [1, 0],
    3: [0, -1],
    4: [0, 1],
}

exploded_count = {
    1: 0,
    2: 0,
    3: 0,
}


def solution(N, d, s, board):
    global exploded_count

    shark = (N + 1) // 2 - 1

    # [1] 마법으로 구슬 파괴하기
    row, col = shark, shark
    mr, mc = d_type[d]
    for _ in range(s):
        row += mr
        col += mc
        if 0 <= row < N and 0 <= col < N:
            board[row][col] = 0

    # [2] 2차원 달팽이 배열을 순서대로 1차원 배열로 변환하기
    left, right = shark - 1, shark + 1
    top, bottom = shark - 1, shark + 1
    row, col = shark, shark - 1
    board_arr = []  # 시작점 넣어놓기
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하 우 상 좌
    while all_in_range(N, left, right, top, bottom):
        board_arr.append(board[row][col])
        for mr, mc in moves:
            row += mr
            col += mc

            while left <= row <= right and top <= col <= bottom:
                board_arr.append(board[row][col])
                row += mr
                col += mc

            row -= mr
            col -= mc

        col -= 1

        # left, right, top, bottom 갱신
        left -= 1
        right += 1
        top -= 1
        bottom += 1

    # [3] 4개 연속하는 구슬은 폭발시키기 & 중간에 비어있는 구간은 앞으로 밀어넣기
    is_first = True
    exlploded = False
    while True:
        if not is_first and not exlploded:
            break

        is_first = False
        exlploded = False

        move_cnt = 1
        continous_count = 1
        prev_number = board_arr[0]
        for i in range(1, len(board_arr)):
            if board_arr[i] == 0:
                move_cnt += 1
                continue

            if prev_number == 0:
                continous_count = 1
                move_cnt = 1
                prev_number = board_arr[i]
                continue

            if board_arr[i] == prev_number:
                continous_count += 1
                move_cnt += 1
                continue

            if continous_count >= 4:
                exlploded = True
                start = i - move_cnt
                exploded_count[board_arr[start]] += continous_count
                for j in range(start, i):
                    board_arr[j] = 0

            prev_number = board_arr[i]
            continous_count = 1
            move_cnt = 1

        if continous_count >= 4:
            exlploded = True
            start = i - move_cnt + 1
            exploded_count[board_arr[start]] += continous_count
            for j in range(start, i):
                board_arr[j] = 0

    # [5] 새로운 배열에 담기
    new_board = []
    for num in board_arr:
        if num != 0:
            new_board.append(num)

    # [6] 구슬 복사하기
    next_board = []
    continous_count = 1
    for i in range(1, len(new_board)):
        if new_board[i] == new_board[i - 1]:
            continous_count += 1
        else:
            next_board.append(continous_count)
            next_board.append(new_board[i - 1])
            continous_count = 1
    if new_board != []:
        next_board.append(continous_count)
        next_board.append(new_board[-1])

    # [6] 다시 2차원 달팽이 배열로 변환하기
    result_board = [[0 for _ in range(N)] for _ in range(N)]

    # [2] 2차원 달팽이 배열을 순서대로 1차원 배열로 변환하기
    left, right = shark - 1, shark + 1
    top, bottom = shark - 1, shark + 1
    row, col = shark, shark - 1
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]  # 하 우 상 좌
    i = 0
    n = len(next_board)
    while all_in_range(N, left, right, top, bottom) and 0 <= i < n:
        result_board[row][col] = next_board[i]
        i += 1

        for mr, mc in moves:
            row += mr
            col += mc

            while left <= row <= right and top <= col <= bottom and 0 <= i < n:
                result_board[row][col] = next_board[i]
                i += 1

                row += mr
                col += mc

            row -= mr
            col -= mc

        col -= 1

        # left, right, top, bottom 갱신
        left -= 1
        right += 1
        top -= 1
        bottom += 1

    return result_board


N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
for i in range(M):
    d, s = map(int, input().split())
    board = solution(N, d, s, board)

answer = exploded_count[1] + exploded_count[2] * 2 + exploded_count[3] * 3
print(answer)
