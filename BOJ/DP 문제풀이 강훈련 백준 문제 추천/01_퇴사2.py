# 언어 : Python
# 날짜 : 2021.08.02
# 문제 : BOJ > 퇴사 2 (https://www.acmicpc.net/problem/15486)
# 티어 : 실버 1
# ======================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : -
# ======================================================================
def solution():
    dp = [0 for _ in range(N + 2)]

    for start in range(1, N + 1):
        end = reservations[start][0]
        cost = reservations[start][1]
        if end <= N + 1:
            dp[end] = max(dp[start] + cost, dp[end])

        dp[start + 1] = max(dp[start], dp[start + 1])

    print(dp[-1])


N = int(input())
reservations = [None]  # idx는 1부터 시작
for start in range(1, N + 1):
    days, cost = map(int, input().split())
    end = start + days
    reservations.append([end, cost])  # 상담 끝나는 일, 비용

solution()