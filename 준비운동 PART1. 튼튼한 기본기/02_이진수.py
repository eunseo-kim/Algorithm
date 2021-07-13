# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 이진수
# 티어 : 브론즈 3
# =====================================================
# 소요 시간 : 15'
# 제출 시도 : 5
# 오답 이유 : 최하위 비트의 위치가 0이라고 알려줬는데
# 반대로 풀어서 for문을 거꾸로 돌았다.🤣
# =====================================================


def solution(N):
    answer = ""
    binary = bin(N)[2:]
    for idx, bit in enumerate(binary[::-1]):
        if bit == "1":
            print(idx, end=" ")


for i in range(int(input())):
    N = int(input())
    solution(N)