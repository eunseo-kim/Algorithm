"""
구슬 탈출 2(https://www.acmicpc.net/problem/13460) / 골1
"""

from collections import deque


def in_range(r, c, R, C):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution(R, C, board):
    cases = set()

    # [1] 구슬의 위치 파악하기
    red, blue = [], []
    for r in range(R):
        for c in range(C):
            if board[r][c] == "R":
                red = [r, c]
            if board[r][c] == "B":
                blue = [r, c]

    # [2] 빨간 구슬이 구멍에 들어갈 때까지 BFS 반복
    queue = deque()
    queue.append([red[0], red[1], blue[0], blue[1], 0])
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    move_type = {"01": "right", "10": "bottom", "0-1": "left", "-10": "top"}

    min_cnt = float("inf")

    while queue:
        rr, rc, br, bc, cnt = queue.popleft()
        if f"{rr}{rc}{br}{bc}" in cases:
            continue
        cases.add(f"{rr}{rc}{br}{bc}")

        # [2-1] 단, 10번 초과 시 BFS 종료되도록
        if cnt > 10:
            continue

        for mr, mc in moves:
            r_moved = True
            b_moved = True

            new_rr = rr + mr
            new_rc = rc + mc
            red_hole = False

            if not in_range(new_rr, new_rc, R, C):
                new_rr, new_rc = rr, rc

            elif board[new_rr][new_rc] == "#":
                new_rr, new_rc = rr, rc
            else:
                # [2-2] 빨간구슬 => 이동할 수 있으면 '#'을 만나기 전까지 이동하기
                while in_range(new_rr, new_rc, R, C) and board[new_rr][new_rc] != "#":
                    if board[new_rr][new_rc] == "O":
                        red_hole = True
                        break
                    new_rr += mr
                    new_rc += mc

                if not red_hole:
                    new_rr -= mr
                    new_rc -= mc

            if new_rr == rr and new_rc == rc:
                r_moved = False

            # [2-3] 파란구슬 => 이동할 수 있으면 '#'를 만나기 전까지 이동하기
            new_br = br + mr
            new_bc = bc + mc
            blue_hole = False

            if not in_range(new_br, new_bc, R, C):
                new_br, new_bc = br, bc
            else:
                while in_range(new_br, new_bc, R, C) and board[new_br][new_bc] != "#":
                    if board[new_br][new_bc] == "O":
                        blue_hole = True
                        break
                    new_br += mr
                    new_bc += mc

                if not blue_hole:
                    new_br -= mr
                    new_bc -= mc

            if new_br == br and new_bc == bc:
                b_moved = False

            # [3] 다음으로 이동할 지 결정하기
            # [3-1] 둘다 이동 안했으면 버리기
            if not b_moved and not r_moved:
                continue

            # [3-2] 만약 파란구슬이 구멍에 들어가면 해당 경로 버리기
            if blue_hole:
                continue

            # [3-3] 빨간 구슬과 파란 구슬은 동시에 같은 칸에 있을 수 없음
            if new_rr == new_br and new_rc == new_bc:
                type = move_type[f"{mr}{mc}"]
                if type == "left":
                    if rc > bc:
                        new_rc += 1
                    else:
                        new_bc += 1
                elif type == "right":
                    if rc < bc:
                        new_rc -= 1
                    else:
                        new_bc -= 1
                elif type == "top":
                    if rr > br:
                        new_rr += 1
                    else:
                        new_br += 1
                else:
                    if rr < br:
                        new_rr -= 1
                    else:
                        new_br -= 1

                if new_rr == rr and new_rc == rc and new_br == br and new_bc == bc:  # [3-4] 이동하지 않았다면 버리기
                    continue
                else:
                    if f"{new_rr}{new_rc}{new_br}{new_bc}" in cases:  # [3-5] 이미 방문했던 케이스라면 버리기
                        continue

                    queue.append([new_rr, new_rc, new_br, new_bc, cnt + 1])  # [4] 이동 가능
                    continue

            if red_hole:
                min_cnt = min(min_cnt, cnt + 1)  # [5] 빨간구슬만 구멍에 들어간 경우 ➢ 최소 이동 횟수 갱신하기
                continue

            if f"{new_rr}{new_rc}{new_br}{new_bc}" in cases:
                continue
            queue.append([new_rr, new_rc, new_br, new_bc, cnt + 1])  # [4] 이동 가능

    if min_cnt > 10 or min_cnt == float("inf"):  # [5] (10회 이상 사용한 경우 or 구멍에 들어간 적이 없는 경우)는 return -1
        min_cnt = -1
    return min_cnt


R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))
result = solution(R, C, board)
print(result)
