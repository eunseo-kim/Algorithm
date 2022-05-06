from collections import defaultdict

max_sheep = 0


def solution(info, edges):
    type = {
        "sheep": 0,
        "wolf": 1,
    }

    N = len(info)

    children = defaultdict(list)
    for p, c in edges:
        children[p].append(c)

    def dfs(index, wolf, sheep, visited, can_go):
        global max_sheep

        if visited[index]:
            return
        visited[index] = True

        if info[index] == type["sheep"]:
            sheep += 1
            max_sheep = max(sheep, max_sheep)
        else:
            wolf += 1

        if wolf >= sheep:
            return

        new_go = can_go.copy()
        for child in children[index]:
            if not visited[child]:
                new_go.add(child)

        for route in new_go:
            if not visited[route]:
                dfs(route, wolf, sheep, visited[:], new_go)

        return max_sheep

    visited = [False for _ in range(N)]

    dfs(0, 0, 0, visited, set(children[0]))

    return max_sheep


info = [0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1]
edges = [[0, 1], [1, 2], [1, 4], [0, 8], [8, 7], [9, 10], [9, 11], [4, 3], [6, 5], [4, 6], [8, 9]]
result = solution(info, edges)
print(result)