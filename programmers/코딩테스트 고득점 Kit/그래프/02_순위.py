# 언어 : Python
# 날짜 : 2022.06.30
# 문제 : Programmers > 순위
# 티어 : Lv 3
# ==============================================================

# 현재 player을 기준으로 하위 노드들에게 player 정보를 전파합니다.
def bfs(player, graph, dict, n):
    visited = [False for _ in range(n + 1)]
    stack = [player]

    while stack:
        node = stack.pop()
        visited[node] = True
        children = graph[node]
        for child in children:
            if not visited[child]:
                dict[player].add(child)
                stack.append(child)


def solution(n, results):
    # [0] 초기화
    graph = {}
    reversed_graph = {}
    win_dict = {}  # 내가 이긴 사람
    lose_dict = {}  # 나한테 진 사람

    for player in range(1, n + 1):
        graph[player] = []
        reversed_graph[player] = []
        win_dict[player] = set()
        lose_dict[player] = set()

    # [1] results 정보를 바탕으로 그래프를 만듭니다.
    for p1, p2 in results:
        if p1 not in graph.keys():
            graph[p1] = []
        graph[p1].append(p2)

    for p1, p2 in results:
        if p1 not in reversed_graph.keys():
            reversed_graph[p2] = []
        reversed_graph[p2].append(p1)

    # [2] 내가 이긴 사람 / 나한테 진 사람을 구합니다.
    for player in range(1, n + 1):
        bfs(player, graph, win_dict, n)

    for player in range(1, n + 1):
        bfs(player, reversed_graph, lose_dict, n)

    # [3] 내가 이긴 사람 + 나한테 진 사람 + 나 == n 을 만족하면 순위를 결정할 수 있습니다.
    answer = 0
    for player in range(1, n + 1):
        if len(win_dict[player]) + len(lose_dict[player]) == n - 1:
            answer += 1

    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
answer = solution(n, results)
print(answer)