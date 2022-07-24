# 언어 : Python
# 날짜 : 2022.7.23
# 문제 : BOJ > 부분 문자열 (https://www.acmicpc.net/problem/16916)
# 티어 : 실버 1
# ================================================================

TRUE = 1
FALSE = 0


def make_table():
    table = [0 for _ in range(N)]

    j = 0
    for i in range(1, N):
        while j > 0 and S[i] != S[j]:
            j = table[j - 1]

        if S[i] == S[j]:
            j += 1
            table[i] = j

    return table


def KMP(S, P):
    table = make_table()

    j = 0
    for i in range(N):
        while j > 0 and S[i] != P[j]:
            j = table[j - 1]

        if S[i] == P[j]:
            j += 1
            if j == len(P):
                return TRUE

    return FALSE


S = input()
P = input()
N = len(S)

result = KMP(S, P)
print(result)