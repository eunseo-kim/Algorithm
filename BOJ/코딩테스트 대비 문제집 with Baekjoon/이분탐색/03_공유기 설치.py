# 언어 : Python
# 날짜 : 2022.8.17
# 문제 : BOJ > 공유기 설치 (https://www.acmicpc.net/problem/2110)
# 티어 : 골드 5
# ===============================================================

import sys

input = sys.stdin.readline


def binary_search(N, start, end):
    result = 0

    while start <= end:
        mid = (start + end) // 2
        prev_location = locations[0]
        router_count = 1

        for i in range(1, N):
            if locations[i] - prev_location >= mid:
                router_count += 1
                prev_location = locations[i]

        if router_count >= C:  # gap이 너무 작습니다.
            start = mid + 1  # gap의 범위를 크게 잡아봅니다.
            result = mid
        else:  # gap이 너무 큽니다.
            end = mid - 1  # gap의 범위를 작게 잡아봅니다.

    return result


def solution():
    start = 1  # 최소 인접 거리
    end = locations[-1] - locations[0]  # 최대 인접 거리
    return binary_search(len(locations), start, end)


#
N, C = map(int, input().split(" "))
locations = []
for _ in range(N):
    locations.append(int(input()))
locations.sort()
print(solution())
