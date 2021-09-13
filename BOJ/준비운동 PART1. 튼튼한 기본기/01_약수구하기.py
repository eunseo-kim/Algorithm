# 언어 : Python
# 날짜 : 2021.07.12
# 문제 : BOJ > 약수구하기
# 티어 : 브론즈 3
# =====================================================
# 소요 시간 : 10'
# 제출 시도 : 3
# 오답 이유 : # range(1, N)으로 해서 틀렸다.
# =====================================================


def solution(N, K):
    count = 0
    for i in range(1, N + 1):
        if N % i == 0:
            count += 1
            if count == K:
                return i
    return 0


N, K = map(int, input().split())
print(solution(N, K))