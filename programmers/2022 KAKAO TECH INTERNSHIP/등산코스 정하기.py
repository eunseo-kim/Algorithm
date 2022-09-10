from collections import defaultdict
import heapq


def solution(n, paths, gates, summits):
    SUMMITS = set(summits)
    GATES = set(gates)

    # make graph (weight을 기준으로 최소힙을 만들 예정)
    graph = defaultdict(list)
    for i, j, weight in paths:
        graph[i].append([weight, j])
        graph[j].append([weight, i])

    queue = []
    node_intensity = [float("inf") for _ in range(n + 1)]

    for gate in gates:
        heapq.heappush(queue, [0, gate])  # 시작점의 indensity는 가장 작은 0으로 설정

    while queue:
        intensity, node = heapq.heappop(queue)

        # 만약 현재 노드의 intensity값보다 크거나 같다면 더 이상 탐색 X
        if intensity >= node_intensity[node]:
            continue

        node_intensity[node] = intensity

        # 만약 산봉우리에 도달했다면 더 이상 탐색 X
        if node in SUMMITS:
            continue

        neighbors = graph[node]
        for w, neighbor in neighbors:
            # 다음 방문 지점이 출발지라면 더 이상 탐색 X
            if neighbor in GATES:
                continue

            # 현재 경로에서의 intensity 값이 다음에 방문할 노드의 기존 intensity보다 크거나 같다면 더 이상 탐색 X
            next_intensity = max(intensity, w)  # -> intensity는 현재 경로에서 가장 큰 거리값
            if next_intensity >= node_intensity[neighbor]:
                continue

            heapq.heappush(queue, [next_intensity, neighbor])

    answer = [None, float("inf")]  # [산봉우리의 번호, intensity의 최솟값]
    summits.sort()
    for summit in summits:
        if answer[1] > node_intensity[summit]:  # intensity가 최소가 되는 코스 중 summit 번호가 가장 작은 것
            answer = [summit, node_intensity[summit]]

    return answer


result = solution(7, [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]], [3, 7], [1, 5])
print(result)