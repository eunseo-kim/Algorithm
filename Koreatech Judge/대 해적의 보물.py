# 언어 : Python
# 날짜 : 2021.09.16
# 문제 : KOREATECH JUDGE > 대 해적의 보물 (https://judge.koreatech.ac.kr/problem.php?id=1141)
# ==========================================================================================
import math


def solution():
    s1, s2 = input().split()
    if len(s2) > len(s1):
        tmp = s1
        s1 = s2
        s2 = tmp

    gcd = GCD(len(s1), len(s2))
    candidates = get_divisor(gcd)

    for c in candidates:
        is_valid = True
        key = s1[:c]
        for i in range(c, len(s1), c):
            if s1[i : c + i] != key:
                is_valid = False
                break
        for i in range(c, len(s2), c):
            if s2[i : c + i] != key:
                is_valid = False
                break

        if is_valid:
            return key

    return ""


def GCD(a, b):  # 최대공약수
    while b != 0:
        n = a % b
        a = b
        b = n
    return a


def get_divisor(n):  # 약수구하기
    divisor = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisor = [i] + divisor

    return divisor


# 입력 및 실행
T = int(input())
for _ in range(T):
    print(solution())