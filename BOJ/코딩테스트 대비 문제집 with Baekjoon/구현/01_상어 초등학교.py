# 언어 : Python
# 날짜 : 2022.1.27
# 문제 : BOJ > 상어 초등학교(https://www.acmicpc.net/problem/21608)
# 티어 : 실버 1
# 시간 : 52분
# ① HOW
# 첫번째 학생은 무조건 (2, 2)에 들어간다.
# 각 학생마다 매번 전체 그래프를 차례대로 돌면서 [최대힙]에 차례대로 넣는다.
#   1. 상하좌우에 좋아하는 학생이 몇 명 있는지 (최대힙이니까 음수로 넣는다.)
#   2. 상하좌우에 빈 칸이 몇 개 있는지 (최대힙이니까 음수로 넣는다.)
#   3. 현재 위치의 row
#   4. 현재 위치의 col
# ② NEW
# - 파이썬의 heapq는 최소힙을 지원한다. 최대힙으로 사용하려면 음수를 붙인다.
# - i가 1부터 시작하는 그래프는 (N+2)*(N+2) 그래프로 만들어 사용하면 편하다.
# ✔ 시간복잡도
# 3 ≤ N ≤ 20
# heapq를 쓰지 않고 N번을 돈다고 해도 사실 O(N^4)이다.
# 따라서 완전탐색으로 구현해도 문제 없다. 입력이 최대 20이여서..
# ============================================================================

import heapq

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def calc_sum(graph):
    satisfaction = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
    sum = 0

    for row in range(1, N + 1):
        for col in range(1, N + 1):
            count = 0
            for move in moves:
                n_row, n_col = row + move[0], col + move[1]
                if graph[n_row][n_col] in favorite[graph[row][col]]:
                    count += 1
            sum += satisfaction[count]

    return sum


def solution():
    graph[2][2] = students[0]

    for student in students[1:]:
        queue = []
        for row in range(1, N + 1):
            for col in range(1, N + 1):
                favorite_count = 0
                empty_count = 0
                if graph[row][col] != 0:
                    continue
                for move in moves:
                    n_row, n_col = row + move[0], col + move[1]
                    if graph[n_row][n_col] == -1:
                        continue
                    else:
                        if graph[n_row][n_col] in favorite[student]:
                            favorite_count += 1
                        if graph[n_row][n_col] == 0:
                            empty_count += 1

                heapq.heappush(queue, [-favorite_count, -empty_count, row, col])

        favorite_count, empty_count, r, c = heapq.heappop(queue)
        graph[r][c] = student

    return calc_sum(graph)


# 입력 및 실행
N = int(input())

graph = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
for r in range(1, N + 1):
    for c in range(1, N + 1):
        graph[r][c] = 0

favorite = dict()
students = []
for _ in range(N * N):
    nums = list(map(int, input().split()))
    students.append(nums[0])
    favorite[nums[0]] = set(nums[1:])

print(solution())
