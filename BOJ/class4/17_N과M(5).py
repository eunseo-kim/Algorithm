# 언어 : Python
# 날짜 : 2021.09.24
# 문제 : BOJ > N과 M(5) (https://www.acmicpc.net/problem/15654)
# 티어 : 실버 3
# ==========================================================


def dfs(path):
    if len(path) == M:
        answer.append(path)
        return

    for i in range(N):
        if arr[i] not in path:
            dfs(path + [arr[i]])


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
answer = []
for idx in range(N):
    dfs([arr[idx]])

answer.sort()
for ans in answer:
    print(" ".join(map(str, ans)))