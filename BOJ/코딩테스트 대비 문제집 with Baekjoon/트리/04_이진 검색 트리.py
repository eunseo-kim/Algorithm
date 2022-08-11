# 언어 : Python
# 날짜 : 2022.8.11
# 문제 : BOJ > 이진 검색 트리 (https://www.acmicpc.net/problem/5639)
# 티어 : 골드 5
# =========================================================================

# 후위 순위 => left > root > right 순서대로...

import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def add_node(root, node):
    curr = root

    while True:
        if curr.value > node.value:
            if not curr.left:
                curr.left = node
                return
            curr = curr.left
        else:
            if not curr.right:
                curr.right = node
                return
            curr = curr.right


def post_order(node):
    if node.left:
        post_order(node.left)
    if node.right:
        post_order(node.right)

    print(node.value)


def solution(numbers):
    root = Node(numbers[0])

    for number in numbers[1:]:
        node = Node(number)
        add_node(root, node)

    post_order(root)


numbers = []
while True:
    try:
        numbers.append(int(input()))
    except:
        break

solution(numbers)


# 50
# 30
# 24
# 5
# 28
# 45
# 98
# 52
# 60