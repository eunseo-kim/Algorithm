# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 소수 찾기
# 티어 : 실버 4
# =====================================================
# 소요 시간 : 5'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================
import math


def is_prime(num):  # True이면 1, False이면 0 리턴
    if num == 1:
        return 0

    for n in range(2, int(math.sqrt(num) + 1)):
        if num % n == 0:
            return 0
    return 1


N = int(input())
nums = list(map(int, input().split()))
result = 0
for num in nums:
    result += is_prime(num)
print(result)