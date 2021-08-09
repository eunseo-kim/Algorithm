# 언어 : Python
# 날짜 : 2021.08.09
# 문제 : BOJ > 1, 2, 3 더하기 4 (https://www.acmicpc.net/problem/15989)
# 티어 : 실버 1
# ======================================================================
# 소요 시간 : 15분
# 제출 시도 : 1 try
# ======================================================================


def solution(key):
    dp = [0 for _ in range(key + 1)]
    dp[0] = 1

    for num in range(1, 4):
        for k in range(1, key + 1):
            if k - num >= 0:
                if dp[k - num] != 0:
                    dp[k] += dp[k - num]

    print(dp[-1])


n = int(input())
for _ in range(n):
    solution(int(input()))
