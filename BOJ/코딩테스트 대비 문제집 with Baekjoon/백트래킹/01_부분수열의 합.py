# 언어 : Python
# 날짜 : 2022.2.25
# 문제 : BOJ > 부분수열의 합 (https://www.acmicpc.net/problem/17626)
# 티어 : 실버 2
# =========================================================================


def dfs(i, sum, path):
    global answer

    if i >= N:
        return

    if sum == M:
        answer += 1

    for idx in range(i + 1, N):
        dfs(idx, sum + nums[idx], path + [nums[idx]])


N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0
for index in range(N):
    dfs(index, nums[index], [nums[index]])
print(answer)
