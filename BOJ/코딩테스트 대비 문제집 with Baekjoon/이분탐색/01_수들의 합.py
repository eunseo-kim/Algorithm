# 언어 : Python
# 날짜 : 2022.2.28
# 문제 : BOJ > 수들의 합 (https://www.acmicpc.net/problem/1789)
# 티어 : 실버 5
# 풀이 : 서로 다른 N개의 자연수의 합이 S라고 한다. S를 알 때, 자연수 N의 최댓값은 얼마일까?
# 1부터 N까지의 합 = (N * (N+1)) / 2
# (N * (N+1)) / 2 <= S 가 되는 N의 최댓값
# =========================================================================


def solution():
    left, right = 1, S
    answer = 0
    while left <= right:
        mid = (left + right) // 2
        sum = (mid * (mid + 1)) // 2
        if sum <= S:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)


S = int(input())
solution()
