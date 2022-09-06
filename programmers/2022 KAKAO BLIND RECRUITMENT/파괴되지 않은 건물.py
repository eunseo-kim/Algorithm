# 41"
def solution(board, skill):
    ATTACK = 1
    R, C = len(board), len(board[0])
    p_sum = [[0 for _ in range(C)] for _ in range(R)]

    for type, r1, c1, r2, c2, degree in skill:
        if type == ATTACK:
            degree = -degree

        row_gap = r2 - r1 + 1
        col_gap = c2 - c1 + 1

        # 누적합 시작점 설정
        p_sum[r1][c1] += degree

        # 누적합 끝점 설정
        if 0 <= c1 + col_gap < C:
            p_sum[r1][c1 + col_gap] += -degree

        if 0 <= r1 + row_gap < R:
            p_sum[r1 + row_gap][c1] += -degree

        if 0 <= r2 + 1 < R and 0 <= c2 + 1 < C:
            p_sum[r2 + 1][c2 + 1] += degree

    # 누적합 행 계산
    for row in range(R):
        for c in range(1, C):
            p_sum[row][c] += p_sum[row][c - 1]

    # 누적합 열 계산
    for col in range(C):
        for r in range(1, R):
            p_sum[r][col] += p_sum[r - 1][col]

    answer = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] + p_sum[r][c] >= 1:
                answer += 1

    return answer


board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
skill = [[1, 1, 1, 2, 2, 4], [1, 0, 0, 1, 1, 2], [2, 2, 0, 2, 0, 100]]
result = solution(board, skill)
print(result)
