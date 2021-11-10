# 언어 : Python
# 날짜 : 2021.11.10
# 문제 : BOJ > 벽 부수고 이동하기(https://www.acmicpc.net/problem/2206)
# 티어 : 골드 4
# 해결방법
#   ▶최단거리 구하기? → BFS
#   ▶[현재까지 최단 거리, 벽 부수기 가능 여부] 저장하기
#   ▶왔던 길 체크하는 visited
#     - 3차원 visited로 만들어야 풀 수 있는듯? visited[row][col][2]
#     - visited[row][col][벽 방문 여부]
#     - 벽 방문 여부 : 0이면 방문 X, 1이면 방문 O
# 새롭게 배운 점
#   ▶BFS는 방문 표시를 큐에서 뺀 다음이 아니라 큐에 넣을 때 해야 한다!★
# =====================================================================

import heapq

move = [[0, 1], [1, 0], [-1, 0], [0, -1]]


def solution():
    dist, row, col, breakable, wall = 1, 0, 0, True, 0
    queue = [[dist, row, col, breakable, wall]]

    while queue:
        d, r, c, is_breakable, wall_check = heapq.heappop(queue)
        if r == N - 1 and c == M - 1:
            return d

        for m in move:
            new_row = r + m[0]
            new_col = c + m[1]

            if 0 <= new_row < N and 0 <= new_col < M:
                if board[new_row][new_col] == "0" and not visited[new_row][new_col][wall_check]:
                    visited[new_row][new_col][wall_check] = True
                    value = [d + 1, new_row, new_col, is_breakable, wall_check]
                    heapq.heappush(queue, value)
                elif board[new_row][new_col] == "1" and is_breakable and not visited[new_row][new_col][wall_check]:
                    visited[new_row][new_col][wall_check] = True
                    value = [d + 1, new_row, new_col, False, 1]
                    heapq.heappush(queue, value)

    return -1


# 입력 및 실행
N, M = map(int, input().split())
board = []
visited = []
for _ in range(N):
    board.append(list(input()))
    visited.append([[False, False] for _ in range(M)])  # 0은 벽 방문 X, 1은 벽 방문 O
print(solution())
