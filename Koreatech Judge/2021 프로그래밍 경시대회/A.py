from collections import defaultdict


def solution():
    arr = defaultdict(int)
    N = int(input())
    for _ in range(N):
        s = input()
        for ch in s:
            arr[ch] += 1

    for key in arr.keys():
        if arr[key] % N != 0:
            return "false"
    return "true"


print(solution())