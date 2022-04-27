# 우선순위를 재정의한다
# 음수라면 절댓값
# 가장 큰 숫자의 참가자가 우승
# 연산자 개수가 N(3 <= N <= 100)이면 N! 가지 경우
#

import re

operators_in_priority = [
    ["+", "-", "*"],
    ["+", "*", "-"],
    ["*", "+", "-"],
    ["*", "-", "+"],
    ["-", "+", "*"],
    ["-", "*", "+"],
]


def calculate(expression, priority):
    stack = expression[:]
    buffer = []

    for p in priority:
        while stack:
            e = stack.pop(0)

            if e.isdigit():
                buffer.append(e)
            else:
                if e == p:
                    n1 = buffer.pop()
                    n2 = stack.pop(0)
                    n3 = eval(n1 + p + n2)
                    buffer.append(str(n3))
                else:
                    buffer.append(e)
        stack = buffer[:]
        buffer = []

    return abs(int(stack.pop()))


def seperate_expression(expression):
    numbers = re.split("[+*-]", expression)
    operators = re.findall("[+*-]", expression)

    exp = []
    for i in range(len(operators)):
        exp.append(numbers[i])
        exp.append(operators[i])
    exp.append(numbers[-1])

    return exp


def solution(expression):
    answer = 0

    exp = seperate_expression(expression)

    for priority in operators_in_priority:
        result = calculate(exp, priority)
        answer = max(answer, result)

    return answer


expression = "3-10*30"
result = solution(expression)
print(result)