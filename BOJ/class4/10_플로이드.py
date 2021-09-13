# 언어 : Python
# 날짜 : 2021.09.07
# 문제 : BOJ > 플로이드 (https://www.acmicpc.net/problem/11404)
# 티어 : 골드 4
# ===========================================================================
INF = float("inf")


def floyd_warshall():
    global graph
    for via in range(N):
        for i in range(N):
            for j in range(N):
                graph[i][j] = min(graph[i][j], graph[i][via] + graph[via][j])

    for i in range(N):
        for j in range(N):
            if graph[i][j] == INF:
                graph[i][j] = 0

    return graph


def solution():
    result = floyd_warshall()

    for re in result:
        print(" ".join(map(str, re)))

# 입력 및 실행
N = int(input())
T = int(input())
graph = [[INF for _ in range(N)] for _ in range(N)]
for i in range(N):
    graph[i][i] = 0

for _ in range(T):
    i, j, w = map(int, input().split())
    graph[i - 1][j - 1] = min(graph[i - 1][j - 1], w)

solution()