# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 쉽게 푸는 문제
# 티어 : 실버 5
# =====================================================
# 소요 시간 : 20'
# 제출 시도 : 2
# 오답 이유 : 너무 복잡하게 생각했다. N이 1000까지여서 그냥
# 미리 전체 리스트를 만들어놔도 됐었다.
# =====================================================


def solution(A, B):
    num = 1
    num_count = 0
    nums = []
    for i in range(1001):
        num_count += 1
        nums.append(num)

        if num_count == num:
            num += 1
            num_count = 0
    print(sum(nums[A - 1 : B]))


A, B = map(int, input().split())
solution(A, B)