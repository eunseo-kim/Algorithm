from collections import defaultdict
from copy import deepcopy

# 단방향 그래프 만들기
def make_graph(edges):
    graph = defaultdict(list)
    for n1, n2 in edges:
        graph[n1].append(n2)
    return graph


# global
max_sheep_count = 0


def solution(info, edges):
    graph = make_graph(edges)

    def dfs(curr, sheep, wolf, path):
        global max_sheep_count

        if info[curr] == 0:  # 양
            sheep += 1
        else: # 늑대
            wolf += 1

        # 만약 건널 수 없다면 리턴
        if sheep <= wolf:
            return

        max_sheep_count = max(max_sheep_count, sheep)

        for node in path:  # 현재 연결된 모든 노드들에 대하여
            for neighbor in graph[node]:  # 인접해있는 노드들 중
                if neighbor not in path:  # 아직 방문하지 않은 노드들을 방문하면서 확장해가기
                    path.append(neighbor)
                    dfs(neighbor, sheep, wolf, deepcopy(path))
                    path.pop()

    dfs(0, 0, 0, [0])
    return max_sheep_count


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
result = solution(info, edges)
print(result)