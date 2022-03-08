# 언어 : Python
# 날짜 : 2022.3.8
# 문제 : BOJ > 무기 공학 (https://www.acmicpc.net/problem/18430)
# 티어 : 골드 5
# ===============================================================

boomerangs = [[[0, -1], [1, 0]], [[0, -1], [-1, 0]], [[-1, 0], [0, 1]], [[0, 1], [1, 0]]]


def dfs(row, col, sum):
    global visited, result

    if col == C + 1:
        row += 1
        col = 1

    if row == R + 1:
        result = max(result, sum)
        return

    if not visited[row][col]:
        for boomerang in boomerangs:
            is_valid = True
            for b_row, b_col in boomerang:
                new_r, new_c = row + b_row, col + b_col
                if visited[new_r][new_c] or graph[new_r][new_c] == -1:
                    is_valid = False
                    break
            if is_valid:
                visited[row][col] = True
                new_sum = sum + graph[row][col] * 2
                for b_row, b_col in boomerang:
                    new_r, new_c = row + b_row, col + b_col
                    visited[new_r][new_c] = True
                    new_sum += graph[new_r][new_c]
                dfs(row, col + 1, new_sum)
                visited[row][col] = False
                for b_row, b_col in boomerang:
                    new_r, new_c = row + b_row, col + b_col
                    visited[new_r][new_c] = False

    dfs(row, col + 1, sum)


result = -float("inf")
R, C = map(int, input().split())
visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]
graph = [[-1 for _ in range(C + 2)]]
for _ in range(R):
    graph.append([-1] + list(map(int, input().split())) + [-1])
graph.append([-1 for _ in range(C + 2)])

dfs(1, 1, 0)
print(result)