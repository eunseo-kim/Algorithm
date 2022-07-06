# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (4) (https://www.acmicpc.net/problem/15652)
# 티어 : 실버 3
# =================================================================


def dfs(path, i):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for i in range(i, N):
        dfs(path + [i + 1], i)


N, M = map(int, input().split(" "))
dfs([], 0)
