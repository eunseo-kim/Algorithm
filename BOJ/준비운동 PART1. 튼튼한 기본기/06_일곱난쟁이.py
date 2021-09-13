# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 일곱 난쟁이
# 티어 : 브론즈 2
# =====================================================
# 소요 시간 : 8'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


def solution(nums):
    find = sum(nums) - 100
    for idx, num in enumerate(nums):
        if find - num in nums[idx + 1 :]:
            nums.remove(num)
            nums.remove(find - num)
            break

    for num in sorted(nums):
        print(num)


nums = []
for i in range(9):
    nums.append(int(input()))
solution(nums)