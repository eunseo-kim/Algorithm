# 언어 : Python
# 날짜 : 2022.3.14
# 문제 : BOJ > 로프 (https://www.acmicpc.net/problem/2217)
# 티어 : 실버 4
# ============================================================================


def solution():
    ropes.sort()

    max_weight = -float("inf")
    for idx, rope in enumerate(ropes):
        curr_weight = rope * (N - idx)
        if max_weight < curr_weight:
            max_weight = curr_weight

    print(max_weight)


ropes = []
N = int(input())
for _ in range(N):
    ropes.append(int(input()))
solution()