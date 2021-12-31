# 언어 : Python
# 날짜 : 2021.12.31
# 문제 : BOJ > N과 M(4)(https://www.acmicpc.net/problem/15652)
# 티어 : 실버 3
# =====================================================================
def solution(numbers, number):
    if len(numbers) == M:
        print(" ".join(map(str, numbers)))
        return

    for n in range(number, N + 1):
        solution(numbers + [n], n)


N, M = list(map(int, input().split()))
solution([], 1)
