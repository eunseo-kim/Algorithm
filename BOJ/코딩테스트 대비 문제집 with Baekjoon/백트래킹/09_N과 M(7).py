# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (7) (https://www.acmicpc.net/problem/15656)
# 티어 : 실버 3
# =================================================================

def dfs(path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    for i in range(N):
        dfs(path + [arr[i]])


N, M = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
arr.sort()
dfs([])