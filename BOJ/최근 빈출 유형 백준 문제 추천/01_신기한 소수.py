# 언어 : Python
# 날짜 : 2022.1.8
# 문제 : BOJ > 신기한 소수(https://www.acmicpc.net/problem/2023)
# 티어 : 골드 5
# =====================================================================

import math
import heapq


def is_prime(number):
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            return False
    return True


def solution():
    result = []
    queue = [2, 3, 5, 7]

    while queue:
        num = heapq.heappop(queue)

        if len(str(num)) == N:
            result.append(num)

        if len(str(num)) > N:
            break

        if is_prime(num):
            for n in range(1, 10):
                new_num = num * 10 + n
                if is_prime(new_num):
                    heapq.heappush(queue, new_num)

    return result


N = int(input())
answer = solution()

for n in answer:
    print(n)