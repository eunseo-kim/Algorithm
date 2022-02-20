# 언어 : Python
# 날짜 : 2022.2.20
# 문제 : BOJ > 달팽이 (https://www.acmicpc.net/problem/1913)
# 티어 : 실버 4
# =========================================================================

moves = [[-1, 0], [0, 1], [1, 0], [0, -1]]  # 시계방향


def solution():
    board = [[0 for _ in range(N)] for _ in range(N)]
    row, col = N // 2, N // 2
    board[row][col] = 1
    num = 2  # 각 칸에 입력하는 자연수
    cnt = 0  # cnt = 2 마다 add_num += 1
    moves_idx = 0  # moves의 인덱스
    add_num = 1  # 같은 방향으로 입력하는 연속 수 개수
    result_r, result_c = N // 2 + 1, N // 2 + 1

    while num <= N * N:
        if cnt == 2:
            cnt = 0
            add_num += 1

        move_r, move_c = moves[moves_idx]

        for _ in range(add_num):
            row, col = row + move_r, col + move_c
            board[row][col] = num
            if num == M:
                result_r, result_c = row + 1, col + 1
            num += 1
            if num > N * N:
                break

        moves_idx = (moves_idx + 1) % 4
        cnt += 1

    return board, result_r, result_c


N = int(input())
M = int(input())
answer, row, col = solution()
for a in answer:
    print(" ".join(map(str, a)))
print(row, col)