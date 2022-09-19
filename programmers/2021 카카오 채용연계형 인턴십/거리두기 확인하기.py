"""
P는 응시자가 앉아있는 자리를 의미합니다.
O는 빈 테이블을 의미합니다.
X는 파티션을 의미합니다.
"""


def solution(places):
    moves = [[1, 0], [0, 1], [-1, 0], [0, -1]]

    def in_range(r, c):
        if 0 <= r < 5 and 0 <= c < 5:
            return True
        return False

    def check(i):
        for row in range(5):
            for col in range(5):
                if place[row][col] == "P":
                    # 거리두기를 체크합니다.
                    for move in moves:
                        new_r, new_c = move[0] + row, move[1] + col
                        if in_range(new_r, new_c):
                            if place[new_r][new_c] == "P":
                                return False
                            elif place[new_r][new_c] == "X":
                                continue
                            else:
                                for move in moves:
                                    next_r, next_c = move[0] + new_r, move[1] + new_c
                                    if in_range(next_r, next_c):
                                        if next_r == row and next_c == col:
                                            continue
                                        if place[next_r][next_c] == "P":
                                            return False
        return True

    answer = []
    for i, place in enumerate(places):
        if check(i):
            answer.append(1)
        else:
            answer.append(0)

    return answer


result = solution(
    [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"],
        ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
        ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"],
    ]
)
print(result)
