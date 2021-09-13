# 언어 : Python
# 날짜 : 2021.08.28
# 문제 : BOJ > RGB 거리 (https://www.acmicpc.net/problem/1149)
# 티어 : 실버 1
# 분류 : dp
# ======================================================================
def solution():
    R, G, B = colors[0]
    dp = [R, G, B]

    for i in range(1, N):
        print("dp:", dp)
        pR, pG, pB = dp
        cR, cG, cB = colors[i]
        nR = cR + min(pG, pB)
        nG = cG + min(pR, pB)
        nB = cB + min(pR, pG)
        dp = [nR, nG, nB]

    print(min(dp))


N = int(input())
colors = []  # [R, G, B]
for _ in range(N):
    colors.append(list(map(int, input().split())))
solution()
