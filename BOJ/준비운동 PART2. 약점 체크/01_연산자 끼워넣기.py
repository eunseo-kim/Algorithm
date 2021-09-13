# 언어 : Python
# 날짜 : 2021.07.14
# 문제 : BOJ > 연산자 끼워넣기 (https://www.acmicpc.net/problem/14888)
# 티어 : 실버 1
# =====================================================
# 소요 시간 : 30-40'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================

from itertools import permutations


def get_operators(add, sub, mul, div):
    return "+" * add + "-" * sub + "*" * mul + "/" * div


def calculate(n1, op, n2):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    else:
        if (n1 < 0 and n2 > 0) or (n1 > 0 and n2 < 0):
            return (-1) * (abs(n1) // abs(n2))
        else:
            return n1 // n2


def recursion(nums, op, idx1, op_idx, idx2):
    if idx1 == 0:
        return calculate(nums[idx1], op[op_idx], nums[idx2])
    else:
        n1 = recursion(nums, op, idx1 - 1, op_idx - 1, idx2 - 1)
        return calculate(n1, op[op_idx], nums[idx2])


def solution():
    N = int(input())
    nums = list(map(int, input().split()))
    add, sub, mul, div = map(int, input().split())
    operator = get_operators(add, sub, mul, div)
    op_len = len(operator)
    op_list = set(permutations(operator))
    max, min = float("-inf"), float("inf")
    for op in op_list:
        result = recursion(nums, op, N - 2, N - 2, N - 1)
        if result > max:
            max = result
        if result < min:
            min = result
    print(max)
    print(min)


solution()