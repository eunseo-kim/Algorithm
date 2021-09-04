# 언어 : Python
# 날짜 : 2021.09.05
# 문제 : BOJ > 최단경로 (https://www.acmicpc.net/problem/1932)
# 티어 : 실버 1
# ===========================================================================
# 새롭게 알게된 점!
# nums.append(inputs)
# dp.append(inputs)
# 를 했더니 nums와 dp가 같은 리스트로 계산이 되었다. (nums == dp 출력하면 true가 됨)
# 따라서 inputs를 전달할 때 [:]를 통해 값을 복사하여 전달하였다.
# ===========================================================================


def solution():
    global dp

    for i in range(N - 1):
        for j, num in enumerate(nums[i]):
            dp[i + 1][j] = max(dp[i][j] + nums[i + 1][j], dp[i + 1][j])
            dp[i + 1][j + 1] = max(dp[i][j] + nums[i + 1][j + 1], dp[i + 1][j + 1])

    print(max(dp[N - 1]))


N = int(input())
nums = []
dp = []
for i in range(N):
    inputs = list(map(int, input().split()))
    nums.append(inputs[:])
    dp.append(inputs[:])

solution()
