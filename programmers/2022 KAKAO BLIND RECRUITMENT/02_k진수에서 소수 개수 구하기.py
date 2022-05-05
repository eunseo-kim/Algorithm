import math


def change_decimal(number, k):
    stack = ""
    while number > 1:
        stack += str(number % k)
        number = number // k
    stack += str(number)

    return stack[::-1]


def is_prime(number):
    if number <= 1:
        return False

    for n in range(2, int(math.sqrt(number) + 1)):
        if number % n == 0:
            return False
    return True


def solution(n, k):
    changed_number = str(int(change_decimal(n, k)))

    number_list = changed_number.split("0")

    answer = 0
    for number in number_list:
        if number != "" and is_prime(int(number)):
            answer += 1

    return answer


result = solution(437674, 3)
print(result)