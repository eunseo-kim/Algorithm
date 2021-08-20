# 언어 : Python
# 날짜 : 2021.08.20
# 문제 : BOJ > 전쟁 - 전투 (https://www.acmicpc.net/problem/1303)
# 티어 : 실버 1
# ======================================================================

from collections import defaultdict


def dfs(r, c, team):
    global score
    global check
    score += 1

    if r + 1 < R and not check[r + 1][c] and soldiers[r + 1][c] == team:
        check[r + 1][c] = True
        dfs(r + 1, c, team)

    if r - 1 >= 0 and not check[r - 1][c] and soldiers[r - 1][c] == team:
        check[r - 1][c] = True
        dfs(r - 1, c, team)

    if c + 1 < C and not check[r][c + 1] and soldiers[r][c + 1] == team:
        check[r][c + 1] = True
        dfs(r, c + 1, team)

    if c - 1 >= 0 and not check[r][c - 1] and soldiers[r][c - 1] == team:
        check[r][c - 1] = True
        dfs(r, c - 1, team)


C, R = map(int, input().split())
check = [[False for _ in range(C)] for _ in range(R)]
soldiers = []
for _ in range(R):
    soldiers.append(list(input()))

score_board = defaultdict(int)
for r in range(R):
    for c in range(C):
        if not check[r][c]:
            check[r][c] = True
            score = 0
            team = soldiers[r][c]
            dfs(r, c, team)
            score_board[team] += score * score


print(score_board["W"], score_board["B"])

soldiers = [
    ["W", "B", "W", "W", "W"],
    ["W", "W", "W", "W", "W"],
    ["B", "B", "B", "B", "B"],
    ["B", "B", "B", "W", "W"],
    ["W", "W", "W", "W", "W"],
]
