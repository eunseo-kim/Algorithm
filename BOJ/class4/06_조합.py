# 언어 : Python
# 날짜 : 2021.09.01
# 문제 : BOJ > 조합 (https://www.acmicpc.net/problem/2407)
# 티어 : 실버 2
# ===========================================================================


def calculate(num, turn):
    n = num
    while turn > 1:
        num *= n - 1
        n -= 1
        turn -= 1
    return num


def solution():
    c1 = calculate(n, m)
    c2 = calculate(m, m)
    print(c1 // c2)


n, m = map(int, input().split())
solution()
