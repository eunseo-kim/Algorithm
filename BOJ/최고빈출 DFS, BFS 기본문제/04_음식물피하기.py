# 언어 : Python
# 날짜 : 2021.08.23
# 문제 : BOJ > 음식물 피하기 (https://www.acmicpc.net/problem/1743)
# 티어 : 실버 1
# ======================================================================
import sys

sys.setrecursionlimit(100000)


def dfs(r, c):
    global cur_ans
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    for i in range(4):
        nr, nc = dx[i] + r, dy[i] + c
        if 0 <= nr < R and 0 <= nc < C:
            if not visited[nr][nc] and arr[nr][nc] == "#":
                cur_ans += 1
                visited[nr][nc] = True
                dfs(nr, nc)


# 입력 및 실행
R, C, K = map(int, input().split())
arr = [["." for _ in range(C)] for _ in range(R)]

for _ in range(K):
    r, c = map(int, input().split())
    arr[r - 1][c - 1] = "#"

visited = [[False for _ in range(C)] for _ in range(R)]
answer = 0
for r in range(R):
    for c in range(C):
        if not visited[r][c] and arr[r][c] == "#":
            visited[r][c] = True
            cur_ans = 1
            dfs(r, c)
            answer = max(answer, cur_ans)

# 정답
print(answer)