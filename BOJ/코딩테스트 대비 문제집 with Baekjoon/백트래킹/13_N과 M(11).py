# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (2) (https://www.acmicpc.net/problem/15665)
# 티어 : 실버 2
# =================================================================


def dfs(path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    last_called = None

    for idx in range(N):
        if last_called != arr[idx]:
            last_called = arr[idx]
            dfs(path + [arr[idx]])


N, M = map(int, input().split(" "))
arr = sorted(list(map(int, input().split(" "))))
dfs([])