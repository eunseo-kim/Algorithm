# 언어 : Python
# 날짜 : 2021.08.30
# 문제 : BOJ > LCS (https://www.acmicpc.net/problem/11053)
# 티어 : 실버 2
# 분류 : dp
# 풀이 : dp[i] = [현재 i보다 작은 수까지의 최대 부분 수열] + i번째 수
# ===========================================================================


def solution():
    dp = [0 for i in range(N)]
    for i in range(N):
        for j in range(i):
            if a[i] > a[j]:
                dp[i] = max(dp[i], dp[j])

        dp[i] += 1

    print(max(dp))


N = int(input())
a = list(map(int, input().split()))
solution()