# 언어 : Python
# 날짜 : 2022.2.2
# 문제 : BOJ > 배열 합치기 (https://www.acmicpc.net/problem/11728)
# 티어 : 실버 5
# 시간 : 8분
# 시간복잡도 / 1.5초
# 1 ≤ N, M ≤ 1,000,000
# O(N + M)이므로 투포인터로 풀면 ok
# ============================================================================


def solution():
    a, b = 0, 0
    result = []
    while a < N and b < M:
        if A[a] < B[b]:
            result.append(A[a])
            a += 1
        else:
            result.append(B[b])
            b += 1

    return result + A[a:] + B[b:]


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(" ".join(map(str, solution())))