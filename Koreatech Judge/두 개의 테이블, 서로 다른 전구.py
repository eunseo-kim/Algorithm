# 언어 : Python
# 날짜 : 2021.09.17
# 문제 : KOREATECH JUDGE > 두 개의 테이블, 서로 다른 전구(1144번)
# 소요시간: 5' 38"
# ==============================================================


def solution():
    a, b = map(int, input().split())
    b1, b2 = bin(a)[2:], bin(b)[2:]
    l1, l2 = len(b1), len(b2)
    if l1 > l2:
        length = l1
        b2 = b2.zfill(length)
    else:
        length = l2
        b1 = b1.zfill(length)

    cnt = 0
    for i in range(length):
        if b1[i] != b2[i]:
            cnt += 1

    return cnt


for _ in range(int(input())):
    print(solution())