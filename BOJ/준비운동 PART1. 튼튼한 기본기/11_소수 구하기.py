# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 소수 구하기
# 티어 : 실버 5
# =====================================================
# 소요 시간 : 10'
# 제출 시도 : 2
# 오답 이유 : 소수가 존재하지 않는 경우 -1만 출력되게 해야됨
# =====================================================

import math


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

M = int(input())
N = int(input())
sum, min = 0, -1
min_found = False
for num in range(M, N + 1):
    if is_prime(num):
        if not min_found:
            min = num
            min_found = True
        sum += num

if sum > 0:
    print(sum)
print(min)