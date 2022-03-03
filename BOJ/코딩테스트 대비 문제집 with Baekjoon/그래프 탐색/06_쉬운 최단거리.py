# 언어 : Python
# 날짜 : 2022.3.3
# 문제 : BOJ > 쉬운 최단거리 (https://www.acmicpc.net/problem/14940)
# 티어 : 골드 5
# =========================================================================


moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]


def solution():
    queue = [[R, C, 0]]
    visited = [[False for _ in range(col + 2)] for _ in range(row + 2)]
    result = [[-1 for _ in range(col + 2)] for _ in range(row + 2)]

    # 원래 갈 수 없는 땅
    for r in range(1, row + 1):
        for c in range(1, col + 1):
            if graph[r][c] == 0:
                result[r][c] = 0
                visited[r][c] = True

    while queue:
        r, c, dist = queue.pop(0)
        if not visited[r][c]:
            visited[r][c] = True
            result[r][c] = dist

            for move in moves:
                new_r = r + move[0]
                new_c = c + move[1]

                if graph[new_r][new_c] != -1 and not visited[new_r][new_c]:
                    queue.append([new_r, new_c, dist + 1])

    for r in range(1, row + 1):
        for c in range(1, col + 1):
            print(result[r][c], end=" ")
        print()


row, col = map(int, input().split())
graph = [[-1 for _ in range(col + 2)]]
for _ in range(row):
    graph.append([-1] + list(map(int, input().split())) + [-1])
graph.append([-1 for _ in range(col + 2)])

# 2(목표 위치) 찾기
find = False
for r in range(1, row + 1):
    for c in range(1, col + 1):
        if graph[r][c] == 2:
            R, C = r, c
            find = True
            break
    if find:
        break

solution()