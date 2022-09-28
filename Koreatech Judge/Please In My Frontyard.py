from copy import deepcopy
import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

answer = None


def solution(graph, missing_cnt, missing_locs):
    global answer

    rows = []
    cols = []
    blocks = []

    for row in range(9):
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        for col in range(9):
            if graph[row][col] != ".":
                alphabets.remove(graph[row][col])
        rows.append(alphabets)

    for col in range(9):
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        for row in range(9):
            if graph[row][col] != ".":
                alphabets.remove(graph[row][col])
        cols.append(alphabets)

    block_locs = [[0, 0], [0, 3], [0, 6], [3, 0], [3, 3], [3, 6], [6, 0], [6, 3], [6, 6]]
    for b_row, b_col in block_locs:
        alphabets = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
        for row in range(b_row, b_row + 3):
            for col in range(b_col, b_col + 3):
                if graph[row][col] != ".":
                    alphabets.remove(graph[row][col])

        blocks.append(alphabets)

    block_indexs = [[0 for _ in range(9)] for _ in range(9)]
    for r in range(9):
        for c in range(9):
            # block index 찾기
            b_row, b_col = 0, 0
            if r < 3:  # 0~2
                b_row = 0
            elif r < 6:  # 3~5
                b_row = 3
            else:  # 6~8
                b_row = 6

            if c < 3:
                b_col = 0
            elif c < 6:
                b_col = 1
            else:
                b_col = 2
            block_indexs[r][c] = b_row + b_col

    def dfs(missing_loc, rows, cols, blocks, graph, cnt):
        global answer

        if missing_loc == missing_cnt:
            answer = deepcopy(graph)
            return

        r, c = missing_locs[missing_loc]
        b_index = block_indexs[r][c]

        for alpha in ["A", "B", "C", "D", "E", "F", "G", "H", "I"]:
            if alpha in rows[r] and alpha in cols[c] and alpha in blocks[b_index]:
                # 지우고 다시 remove
                rows[r].remove(alpha)
                cols[c].remove(alpha)
                blocks[b_index].remove(alpha)
                graph[r][c] = alpha
                dfs(missing_loc + 1, rows, cols, blocks, graph, cnt + 1)

                rows[r].append(alpha)
                cols[c].append(alpha)
                blocks[b_index].append(alpha)
                graph[r][c] = "."

    dfs(0, rows, cols, blocks, graph, 0)
    return answer


graph = []
for i in range(9):
    graph.append(list(map(str, input().split())))

missing_cnt = 0
missing_locs = []
for r in range(9):
    for c in range(9):
        if graph[r][c] == ".":
            missing_cnt += 1
            missing_locs.append([r, c])

solution(graph, missing_cnt, missing_locs)
for a in answer:
    print(" ".join(map(str, a)))
