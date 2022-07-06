# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (3) (https://www.acmicpc.net/problem/15651)
# 티어 : 실버 3
# =================================================================

def dfs(path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return
    
    for i in range(1, N+1):
        dfs(path + [i])

N, M = map(int, input().split(" "))
dfs([])