# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (12) (https://www.acmicpc.net/problem/15666)
# 티어 : 실버 2
# =================================================================


def dfs(path, i):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    last_called = None

    for idx in range(i, N):
        if last_called != arr[idx]:
            last_called = arr[idx]
            dfs(path + [arr[idx]], idx)


N, M = map(int, input().split(" "))
arr = sorted(list(map(int, input().split(" "))))
dfs([], 0)