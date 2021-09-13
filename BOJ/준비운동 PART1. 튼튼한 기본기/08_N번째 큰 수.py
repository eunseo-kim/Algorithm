# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > N번째 큰 수
# 티어 : 실버 5
# =====================================================
# 소요 시간 : 3'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


# def solution(nums):
#     print(sorted(nums)[-3])

# sorted 안쓰고 풀기
def solution(nums):
    count = 0  # 몇 번 졌는지
    for i in range(10):
        count = 0
        for j in range(10):
            if nums[i] < nums[j]:
                count += 1
        if count == 2:
            print(nums[i])
            break


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    solution(nums)