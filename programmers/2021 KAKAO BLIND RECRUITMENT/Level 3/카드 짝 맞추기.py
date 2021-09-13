# 언어 : Python
# 날짜 : 2021.06.27
# 문제 : Programmers > Lv3 > 카드 짝 맞추기
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# =================================================================
# 소요 시간 :
# 제출 시도 :
# =================================================================


def get_locations(board):
    locations = []
    for row in range(4):
        for col in range(4):
            if board[row][col] != 0:
                locations.append([row, col, board[row][col]])
    return locations


def make_graph(locations):
    graph = [[float("inf") for _ in range(7)] for _ in range(7)]  # 인형의 종류는 7

    for idx, loc in enumerate(locations):
        row, col, id1 = loc[0], loc[1], loc[2]
        for r, c, id2 in locations[idx + 1 :]:
            if row == r or col == c:
                graph[id1][id2] = 1
            else:
                graph[id1][id2] = 2
    return graph


def solution(board, r, c):
    locations = get_locations(board)
    graph = make_graph(locations)

    start_id = set()
    for i in range(4):
        if board[r][i] != 0:
            start_id.append(board[r][i])

    answer = 0
    return answer


board = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
r, c = 1, 0
print(solution(board, r, c))