# 언어 : Python
# 날짜 : 2022.8.12
# 문제 : BOJ > 단절점과 단절선 (https://www.acmicpc.net/problem/14675)
# 티어 : 골드 5
# =========================================================================

# 단절점 / 리프노드를 제외한 어떠한 단절점 삭제 시 트리가 2개 이상으로 쪼개집니다.
# 단절선 / 어떠한 단절선 삭제 시 트리가 '2개'로 쪼개집니다.
# 이해가 안된다면 아래 트리를 예시로 실험해보기.
#
#             1
#           /\  \
#          2 10  3
#         /\     /\
#        4  5   6  7
#       /      /    \
#      8      11     9
#


from collections import defaultdict

import sys

input = sys.stdin.readline


N = int(input())  # 최소 2개의 노드
edges = defaultdict(list)
inputs = []
for _ in range(N - 1):
    a, b = map(int, input().split(" "))
    edges[a].append(b)
    edges[b].append(a)
    inputs.append([a, b])

for _ in range(int(input())):
    t, q = map(int, input().split(" "))
    if t == 1:
        if len(edges[q]) <= 1:
            print("no")
        else:
            print("yes")
    else:
        print("yes")
