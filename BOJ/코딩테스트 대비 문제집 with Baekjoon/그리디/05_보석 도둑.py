# 언어 : Python
# 날짜 : 2022.8.27
# 문제 : BOJ > 보석 도둑 (https://www.acmicpc.net/problem/1202)
# 티어 : 골드 2
# ================================================================

import sys
import heapq

input = sys.stdin.readline


def solution():
    answer = 0

    candidates = []
    for acceptable in bags:
        while gems and acceptable >= gems[0][0]:
            _, value = heapq.heappop(gems)
            heapq.heappush(candidates, (-1) * value)

        if candidates:
            answer += (-1) * heapq.heappop(candidates)

    return answer


N, K = map(int, input().split(" "))
gems = []  # 보석 무게 작은 순서대로
for _ in range(N):
    weight, value = map(int, input().split(" "))
    heapq.heappush(gems, [weight, value])

bags = []  # 가방 무게 작은 순서대로
for _ in range(K):
    bags.append(int(input()))
bags.sort()

result = solution()
print(result)