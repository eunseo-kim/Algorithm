# 언어 : Python
# 날짜 : 2022.3.5
# 문제 : BOJ > 마법사 상어와 파이어스톰 (https://www.acmicpc.net/problem/20058)
# 티어 : 골드 4
# =============================================================================


def rotate(l, row, col):
    global changed_graph
    N = l

    while N > 0:
        for r in range(row, row + l):
            for c in range(col, col + l):
                changed_graph[r][c] = graph[c][N - 1 - r]

        N -= 2

    for g in changed_graph:
        print(g)
    print("===")


def solution(l):
    print("check1:", l)
    global graph

    # rotate
    for row in range(1, n + 1, l):
        for col in range(1, n + 1, l):
            rotate(l, row, col)
    graph = changed_graph


N, Q = map(int, input().split())
n = pow(2, N)
graph = [[0 for _ in range(n + 2)]]
changed_graph = [[0 for _ in range(n + 2)] for _ in range(n + 2)]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0 for _ in range(n + 2)])
L_list = list(map(int, input().split()))

for i in range(Q):
    L = pow(2, L_list[i])
    solution(L)