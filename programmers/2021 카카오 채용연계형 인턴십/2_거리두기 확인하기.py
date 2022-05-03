moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def is_available(place):
    for row in range(5):
        for col in range(5):
            if place[row][col] == "P":
                for m_row, m_col in moves:
                    n_row, n_col = row + m_row, col + m_col
                    if 0 <= n_row < 5 and 0 <= n_col < 5:
                        if 0 <= n_row < 5 and 0 <= n_col < 5:
                            if place[n_row][n_col] == "P":
                                return False

                        elif place[n_row][n_col] == "O":
                            for move in moves:
                                new_r, new_c = n_row + move[0], n_col + move[1]
                                if 0 <= new_r < 5 and 0 <= new_c < 5:
                                    if place[new_r][new_c] == "P":
                                        if new_r == row and new_c == col:
                                            continue
                                        return False

    return True


def solution(places):
    answer = []
    for place in places:
        if is_available(place):
            answer.append(1)
        else:
            answer.append(0)

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