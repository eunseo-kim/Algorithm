# 언어 : Python
# 날짜 : 2022.3.16
# 문제 : BOJ > 주유소 (https://www.acmicpc.net/problem/13305)
# 티어 : 실버 4
# ============================================================================


def solution():
    total_cost = 0
    cost = float("inf")
    for idx, dist in enumerate(distances):
        if costs[idx] < cost:
            cost = costs[idx]
        total_cost += cost * dist

    print(total_cost)


N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))
solution()