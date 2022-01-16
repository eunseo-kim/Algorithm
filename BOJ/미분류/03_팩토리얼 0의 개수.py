# 언어 : Python
# 날짜 : 2022.1.16
# 문제 : BOJ > 팩토리얼 0의 개수 (https://www.acmicpc.net/problem/1676)
# 티어 : 실버 4
# - 잔디 채우기용 쉬운 문제..^_^;;
# - 근데 '처음으로 0이 아닌 숫자가 나올 때'를 제대로 못봐서 생각보다(?) 오래 걸림
# ===============================================================================


def solution(num):
    result = 1
    while num != 1:
        result *= num
        num -= 1

    return result


number = int(input())

if number == 0:
    print(0)
else:
    factorial = solution(number)

    count = 0
    for char in str(factorial)[::-1]:
        if char != "0":
            break
        count += 1

    print(count)
