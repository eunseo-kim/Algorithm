# 언어 : Python
# 날짜 : 2022.1.1
# 문제 : BOJ > 치킨 배달(https://www.acmicpc.net/problem/15686)
# 티어 : 골드 5
# =====================================================================
from itertools import combinations

CHICKEN = 2
HOUSE = 1

N, M = map(int, input().split())

city = []
for _ in range(N):
    city.append(list(map(int, input().split())))

chicken_count = 0
chickens = []
for i in range(N):
    for j in range(N):
        if city[i][j] == CHICKEN:
            chickens.append([i, j])
            chicken_count += 1

distances = []
for i in range(N):
    for j in range(N):
        if city[i][j] == HOUSE:
            distance = []
            for loc_x, loc_y in chickens:
                currend_distance = abs(loc_x - i) + abs(loc_y - j)
                distance.append(currend_distance)
            distances.append(distance)


def choose(chickens):
    current_min_distance = 0

    for distance in distances:
        min_distance = float("inf")
        for idx in chickens:
            min_distance = min(min_distance, distance[idx])
        current_min_distance += min_distance

    return current_min_distance


min_result = float("inf")
for selected_numbers in combinations(range(chicken_count), M):
    min_result = min(min_result, choose(selected_numbers))

print(min_result)
