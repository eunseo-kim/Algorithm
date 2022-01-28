# 언어 : Python
# 날짜 : 2022.1.28
# 문제 : BOJ > 인구 이동 (https://www.acmicpc.net/problem/16234)
# 티어 : 골드 5
# 시간 : 1시간 30분 (+ 못 풂)
# ① HOW
# ② NEW
# ✔시간복잡도
# N <= 50 / L <= R <= 100
# ============================================================================

# 하루 동안 일어나는 일 -------------------------
# 인구수 A[r][c]
# L <= 인구 차이 <= R 이면 국경선 열림
# 국경선이 열려서 국경이 연결된 한 묶음 = 연합
# 각 칸의 인구수는 N빵
#  ----------------------------------------------
# 다시 반복 모든 국경선이 다 닫힐때까지 하루 반복


import math

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def find_union(people):
    union = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            union[r][c] = 0

    cnt = 1
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            if union[r][c] == 0:
                union[r][c] = cnt
                cnt += 1

            for move in moves:
                new_r, new_c = r + move[0], c + move[1]
                if people[new_r][new_c] == -1:
                    continue

                if L <= abs(people[new_r][new_c] - people[r][c]) <= R:
                    union[new_r][new_c] = union[r][c]
                elif union[new_r][new_c] == 0:
                    union[new_r][new_c] = cnt
                    cnt += 1

    union_result = dict()
    for r in range(1, N + 1):
        for c in range(1, N + 1):
            key = union[r][c]
            if key not in union_result:
                union_result[key] = [1, people[r][c]]
            else:
                union_result[key][0] += 1
                union_result[key][1] += people[r][c]

    for key, value in union_result.items():
        union_result[key] = [1, math.floor(value[1] / value[0])]

    for key in union_result.keys():
        for r in range(1, N + 1):
            for c in range(1, N + 1):
                if union[r][c] == key:
                    people[r][c] = union_result[key][1]

    return union_result, people[:]


def solution():
    union, people = find_union(A)
    days = 0
    while len(union.keys()) != N * N:
        union, people = find_union(people[:])
        days += 1
    return days


# 입력 및 실행
N, L, R = map(int, input().split())
A = [[-1 for _ in range(N + 2)] for _ in range(N + 2)]
for r in range(1, N + 1):
    for c, num in enumerate(list(map(int, input().split())), 1):
        A[r][c] = num

print(solution())
