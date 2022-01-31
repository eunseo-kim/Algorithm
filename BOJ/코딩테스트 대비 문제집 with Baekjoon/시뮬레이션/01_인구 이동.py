# 언어 : Python
# 날짜 : 2022.1.28
# 문제 : BOJ > 인구 이동 (https://www.acmicpc.net/problem/16234)
# 티어 : 골드 5
# ▷ 하루 동안 일어나는 일
# 인구수 A[r][c]
# L <= 인구 차이 <= R 이면 국경선 열림
# 국경선이 열려서 국경이 연결된 한 묶음 = 연합
# 연합인 칸의 인구수는 N분의 1
# ▷ 모든 국경선이 다 닫힐때까지 하루 반복
# ============================================================================

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def bfs(r, c, visited):
    queue = [(r, c)]
    unions = [(r, c)]
    while queue:
        row, col = queue.pop(0)
        for move in moves:
            new_r, new_c = row + move[0], col + move[1]
            if A[new_r][new_c] != -1 and not visited[new_r][new_c]:
                if L <= abs(A[row][col] - A[new_r][new_c]) <= R:
                    visited[new_r][new_c] = True
                    unions.append((new_r, new_c))
                    queue.append((new_r, new_c))

    moved = False
    if len(unions) > 1:
        moved = True
        sum = 0
        for r, c in unions:
            sum += A[r][c]
        average = sum // len(unions)
        for r, c in unions:
            A[r][c] = average

    return visited, moved


def solution():
    day = 0
    while True:
        visited = [[False for _ in range(N + 1)] for _ in range(N + 1)]
        finished = True
        for row in range(1, N + 1):
            for col in range(1, N + 1):
                if not visited[row][col]:
                    visited[row][col] = True
                    visited, moved = bfs(row, col, visited)
                    if moved:
                        finished = False

        if finished:
            break
        day += 1

    return day


# 입력 및 실행
N, L, R = map(int, input().split())
A = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
for r in range(1, N + 1):
    for c, num in enumerate(list(map(int, input().split())), 1):
        A[r][c] = num

print(solution())
