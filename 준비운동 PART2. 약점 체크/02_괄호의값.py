# 언어 : Python
# 날짜 : 2021.07.14
# 문제 : BOJ > 괄호의 값 (https://www.acmicpc.net/problem/2504)
# 티어 : 실버 2
# =========================================================
# 소요 시간 : 60+
# 제출 시도 : 6
# 오답 이유 : 논리 오류, 코드 문법 오류
# if ("(" or ")" or "[" or "]") in stack: ← 이렇게 해서 틀림
# =========================================================


def is_pair(b1, b2):
    if b1 == "(":
        return b2 == ")"
    elif b1 == "[":
        return b2 == "]"


def solution(brackets):
    open_brackets = ["[", "("]
    close_brackets = ["]", ")"]
    stack = [brackets.pop()]
    while brackets:
        element = brackets.pop()
        if element in close_brackets:
            stack.append(element)
        elif element in open_brackets:
            found_pair = False
            num_stack = []
            while stack and not found_pair:
                pop_element = stack.pop()
                if type(pop_element) == int:
                    num_stack.append(pop_element)
                elif is_pair(element, pop_element):
                    found_pair = True
                    # 계산해서 다시 stack에 넣기
                    if num_stack:
                        if len(num_stack) >= 2:
                            new_num = sum(num_stack)
                        else:
                            new_num = num_stack.pop()
                        if element == "(":
                            stack.append(new_num * 2)
                        else:
                            stack.append(new_num * 3)
                    else:  # stack에 숫자가 없는 경우
                        if element == "(":
                            stack.append(2)
                        else:
                            stack.append(3)
                    break
            if not found_pair:
                return 0

    if "]" in stack or "[" in stack or ")" in stack or "(" in stack:
        return 0

    return sum(stack)


brackets = list(input())
print(solution(brackets))
# brackets = list("(()[[]])([])")
