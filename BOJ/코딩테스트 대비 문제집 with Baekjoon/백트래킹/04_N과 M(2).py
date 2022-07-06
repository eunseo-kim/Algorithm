# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (2) (https://www.acmicpc.net/problem/15650)
# 티어 : 실버 3
# =================================================================


def dfs(path, idx):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for i in range(idx + 1, N):
        dfs(path + [i + 1], i)


N, M = map(int, input().split(" "))
dfs([], -1)