# 언어 : Python
# 날짜 : 2022.2.25
# 문제 : BOJ > 공주님을 구해라! (https://www.acmicpc.net/problem/17836)
# 티어 : 골드 5
# =========================================================================

moves = [[-1, 0], [0, -1], [1, 0], [0, 1]]


def solution():
    min_hour = float("inf")
    visited = [[False for _ in range(C + 2)] for _ in range(R + 2)]
    queue = [[1, 1, 0]]  # row, col, hour
    while queue:
        row, col, hour = queue.pop(0)
        if not visited[row][col]:
            visited[row][col] = True

            if graph[row][col] == 2:
                min_hour = min(min_hour, hour + (R - row) + (C - col))
            if row == R and col == C:
                min_hour = min(min_hour, hour)

            for r, c in moves:
                new_r, new_c = row + r, col + c
                if not visited[new_r][new_c] and graph[new_r][new_c] not in [-1, 1]:
                    queue.append([new_r, new_c, hour + 1])

    return min_hour


R, C, T = map(int, input().split())
graph = [[-1 for _ in range(C + 2)]]
for _ in range(R):
    graph.append([-1] + list(map(int, input().split())) + [-1])
graph.append([-1 for _ in range(C + 2)])

result = solution()
if result == float("inf"):
    print("Fail")
elif result > T:
    print("Fail")
else:
    print(result)