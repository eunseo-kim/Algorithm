# 언어 : Python
# 날짜 : 2022.3.14
# 문제 : BOJ > 거스름돈 (https://www.acmicpc.net/problem/14916)
# 티어 : 실버 5
# ============================================================================


def solution():
    # 예외처리
    if n < 5:
        if n % 2 == 0:
            return n // 2
        else:
            return -1

    cnt, N = divmod(n, 5)
    if N == 0:
        return cnt
    if N % 2 == 0:
        return cnt + N // 2
    else:
        return cnt + (N + 5) // 2 - 1


n = int(input())
print(solution())