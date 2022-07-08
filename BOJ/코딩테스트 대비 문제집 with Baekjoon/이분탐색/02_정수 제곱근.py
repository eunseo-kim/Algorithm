# 언어 : Python
# 날짜 : 2022.7.8
# 문제 : BOJ > 정수 제곱근 (https://www.acmicpc.net/problem/2417)
# 티어 : 실버 4
# =================================================================


def lower_bound(N):
    left, right = 0, N

    while left < right:
        mid = (left + right) // 2

        if mid ** 2 >= N:
            right = mid
        else:
            left = mid + 1

    return left


N = int(input())
if N == 0:
    print(0)
else:
    print(lower_bound(N))