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
    for p in priority:
        for e in expression:
            if e == p:
                idx = expression.index(e)
                n1 = expression[idx-1]
                n2 = expression[idx+1]
                n3 = eval(n1+e+n2)
                
                expression = expression[:idx-1] + [str(n3)] + expression[idx+2:]

    return abs(int(expression.pop()))
    

def solution(expression):
    answer = 0
    ex = re.split(r"(\D)", expression)

    for priority in operators_in_priority:
        result = calculate(ex, priority)
        answer = max(answer, result)

    return answer


expression = "3-10*30"
result = solution(expression)
print(result)