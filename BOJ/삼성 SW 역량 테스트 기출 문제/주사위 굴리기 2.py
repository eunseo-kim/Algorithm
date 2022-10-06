"""
주사위 굴리기 2(https://www.acmicpc.net/problem/23288)
- 오른쪽으로 이동 ➜ dice_col의 맨 끝 원소를 앞으로 / [1, 3]번 원소를 dice_col로 맞춰줌
- 왼쪽으로 이동 ➜ dict_col의 맨 앞 원소를 끝으로 / [1, 3]번 원소를 dice_col로 맞춰줌
- 위쪽으로 이동 ➜ dict_row의 맨 앞 원소를 끝으로 / [1, 3]번 원소를 dice_row로 맞춰줌
- 아래쪽으로 이동 ➜ dice_row의 맨 끝 원소를 앞으로 / [1, 3]번 원소를 dice_row로 맞춰줌
"""

from collections import deque


def in_range(r, c, R, C):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution(ROW, COL, K, board):
    total_score = 0

    dice_row = deque([1, 5, 6, 2])
    dice_col = deque([1, 3, 6, 4])

    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]  # 시계방향 / 동서남북
    move_type = {"01": "RIGHT", "10": "BOTTOM", "0-1": "LEFT", "-10": "TOP"}
    cur_move_idx = 0  # 시작은 동쪽

    row, col = 0, 0
    for _ in range(K):
        # [1] 현재 방향대로 주사위 이동
        mr, mc = moves[cur_move_idx]
        m_type = move_type[f"{mr}{mc}"]

        if m_type == "RIGHT":
            top = dice_col.pop()
            dice_col.appendleft(top)
            dice_row[0] = dice_col[0]
            dice_row[2] = dice_col[2]
        elif m_type == "LEFT":
            top = dice_col.popleft()
            dice_col.append(top)
            dice_row[0] = dice_col[0]
            dice_row[2] = dice_col[2]
        elif m_type == "TOP":
            top = dice_row.popleft()
            dice_row.append(top)
            dice_col[0] = dice_row[0]
            dice_col[2] = dice_row[2]
        else:
            top = dice_row.pop()
            dice_row.appendleft(top)
            dice_col[0] = dice_row[0]
            dice_col[2] = dice_row[2]

        # [2] 주사위 바닥에 있는 숫자 구하기
        A = dice_row[2]

        # [3] BFS로 점수 구하기
        nr, nc = row + mr, col + mc  # 현재 위치 [nr, nc]
        B = board[nr][nc]

        def BFS(row, col):
            C = 0
            visited = [[False for _ in range(COL)] for _ in range(ROW)]
            queue = deque()
            queue.append([row, col])
            target = board[row][col]
            while queue:
                row, col = queue.popleft()
                if visited[row][col]:
                    continue
                visited[row][col] = True
                C += 1

                for mr, mc in moves:
                    nr = row + mr
                    nc = col + mc
                    if in_range(nr, nc, ROW, COL) and not visited[nr][nc] and board[nr][nc] == target:
                        queue.append([nr, nc])
            return C

        C = BFS(nr, nc)
        score = B * C
        total_score += score

        # [3] 다음 방향 구하기(만약 이동가능하지 않다면 반대방향)
        if A < B:  # 시계 방향
            cur_move_idx -= 1
        elif A > B:  # 반시계 방향
            cur_move_idx += 1
        cur_move_idx = (cur_move_idx + 4) % 4

        # [4] 이동가능한지 탐색
        row, col = nr, nc
        mr, mc = moves[cur_move_idx]
        next_r, next_c = row + mr, col + mc
        if not in_range(next_r, next_c, ROW, COL):
            cur_move_idx += 2
            cur_move_idx = (cur_move_idx + 4) % 4

        mr, mc = moves[cur_move_idx]

    return total_score


R, C, K = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(map(int, input().split())))
result = solution(R, C, K, board)
print(result)
