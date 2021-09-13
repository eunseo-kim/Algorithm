# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 최소, 최대
# 티어 : 브론즈 3
# =====================================================
# 소요 시간 : 5'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


def solution(N, nums):
    max, min = float("-inf"), float("inf")
    for i in range(N):
        if nums[i] < min:
            min = nums[i]
        if nums[i] > max:
            max = nums[i]
    print(min, max)

    # print(min(nums), max(nums)) → 사실 이게 조금 더 빠르다.


N = int(input())
nums = list(map(int, input().split()))
solution(N, nums)