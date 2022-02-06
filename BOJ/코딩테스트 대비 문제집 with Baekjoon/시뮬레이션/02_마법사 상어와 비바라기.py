# 언어 : Python
# 날짜 : 2022.2.6
# 문제 : BOJ > 마법사 상어와 비바라기 (https://www.acmicpc.net/problem/21610)
# 티어 : 골드 5
# 시간 초과 해결 방법
# => list in ... 대신 visited로 방문 여부를 체크하도록 수정했다.
# ===============================================================

from collections import deque


def solution():
    clouds = deque([[N, 1], [N, 2], [N - 1, 1], [N - 1, 2]])
    for dir, space in moves:
        visited = [[False for _ in range(N + 2)] for _ in range(N + 2)]

        # 구름의 이동 후 위치 구하기
        direction = dir_dict[dir]
        move = [direction[0] * space, direction[1] * space]
        new_clouds = deque()
        while clouds:
            cloud = clouds.popleft()
            cloud_x = (cloud[0] + move[0] + N) % N
            cloud_y = (cloud[1] + move[1] + N) % N

            if cloud_x == 0:
                cloud_x = N
            if cloud_y == 0:
                cloud_y = N

            # 구름에 비가 1씩 내린다
            basket[cloud_x][cloud_y] += 1
            new_clouds.append([cloud_x, cloud_y])
            visited[cloud_x][cloud_y] = True

        # 물 복사 마법
        add_water = deque()
        for cloud in new_clouds:
            water = 0
            for diagonal in diagonals:
                diag_x = cloud[0] + diagonal[0]
                diag_y = cloud[1] + diagonal[1]
                if basket[diag_x][diag_y] != 0:
                    water += 1
            add_water.append([cloud[0], cloud[1], water])

        for x, y, water in add_water:
            basket[x][y] += water

        # 물의 양 2씩 줄어들고 새로운 구름(구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.)
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if basket[i][j] >= 2 and not visited[i][j]:
                    clouds.append([i, j])
                    basket[i][j] -= 2


# 입력 및 실행
N, M = map(int, input().split())
basket = [[0 for _ in range(N + 2)] for _ in range(N + 2)]
for i in range(1, N + 1):
    nums = list(map(int, input().split()))
    for j, num in enumerate(nums, 1):
        basket[i][j] = num

moves = []
for _ in range(M):
    a, b = map(int, input().split())
    moves.append([a, b])

dir_dict = {1: (0, -1), 2: (-1, -1), 3: (-1, 0), 4: (-1, 1), 5: (0, 1), 6: (1, 1), 7: (1, 0), 8: (1, -1)}
diagonals = [[-1, -1], [1, -1], [1, 1], [-1, 1]]

result = solution()
answer = 0
for i in range(1, N + 1):
    answer += sum(basket[i])

print(answer)