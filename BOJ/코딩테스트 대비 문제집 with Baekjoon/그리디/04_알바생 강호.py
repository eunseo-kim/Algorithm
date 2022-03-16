# 언어 : Python
# 날짜 : 2022.3.16
# 문제 : BOJ > 알바생 강호 (https://www.acmicpc.net/problem/1758)
# 티어 : 실버 4
# ================================================================


def solution():
    nums.sort(reverse=True)
    result = 0
    for i in range(1, N + 1):
        if nums[i - 1] - i >= 0:
            result += nums[i - 1] - i + 1
    print(result)


N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))
solution()