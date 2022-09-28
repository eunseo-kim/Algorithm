from collections import defaultdict

import sys

input = sys.stdin.readline


def solution(N, arr1, Q, arr2):
    visit_count = defaultdict(list)
    for i, num in enumerate(arr1):
        visit_count[num].append(i + 1)

    for num in arr2:
        if visit_count[num] != []:
            print(" ".join(map(str, visit_count[num])))
        else:
            print(-1)


N = 10
arr1 = list(map(int, "3 4 3 2 5 5 1 2 3 4".split(" ")))
Q = 10
arr2 = list(map(int, "1 2 3 4 5 6 7 8 9 10".split(" ")))
result = solution(N, arr1, Q, arr2)
