# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (1) (https://www.acmicpc.net/problem/15649)
# 티어 : 실버 3
# =================================================================


def dfs(path, N, M):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for i in range(1, N + 1):
        if i not in path:
            dfs(path + [i], N, M)

# 입력
N, M = map(int, input().split(" "))
result = []
dfs([], N, M)
