# 언어 : Python
# 날짜 : 2021.09.21
# 문제 : KOREATECH JUDGE > 쉬운 수학, 어려운 프로그래밍 (2020년도 F번 문제)
# 풀이 : 이분 탐색으로 풀어야지 풀리는 문제..
# ========================================================================

import math
import sys


def solution():
    available = []
    num = 1

    low, high = 0, math.pow(2, 32) - 1
    while low <= high:
        mid = (low + high) // 2
        n1 = mid // 3
        n2 = (mid // K) * 3

        np = n1 + n2
        if np == P:
            available.append(mid)
            high -= 1
        elif np < P:
            low = mid + 1
        else:
            high = mid - 1

    if not available:
        return -1
    return int(sorted(available)[0])


for _ in range(int(input())):
    P, K = map(int, input().split())
    print(solution())
