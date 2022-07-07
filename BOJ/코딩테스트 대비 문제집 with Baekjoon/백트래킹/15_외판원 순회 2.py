# 언어 : Python
# 날짜 : 2022.7.7
# 문제 : BOJ > 외판원 순회 2 (https://www.acmicpc.net/problem/10971)
# 티어 : 실버 2
# =================================================================

from collections import defaultdict


def make_graph(W):
    graph = defaultdict(list)

    for i in range(N):
        for j in range(N):
            if W[i][j] != 0:
                graph[i].append([W[i][j], j])
    return graph


def dfs(curr, path, weight):
    global answer

    if False not in visited and curr == start_node:
        answer = min(answer, weight)
        return

    routes = graph[curr]
    for w, r in routes:
        if not visited[r]:
            visited[r] = True
            dfs(r, path + [r], weight + w)
            visited[r] = False


# 입력 및 실행
N = int(input())
W = []
for _ in range(N):
    W.append(list(map(int, input().split(" "))))

start_node = 0
visited = [False for _ in range(N)]
answer = float("inf")

graph = make_graph(W)
dfs(start_node, [start_node], 0)
print(answer)