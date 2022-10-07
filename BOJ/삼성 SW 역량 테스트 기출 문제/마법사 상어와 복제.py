"""
마법사 상어와 복제(https://www.acmicpc.net/problem/23290)
"""

from copy import deepcopy


def in_range(r, c):
    if 0 <= r < 4 and 0 <= c < 4:
        return True
    return False


SHARK_MOVES = [[-1, 0], [0, -1], [1, 0], [0, 1]]  # 상 > 좌 > 하 > 우
all_shark_moves = []


def get_all_shark_moves(path):
    global all_shark_moves
    if len(path) == 3:
        all_shark_moves.append(path)
        return
    for shar_move in SHARK_MOVES:
        get_all_shark_moves(path + [shar_move])


get_all_shark_moves([])


def solution(S, fish_info, shark):
    move_type = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1], 5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
    fish_smell = [[0 for _ in range(4)] for _ in range(4)]
    fish_board = [[[0 for _ in range(9)] for _ in range(4)] for _ in range(4)]
    shark_board = [[False for _ in range(4)] for _ in range(4)]

    # [0] initialize
    for fr, fc, move in fish_info:
        fish_board[fr - 1][fc - 1][move] += 1
    shark_board[shark[0] - 1][shark[1] - 1] = True
    curr_shark_row, curr_shark_col = shark[0] - 1, shark[1] - 1

    for _ in range(S):  # 연습횟수 S번에 대해...
        # [0] 물고기 이동 임시 저장소 생성
        temp_fish_board = [[[0 for _ in range(9)] for _ in range(4)] for _ in range(4)]  # 이동후 물고기가 담긴 temp board

        # [1] 물고기 이동시키기
        for r in range(4):
            for c in range(4):
                for move_num in range(1, 9):  # i번 방향
                    if fish_board[r][c][move_num] > 0:  # 물고기가 존재하면 이동시키기
                        fish_cnt = fish_board[r][c][move_num]  # 현재 위치에서 같은 방향의 물고기 개수

                        # [1-1] 만약 주어진 방향 이동할 수 있으면 그대로 이동하기
                        fr, fc = r, c
                        mr, mc = move_type[move_num]
                        next_fr, next_fc = fr + mr, fc + mc

                        # 이동 가능하고 + 물고기 냄새가 없고 + 상어도 없어야 됨
                        if (
                            in_range(next_fr, next_fc)
                            and fish_smell[next_fr][next_fc] == 0
                            and not shark_board[next_fr][next_fc]
                        ):
                            temp_fish_board[next_fr][next_fc][move_num] += fish_cnt
                            continue

                        # [1-2] 불가능하다면 반시계방향으로 회전하면서 가능한 경우 찾기
                        can_move = False
                        changed_move_num = move_num
                        for i in range(1, 9):
                            changed_move_num -= 1
                            if changed_move_num == 0:
                                changed_move_num = 8

                            mr, mc = move_type[changed_move_num]
                            next_fr, next_fc = fr + mr, fc + mc

                            # 이동 가능하고 + 물고기 냄새가 없고 + 상어도 없어야 됨
                            if (
                                in_range(next_fr, next_fc)
                                and fish_smell[next_fr][next_fc] == 0
                                and not shark_board[next_fr][next_fc]
                            ):
                                temp_fish_board[next_fr][next_fc][changed_move_num] += fish_cnt
                                can_move = True
                                break  # 찾았다면 나오기

                        if not can_move:  # 이동할 수 없다면 현재 위치로 이동하기
                            temp_fish_board[fr][fc][move_num] += fish_cnt

        # [2] 상어 이동하기
        # [2-1] 상하좌우 중 물고기가 많은 곳
        shark_board[curr_shark_row][curr_shark_col] = False

        max_fish = -float("inf")
        fish_found = False
        MAX_CASE = []

        for shark_moves in all_shark_moves:
            curr_sr, curr_sc = curr_shark_row, curr_shark_col
            all_in_range = True
            temp = deepcopy(temp_fish_board)
            total_fish_count = 0

            for sr, sc in shark_moves:
                curr_sr += sr
                curr_sc += sc
                if not in_range(curr_sr, curr_sc):
                    all_in_range = False
                    break

                for move in range(1, 9):
                    curr_fish_count = temp[curr_sr][curr_sc][move]
                    if curr_fish_count > 0:
                        fish_found = True
                        total_fish_count += curr_fish_count
                        temp[curr_sr][curr_sc][move] = 0

            if not all_in_range:  # 하나라도 범위 내에 없으면 해당 케이스 버리기
                continue

            if fish_found:
                if total_fish_count > max_fish:
                    max_fish = total_fish_count
                    MAX_CASE = shark_moves
            else:
                if max_fish == -float("inf"):  # 만약에 물고기 한 마리도 못 먹은 경우
                    max_fish = 0
                    MAX_CASE = shark_moves

        # 상어 이동하기
        for s_r, s_c in MAX_CASE:
            curr_shark_row += s_r
            curr_shark_col += s_c
            for move in range(1, 9):
                if temp_fish_board[curr_shark_row][curr_shark_col][move] > 0:
                    fish_smell[curr_shark_row][curr_shark_col] = 3
                    temp_fish_board[curr_shark_row][curr_shark_col][move] = 0

        # 상어 이동 완료
        shark_board[curr_shark_row][curr_shark_col] = True

        # [3] 물고기 냄새가 있다면 1씩 사라짐
        for r in range(4):
            for c in range(4):
                if fish_smell[r][c] > 0:
                    fish_smell[r][c] -= 1

        # [4] 물고기 복제
        for r in range(4):
            for c in range(4):
                for move in range(1, 9):
                    if temp_fish_board[r][c][move] > 0:
                        curr_fish_list = temp_fish_board[r][c][move]
                        fish_board[r][c][move] += curr_fish_list

    answer = 0
    for r in range(4):
        for c in range(4):
            for move in range(1, 9):
                answer += fish_board[r][c][move]
    return answer


M, S = map(int, input().split())
fish_info = []
for _ in range(M):
    fish_info.append(list(map(int, input().split())))
shark = list(map(int, input().split()))

result = solution(S, fish_info, shark)
print(result)
