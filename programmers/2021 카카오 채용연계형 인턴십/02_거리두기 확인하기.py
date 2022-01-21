# 언어 : Python
# 날짜 : 2022.1.21
# 문제 : 2020 Kakao Internship > 2. 거리두기 확인하기
# 티어 : Lv.2
# =========================================================================


NUM = 5
moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def is_valid_move(r, c, move):
    if 0 <= r + move[0] < NUM and 0 <= c + move[1] < NUM:
        return True
    return False


def get_diagonals(move):
    diagonals = []
    if move[0] != 0:
        diagonals.append([move[0], 1])
        diagonals.append([move[0], -1])
    else:
        diagonals.append([1, move[1]])
        diagonals.append([-1, move[1]])

    return diagonals


def is_valid(place):
    for row in range(NUM):
        for col in range(NUM):
            if place[row][col] == "P":
                for move in moves:
                    if is_valid_move(row, col, move):
                        next_place = place[row + move[0]][col + move[1]]
                        if next_place == "X":
                            continue
                        elif next_place == "P":
                            return False
                        else:
                            # 양쪽 대각선 검사
                            d1, d2 = get_diagonals(move)
                            if is_valid_move(row, col, d1) and place[row + d1[0]][col + d1[1]] == "P":
                                return False
                            if is_valid_move(row, col, d2) and place[row + d2[0]][col + d2[1]] == "P":
                                return False

                            # [P, O, P] 인 경우 검사
                            new_move = [move[0] * 2, move[1] * 2]
                            if is_valid_move(row, col, new_move):
                                new_place = place[row + new_move[0]][col + new_move[1]]
                                if new_place == "P":
                                    return False
    return True


def solution(places):
    answer = []
    for place in places:
        answer.append(int(is_valid(place)))
    return answer


places = [
    ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
    ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
    ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
    ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
    ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
]

result = solution(places)
print(result)
