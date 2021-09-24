# 언어 : Python
# 날짜 : 2021.09.23
# 문제 : BOJ > N과M (https://www.acmicpc.net/problem/15650)
# 티어 : 실버 3
# ==========================================================


def dfs(n, path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for i in range(n + 1, N + 1):
        dfs(i, path + [i])


N, M = map(int, input().split())
for i in range(1, N + 1):
    dfs(i, [i])