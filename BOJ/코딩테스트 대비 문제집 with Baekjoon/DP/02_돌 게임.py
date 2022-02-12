# 언어 : Python
# 날짜 : 2022.2.12
# 문제 : BOJ > 돌 게임 (https://www.acmicpc.net/problem/9655)
# 티어 : 실버 5
# =========================================================================

# f(n) = f(n-1) + f(n-3)

N = int(input())
if N % 2 == 0:
    print("CY")
else:
    print("SK")