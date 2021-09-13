import math
import re


def solution(n, k):
    if k != 10:
        n = change_number(n, k)
    else:
        n = str(n)

    num_list = re.split(r"0+", n)
    if num_list[-1] == "":
        num_list = num_list[:-1]

    num_list = list(map(int, num_list))
    l = len(num_list)
    answer = 0

    if l == 1:
        if is_prime(num_list[0]):
            answer = 1
    else:
        for i in range(l):
            if not is_prime(num_list[i]):
                num_list[i] = -1

        if num_list[0] != -1:
            answer += 1
        if num_list[-1] != -1:
            answer += 1
        for i in range(1, l - 1):
            if num_list[i] != -1:
                answer += 1
    return answer


def change_number(n, k):  # n을 k진수로 변환
    base = ""
    while n > 0:
        n, mod = divmod(n, k)
        base += str(mod)

    return base[::-1]


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


n = 1000000
k = 3
print(solution(1000000, 4))
# n = str(n)
# print

# print(list(map(int, re.split(r"0+", "3310021000"))))
# print(solution(437674, 3))
# print(solution(110011, 10))

# for i in range(3, 11):
#     print("i:", i)
#     print(solution(1, i))

# for i in range(3, 11):
#     print("nnn:", i)
#     print(solution(1000000, i))


# print(solution(1000000, 4))

# 1' 26"