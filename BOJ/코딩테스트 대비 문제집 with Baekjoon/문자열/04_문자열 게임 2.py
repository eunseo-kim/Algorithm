# 언어 : Python
# 날짜 : 2022.7.23
# 문제 : BOJ > 문자열 게임 2 (https://www.acmicpc.net/problem/20437)
# 티어 : 골드 5
# =========================================================================


from collections import defaultdict


def solution(W, K):
    location = defaultdict(list)
    available = []

    for i, char in enumerate(W):
        location[char].append(i)

        if len(location[char]) == K:
            length = i - location[char][0] + 1
            available.append(length)
            location[char].pop(0)

    available.sort()
    if len(available) == 0:
        return -1
    return " ".join(map(str, [available[0], available[-1]]))


#
for _ in range(int(input())):
    W = input()
    K = int(input())
    result = solution(W, K)
    print(result)