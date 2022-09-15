"""
A, B가 합승하는 지점을 K라고 가정했을 때,
1) S ~ K 까지의 최소경로
2) K ~ A 까지의 최소경로
3) K ~ B 까지의 최소경로
1 + 2 + 3을 구한다.
"""

INF = float("inf")


def solution(n, s, a, b, fares):
    def floyd_warshall():
        graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

        # x → x의 경로 비용은 0
        for i in range(n + 1):
            graph[i][i] = 0

        # fares 정보에 따라 graph 초기 세팅
        for n1, n2, w in fares:
            graph[n1][n2] = min(graph[n1][n2], w)
            graph[n2][n1] = min(graph[n2][n1], w)

        # 중간경로를 거치고 가는 것이 더 효율적인지 탐색하기
        for k in range(1, n + 1):
            for a in range(1, n + 1):
                for b in range(1, n + 1):
                    graph[a][b] = min(graph[a][b], graph[a][k] + graph[b][k])

        return graph

    graph = floyd_warshall()
    answer = INF
    # 합승 지점 k(k는 1~n 사이의 임의의 수)에 대해 최소 경로 합을 구하기
    for k in range(1, n + 1):
        answer = min(answer, graph[s][k] + graph[k][a] + graph[k][b])

    return answer


result = solution(
    6, 4, 5, 6, [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11], [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]
)
print(result)