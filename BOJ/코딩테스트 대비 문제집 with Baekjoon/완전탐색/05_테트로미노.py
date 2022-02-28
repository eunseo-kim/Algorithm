# 언어 : Python
# 날짜 : 2022.2.28
# 문제 : BOJ > 테트로미노 (https://www.acmicpc.net/problem/14500)
# 티어 : 골드 5
# =========================================================================

tetromino = [
    [[0, 0], [1, 0], [2, 0], [3, 0]],
    [[0, 0], [0, 1], [0, 2], [0, 3]],
    [[0, 0], [0, 1], [1, 0], [1, 1]],
    [[0, 0], [1, 0], [2, 0], [2, 1]],
    [[0, 0], [0, 1], [0, 2], [-1, 2]],
    [[0, 0], [0, 1], [1, 1], [2, 1]],
    [[0, 0], [1, 0], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 0], [2, 0]],
    [[0, 0], [0, 1], [0, 2], [1, 2]],
    [[0, 1], [1, 1], [2, 1], [2, 0]],
    [[0, 0], [1, 0], [1, 1], [1, 2]],
    [[0, 0], [1, 0], [1, 1], [2, 1]],
    [[1, 0], [1, 1], [2, 0], [0, 1]],
    [[1, 0], [1, 1], [0, 1], [0, 2]],
    [[0, 0], [0, 1], [1, 1], [1, 2]],
    [[1, 0], [1, 1], [0, 1], [1, 2]],
    [[0, 0], [1, 0], [2, 0], [1, 1]],
    [[0, 0], [0, 1], [0, 2], [1, 1]],
    [[0, 1], [1, 1], [2, 1], [1, 0]],
]


def solution():
    max_sum = -float("inf")

    for row in range(R):
        for col in range(C):
            for tet in tetromino:
                cur_sum = 0
                is_valid = True
                for r, c in tet:
                    new_r = row + r
                    new_c = col + c
                    if 0 <= new_r < R and 0 <= new_c < C:
                        cur_sum += graph[new_r][new_c]
                    else:
                        is_valid = False
                        break
                if is_valid:
                    max_sum = max(max_sum, cur_sum)

    print(max_sum)


R, C = map(int, input().split())
graph = []
for _ in range(R):
    graph.append(list(map(int, input().split())))
solution()