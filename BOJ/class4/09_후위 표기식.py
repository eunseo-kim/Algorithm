# 언어 : Python
# 날짜 : 2021.09.06
# 문제 : BOJ > 후위 표기식 (https://www.acmicpc.net/problem/1918)
# 티어 : 골드 3
# ===========================================================================


def solution():
    infix = list(input())
    stack = []
    answer = []
    priority = {")": 3, "*": 2, "/": 2, "+": 1, "-": 1, "(": 0}  # */의 우선순위 > +-의 우선순위

    for t in infix:
        if t.isalpha():
            answer.append(t)
        elif t == "(":
            stack.append(t)
        elif t == ")":
            while stack and stack[-1] != "(":
                answer.append(stack.pop())
            stack.pop()
        else:
            while stack and priority[stack[-1]] >= priority[t]:
                answer.append(stack.pop())
            stack.append(t)

    while stack:
        answer.append(stack.pop())

    return "".join(answer)


print(solution())