def get_expression(exp_list, operators):
    expression = []
    number = ""
    for element in exp_list:
        if element in operators:
            expression.append(int(number))
            expression.append(element)
            number = ""
        else:
            number += element
    expression.append(int(number))
    return expression


def get_operators_priority(operators):
    def dfs(path):
        if len(path) == 3:
            cases.append(path)
            return

        for op in operators:
            if op not in path:
                dfs(path + [op])

    cases = []
    dfs([])
    return cases


def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2

    if op == "-":
        return num1 - num2

    if op == "*":
        return num1 * num2


def solution(expression):
    operators = ["*", "-", "+"]
    expression = get_expression(list(expression), operators)
    priority_cases = get_operators_priority(operators)

    answer = 0
    for case in priority_cases:
        stack = expression.copy()
        for op in case:
            next_stack = []
            while stack:
                element = stack.pop(0)
                if element != op:
                    next_stack.append(element)
                else:
                    num1 = next_stack.pop()
                    num2 = stack.pop(0)
                    next_stack.append(calculate(num1, op, num2))
            stack = next_stack
        answer = max(answer, abs(stack[0]))

    return answer


expression = "100-200*300-500+20"
result = solution(expression)
print(result)