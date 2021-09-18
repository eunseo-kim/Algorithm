# 언어 : Python
# 날짜 : 2021.09.18
# 문제 : KOREATECH JUDGE > 삼각형 그리기 (1143)
# ==============================================================
import math


def solution():
    x1, y1, x2, y2, x3, y3 = map(int, input().split())

    if is_same_point(x1, y1, x2, y2, x3, y3):
        return False

    if is_inline(x1, y1, x2, y2, x3, y3):
        return False

    return True


def is_same_point(x1, y1, x2, y2, x3, y3):
    if x1 == x2 and y1 == y2:
        return True
    if x1 == x3 and y1 == y3:
        return True
    if x2 == x3 and y2 == y3:
        return True
    return False


def is_inline(x1, y1, x2, y2, x3, y3):
    if x1 - x2 == 0:
        s1 = float("inf")
    else:
        s1 = (y1 - y2) / (x1 - x2)

    if x1 - x3 == 0:
        s2 = float("inf")
    else:
        s2 = (y1 - y3) / (x1 - x3)

    if x2 - x3 == 0:
        s3 = float("inf")
    else:
        s3 = (y2 - y3) / (x2 - x3)

    if s1 == s2 == s3:
        return True

    return False


def get_length(x1, y1, x2, y2):  # 두 점 사이의 거리
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2))


for _ in range(int(input())):
    print("Yes") if solution() else print("No")

# x1, x2, x3, y1, y2, y3 = 0, -1, 2, 0, -2, 4
# print(is_inline(x1, y1, x2, y2, x3, y3))