# 언어 : Python
# 날짜 : 2021.08.28
# 문제 : BOJ > 곱셈 (https://www.acmicpc.net/problem/1629)
# 티어 : 실버 1
# 분류 : 분할정복

# A^B를 (log2B)번만에 구할 수 있다.
# 1. b의 값이 짝수인지 홀수인지 파악한다.
# 2. b의 값이 짝수라면 10 ^10 -> (10^5)^2 형태로 바꿔준다.
# 3. b의 값이 홀수라면 10 ^11 -> (10^5)^2 * 10 형태로 바꿔준다

# 틀린이유? - 왜 분할정복을 써도 시간초과가 나올까?
# => 오버플로우도 시간초과로 뜬다고 함.
# => 따라서 너무 큰 수는 계산X
# => 매번 %C를 실행해줌(분배법칙에 의해 같은 결과가 나옴)
# ===========================================================================


def pow(num, exp):
    if exp == 1:
        return num % C

    half = pow(num, exp // 2)
    if exp % 2 == 0:
        return half * half % C
    else:
        return num * half * half % C


def solution():
    answer = pow(A, B)
    print(answer)


A, B, C = map(int, input().split())
solution()
