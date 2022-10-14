from collections import deque

INF = float("inf")


def in_range(row, col, N):
    if 0 <= row < N and 0 <= col < N:
        return True
    return False


def solution(N, K, board):
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    # [1] 가장 높은 봉우리 구하기
    max_height = -INF
    max_height_locations = []
    for r in range(N):
        for c in range(N):
            if max_height < board[r][c]:
                max_height = board[r][c]
                max_height_locations = [[r, c]]
            elif max_height == board[r][c]:
                max_height_locations.append([r, c])

    # [2] 가장 긴 등산로 찾기
    answer = -INF
    for m_row, m_col in max_height_locations:
        queue = deque()
        height = board[m_row][m_col]
        k_used = False
        length = 1
        visited = [f"{m_row} {m_col}"]
        queue.append([m_row, m_col, height, k_used, length, visited])

        # bfs
        while queue:
            row, col, prev_height, k_used, length, visited = queue.popleft()

            can_move = False
            for mr, mc in moves:
                nr, nc = row + mr, col + mc
                if in_range(nr, nc, N) and f"{nr} {nc}" not in visited:
                    # 등산로가 될 수 있는지 여부 체크
                    next_height = board[nr][nc]

                    # (1) 지형을 깎지 않아도 가능한 경우
                    if next_height < prev_height:
                        queue.append([nr, nc, next_height, k_used, length + 1, visited + [f"{nr} {nc}"]])
                    # (2) 지형을 깎아야 되는 경우(한번도 깎은 적이 없어야지 기회를 쓸 수 있음)
                    elif not k_used:
                        if next_height - K < prev_height:  # K를 다 사용했을때 prev_height보다 작으면 가능
                            queue.append([nr, nc, prev_height - 1, True, length + 1, visited + [f"{nr} {nc}"]])

            if not can_move:  # 더이상 움직일 수 없는 경우
                answer = max(answer, length)
                continue

    return answer


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    result = solution(N, K, board)
    print(f"#{test_case} {result}")
