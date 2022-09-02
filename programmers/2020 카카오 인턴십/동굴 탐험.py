from collections import defaultdict, deque


def solution(n, path, order):
    graph = defaultdict(list)
    for v1, v2 in path:
        graph[v1].append(v2)
        graph[v2].append(v1)

    parent = [-1 for _ in range(n)]  # -1은 선방문 조건이 없는 경우
    child = [-1 for _ in range(n)]  # -1은 선방문 조건이 없는 경우
    for n1, n2 in order:
        parent[n2] = n1
        child[n1] = n2

    # 예외처리) 출발점(=0번 노드)에게 선방문 조건이 존재하는 경우
    START_NODE = 0
    if parent[START_NODE] != -1:
        return False

    queue = deque()
    visited = set()
    temp = [False for _ in range(n)]
    queue.append(START_NODE)
    while queue:
        node = queue.popleft()

        if len(visited) == n:
            return True

        if node in visited:
            continue
        visited.add(node)

        # 현재 방문한 node가 선방문(first_visit) 노드라면 second_visit도 통과시켜줌
        if child[node] != -1:
            second_node = child[node]
            if temp[node]:  # 만약 현재 방문한 노드가 temp 안에 넣어둔 선방문 노드인 경우
                queue.append(second_node)
                temp[node] = False
            child[node] = -1
            parent[second_node] = -1

        neighbors = graph[node]
        for neighbor in neighbors:
            # 만약 neighbor 노드의 first_visit을 아직 방문하지 않았다면?
            if parent[neighbor] != -1:
                temp[parent[neighbor]] = True  # 임시 저장소에 먼저 방문해야되는 노드 넣어놓기
                continue

            if neighbor not in visited:
                queue.append(neighbor)

    return len(visited) == n


#
n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]
result = solution(n, path, order)
print(result)