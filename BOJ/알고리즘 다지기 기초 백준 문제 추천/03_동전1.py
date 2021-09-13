# 언어 : Python
# 날짜 : 2021.07.23
# 문제 : BOJ > 동전 1 (https://www.acmicpc.net/problem/2293)
# 티어 : 실버 1
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : dp
# ============================================================================
def solution():
    dp = [0 for _ in range(k + 1)]
    # `n - coin == 0`인 경우는 `num == coin`인 경우.
    # 따라서 dp[0]에는 num == coin 일때 1을 추가할 수 있도록 1을 디폴트로 넣어둔다.
    dp[0] = 1

    for coin in coins:
        for n in range(coin, k + 1):  # 만들고자 하는 수가 현재 coin보다 크거나 같을 때만
            dp[n] += dp[n - coin]  # dp로 n을 만들 수 있는 경우의 수를 누적

    return dp[-1]


n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))
answer = solution()
print(answer)