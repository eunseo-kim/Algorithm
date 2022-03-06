# 언어 : Python
# 날짜 : 2022.3.5
# 문제 : BOJ > 마법사 상어와 파이어스톰 (https://www.acmicpc.net/problem/20058)
# 티어 : 골드 4
# =============================================================================


def rotate(gap, row, col):
    global graph

    # tmp에 복사하기
    tmp = []
    for r in range(row, row + gap):
        tmp.append(graph[r][col : col + gap])

    # tmp를 회전해서 graph를 갱신
    for r in range(gap):
        for c in range(gap):
            graph[row + r][col + c] = tmp[gap - c - 1][r]


def solution(l):
    global graph

    # rotate
    for row in range(1, n + 1, l):
        for col in range(1, n + 1, l):
            rotate(l, row, col)

    # 얼음 3개와 닿아있지 않은 곳
    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    delete = []
    for r in range(1, n + 1):
        for c in range(1, n + 1):
            if graph[r][c] != 0:
                count = 0
                for m_row, m_col in moves:
                    new_r, new_c = r + m_row, c + m_col
                    if graph[new_r][new_c] == 0:
                        count += 1
                if count > 1:
                    delete.append([r, c])

    # 얼음의 양 1 줄기
    for r, c in delete:
        graph[r][c] -= 1


def dfs(row, col):
    global visited
    queue = [[row, col]]
    size = 0

    moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    while queue:
        curr = queue.pop()
        if not visited[curr[0]][curr[1]] and graph[curr[0]][curr[1]] != 0:
            visited[curr[0]][curr[1]] = True
            size += 1

            for m_r, m_c in moves:
                new_r, new_c = curr[0] + m_r, curr[1] + m_c
                if not visited[new_r][new_c] and graph[new_r][new_c] != 0:
                    queue.append([new_r, new_c])

    return size


N, Q = map(int, input().split())
n = pow(2, N)
graph = [[0 for _ in range(n + 2)]]
for _ in range(n):
    graph.append([0] + list(map(int, input().split())) + [0])
graph.append([0 for _ in range(n + 2)])
L_list = list(map(int, input().split()))

for i in range(Q):
    L = pow(2, L_list[i])
    solution(L)

# 남아있는 얼음의 합 구하기
result_sum = 0
for r in range(n + 1):
    for c in range(n + 1):
        result_sum += graph[r][c]

# dfs로 가장 큰 얼음 덩어리 구하기
max_size = 0
visited = [[False for _ in range(n + 2)] for _ in range(n + 2)]
for r in range(1, n + 1):
    for c in range(1, n + 1):
        max_size = max(max_size, dfs(r, c))

print(result_sum)
print(max_size)