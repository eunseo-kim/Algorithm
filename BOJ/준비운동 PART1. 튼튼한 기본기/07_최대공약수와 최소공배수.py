# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 최대공약수와 최소공배수
# 티어 : 실버 5
# =====================================================
# 소요 시간 : 5'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


def solution(a, b):
    cal = a * b
    while b != 0:
        r = a % b
        a = b
        b = r

    print(a, int(cal / a))


a, b = map(int, input().split())
solution(a, b)