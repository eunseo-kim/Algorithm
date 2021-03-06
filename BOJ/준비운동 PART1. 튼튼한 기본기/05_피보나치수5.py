# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 피보나치 수5
# 티어 : 브론즈 2
# =====================================================
# 소요 시간 : 5'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


def fibo(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    else:
        return fibo(N - 1) + fibo(N - 2)


N = int(input())
print(fibo(N))