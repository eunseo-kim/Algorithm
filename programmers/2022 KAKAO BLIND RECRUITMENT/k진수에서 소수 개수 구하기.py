import math


def change_to_k(number, k):
    result = []
    while number >= k:
        number, rest = divmod(number, k)
        result.append(rest)
    result.append(number)
    return "".join(map(str, result[::-1]))


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def solution(n, k):
    changed_result = change_to_k(n, k)
    numbers = changed_result.split("0")

    answer = 0
    for number in numbers:
        if len(number) > 0 and is_prime(int(number)):
            answer += 1

    return answer


n = 110011
k = 10
result = solution(n, k)
print(result)