from collections import defaultdict
import sys

input = sys.stdin.readline

N = int(input())
s_dict = defaultdict(list)
students = list(map(int, input().split()))
for idx, s in enumerate(students):
    s_dict[s].append(idx + 1)

M = int(input())
check = list(map(int, input().split()))
for ch in check:
    if s_dict[ch] != []:
        print(" ".join(map(str, s_dict[ch])))
    else:
        print(-1)
