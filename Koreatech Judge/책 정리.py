# 언어 : Python
# 날짜 : 2021.09.18
# 문제 : KOREATECH JUDGE > 책 정리(1142번)
# ==============================================================
# ljust(): 왼쪽부터 칸수확보 / string.ljust(칸수, 채울 값)


def solution():
    returned = []
    N = int(input())
    for _ in range(N):
        n1, n2 = list(input().split())
        returned.append([float(n1), n2])

    books = []
    M = int(input())
    for _ in range(M):
        n1, n2 = list(input().split())
        books.append([float(n1), n2])

    result = returned + books
    result = sorted(result)

    for re in result:
        if int(re[0]) == re[0]:
            print(str(int(re[0])) + " " + re[1])
        else:
            print(str(re[0]) + " " + re[1])


for _ in range(int(input())):
    answer = solution()