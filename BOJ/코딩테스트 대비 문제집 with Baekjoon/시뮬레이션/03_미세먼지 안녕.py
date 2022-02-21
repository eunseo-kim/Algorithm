# 언어 : Python
# 날짜 : 2022.2.21
# 문제 : BOJ > 미세먼지 안녕! (https://www.acmicpc.net/problem/17144)
# 티어 : 골드 4
# =========================================================================

import copy

moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def solution(graph):
    spread_graph = [[0 for _ in range(C)] for _ in range(R)]

    # 미세먼지 확산
    for r in range(R):
        for c in range(C):
            if graph[r][c] > 0:
                divided = graph[r][c] // 5
                for move in moves:
                    new_r = r + move[0]
                    new_c = c + move[1]
                    if 0 <= new_r < R and 0 <= new_c < C and graph[new_r][new_c] != -1:
                        spread_graph[new_r][new_c] += divided
                        spread_graph[r][c] -= divided

    for r in range(R):
        for c in range(C):
            spread_graph[r][c] += graph[r][c]

    result_graph = copy.deepcopy(spread_graph)

    # 공기청정기
    # 위쪽 (반시계 방향)
    result_graph[start_row][1] = 0
    result_graph[start_row + 1][1] = 0

    for i in range(2, C):
        result_graph[start_row][i] = spread_graph[start_row][i - 1]

    for i in range(start_row):
        result_graph[i][C - 1] = spread_graph[i + 1][C - 1]

    for i in range(C - 1):
        result_graph[0][i] = spread_graph[0][i + 1]

    for i in range(1, start_row + 1):
        result_graph[i][0] = spread_graph[i - 1][0]

    # 아래쪽 (시계방향)
    for i in range(2, C):
        result_graph[start_row + 1][i] = spread_graph[start_row + 1][i - 1]

    for i in range(start_row + 2, R):
        result_graph[i][C - 1] = spread_graph[i - 1][C - 1]

    for i in range(C - 1):
        result_graph[R - 1][i] = spread_graph[R - 1][i + 1]

    for i in range(start_row + 1, R - 1):
        result_graph[i][0] = spread_graph[i + 1][0]

    result_graph[start_row][0] = -1
    result_graph[start_row + 1][0] = -1

    return result_graph


R, C, T = map(int, input().split())

graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))

for r in range(R):
    if graph[r][0] == -1:
        start_row = r
        break

for _ in range(T):
    graph = solution(graph)

answer = 0
for r in range(R):
    for c in range(C):
        answer += graph[r][c]

print(answer + 2)