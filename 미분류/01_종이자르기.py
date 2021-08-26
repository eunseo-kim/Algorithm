# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 종이자르기(https://www.acmicpc.net/problem/2628)
# 티어 : 실버 5
# ======================================================================

C, R = map(int, input().split())
T = int(input())
cut = {0: [0, R], 1: [0, C]}
for _ in range(T):
    a, b = map(int, input().split())
    cut[a].append(b)

cut[0].sort()
cut[1].sort()

max_row, max_col = 0, 0

for i in range(1, len(cut[1])):
    max_row = max(max_row, cut[1][i] - cut[1][i - 1])

for i in range(1, len(cut[0])):
    max_col = max(max_col, cut[0][i] - cut[0][i - 1])

print(max_row * max_col)
