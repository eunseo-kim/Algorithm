# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (5) (https://www.acmicpc.net/problem/15654)
# 티어 : 실버 3
# =================================================================


def dfs(path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    for num in arr:
        if num not in path:
            dfs(path + [num])


# 입력
N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()
dfs([])
