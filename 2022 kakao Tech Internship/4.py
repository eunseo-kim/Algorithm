from collections import deque
from copy import deepcopy


def solution(n, paths, gates, summits):
    graph = dict()

    for a, b, w in paths:
        graph[a] = []
        graph[b] = []

    for a, b, w in paths:
        graph[a].append([b, w])
        graph[b].append([a, w])

    min_intensity = float("inf")
    result = []

    for gate in gates:
        visited, summit_num = False, -1  # 산봉우리 방문했니?, 산봉우리 번호
        start_gate, loc, intensity = gate, gate, 0  # 시작 위치, 현재 위치, 최소 휴식 불가능 경로
        path_visited = [[False for i in range(n + 1)] for _ in range(n + 1)]
        queue = deque()
        queue.append([visited, summit_num, start_gate, loc, intensity, deepcopy(path_visited)])

        while queue:
            visited, summit_num, start_gate, loc, intensity, path_visited = queue.popleft()

            # 만약 산봉우리 방문했으면 현재 위치가 start_gate인지 확인
            if visited:
                if loc == start_gate:
                    if intensity < min_intensity:
                        min_intensity = intensity
                        result = [summit_num, min_intensity]
                    elif intensity == min_intensity:
                        if result[0] > summit_num:
                            result = [summit_num, min_intensity]

            neighbors = graph[loc]

            for neighbor, next_intensity in neighbors:
                if not visited:
                    if neighbor not in gates:
                        if not path_visited[loc][neighbor]:
                            if neighbor in summits:
                                path_visited[loc][neighbor] = True
                                queue.append(
                                    [
                                        True,
                                        neighbor,
                                        start_gate,
                                        neighbor,
                                        max(intensity, next_intensity),
                                        deepcopy(path_visited),
                                    ]
                                )
                                path_visited[loc][neighbor] = False
                            else:
                                path_visited[loc][neighbor] = True
                                queue.append(
                                    [
                                        visited,
                                        summit_num,
                                        start_gate,
                                        neighbor,
                                        max(intensity, next_intensity),
                                        deepcopy(path_visited),
                                    ]
                                )
                                path_visited[loc][neighbor] = False

                else:
                    if neighbor == start_gate:
                        if not path_visited[loc][neighbor]:
                            path_visited[loc][neighbor] = True
                            queue.append(
                                [
                                    visited,
                                    summit_num,
                                    start_gate,
                                    neighbor,
                                    max(intensity, next_intensity),
                                    deepcopy(path_visited),
                                ]
                            )
                            path_visited[loc][neighbor] = False
                    elif neighbor not in gates:
                        if neighbor not in summits:
                            if not path_visited[loc][neighbor]:
                                path_visited[loc][neighbor] = True
                                queue.append(
                                    [
                                        visited,
                                        summit_num,
                                        start_gate,
                                        neighbor,
                                        max(intensity, next_intensity),
                                        deepcopy(path_visited),
                                    ]
                                )
                                path_visited[loc][neighbor] = False

    return result


n = 6
paths = [[1, 2, 3], [2, 3, 5], [2, 4, 2], [2, 5, 4], [3, 4, 4], [4, 5, 3], [4, 6, 1], [5, 6, 1]]
# 등산로, 등산로, 시간
gates = [1, 3]  # 출입구
summits = [5]  # 산봉우리
result = solution(n, paths, gates, summits)
print(result)  # [산봉우리의 번호, intensity의 최솟값]
