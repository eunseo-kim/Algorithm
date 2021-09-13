# 언어 : Python
# 날짜 : 2021.08.26
# 문제 : BOJ > 아기 상어2 (https://www.acmicpc.net/problem/17086)
# 티어 : 실버 2
# 풀이 : 각 칸마다 최소 거리를 구하는 방식은 시간 초과가 걸렸다.
# 대신 상어의 거리로부터 각 칸의 최소 거리를 갱신하는 방법으로 풀었다.
# ======================================================================


def bfs(r, c):
    global distances
    nr = [1, 1, 1, -1, -1, -1, 0, 0]
    nc = [1, 0, -1, 1, -1, 0, 1, -1]
    stack = [[r, c, 0]]
    while stack:
        row, col, dist = stack.pop(0)

        for i in range(8):
            next_row, next_col = row + nr[i], col + nc[i]
            if 0 <= next_row < R and 0 <= next_col < C and dist + 1 < distances[next_row][next_col]:
                distances[next_row][next_col] = dist + 1
                stack.append([next_row, next_col, dist + 1])


# 입력 및 실행
R, C = map(int, input().split())
shark = []
for _ in range(R):
    shark.append(list(map(int, input().split())))
distances = [[float("inf") for _ in range(C)] for _ in range(R)]

for r in range(R):
    for c in range(C):
        if shark[r][c] == 1:
            distances[r][c] = 0
            bfs(r, c)

answer = 0
# 최댓값 구하기
for dist in distances:
    answer = max(max(dist), answer)
print(answer)