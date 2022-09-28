from collections import deque


def in_range(N, r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution(N, graph):
    queue = deque()
    queue.append([0, 0])
    dist = [[float("inf") for _ in range(N)] for _ in range(N)]

    if graph[0][0] == 1:
        dist[0][0] = 0

    while queue:
        r, c = queue.popleft()

        if r == N - 1 and c == N - 1:
            break

        for m_r, m_c in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            n_r = r + m_r
            n_c = c + m_c
            if in_range(N, n_r, n_c) and graph[n_r][n_c] == 1:
                if dist[n_r][n_c] > dist[r][c] + 1:
                    dist[n_r][n_c] = dist[r][c] + 1
                    queue.append([n_r, n_c])

    return dist[N - 1][N - 1]


N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

result = solution(N, graph)

if result == float("inf"):
    print(-1)
elif result <= 2:
    print(result)
else:
    go_back = (result - 2) * 3
    forward = 2
    print(go_back + forward)
