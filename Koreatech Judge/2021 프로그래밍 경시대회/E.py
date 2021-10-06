import math


def find_multiple(base, num):
    cur = 1
    cnt = 0
    while cur <= num:
        cur = int(math.pow(base, cnt + 1))
        cnt += 1

    return cnt - 1


for i in range(int(input())):
    num = int(input())
    two = find_multiple(2, num)
    five = find_multiple(5, num)
    ten = find_multiple(10, num)

    case1 = min(two, five)
    print(max(case1, ten))