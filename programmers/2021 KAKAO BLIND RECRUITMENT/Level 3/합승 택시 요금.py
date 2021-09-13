# 언어 : Python
# 날짜 : 2021.06.26
# 문제 : Programmers > Lv3 > 합승 택시 요금
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# =================================================================
# 소요 시간 : 56분 / 카카오 해설 참고 + floyd warshall 알고리즘 참고
# 제출 시도 : 1회
# =================================================================
from collections import defaultdict


def make_graph(n, fares):
    graph = [[0 if (i == j) else float("inf") for i in range(n)] for j in range(n)]

    for u, v, w in fares:
        graph[u - 1][v - 1] = w
        graph[v - 1][u - 1] = w

    return graph


def floyd_warshall(n, graph):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if graph[i][k] + graph[k][j] < graph[i][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph


def solution(n, s, a, b, fares):
    graph = make_graph(n, fares)
    graph = floyd_warshall(n, graph)

    min_fare = float("inf")
    for k in range(n):
        min_fare = min(min_fare, graph[s - 1][k] + graph[k][a - 1] + graph[k][b - 1])
    return min_fare


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
solution(n, s, a, b, fares)