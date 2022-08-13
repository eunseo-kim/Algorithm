# 언어 : Python
# 날짜 : 2022.8.13
# 문제 : BOJ > 생태학 (https://www.acmicpc.net/problem/4358)
# 티어 : 실버 2
# =========================================================================

from collections import defaultdict

import sys


def solution(trees):
    tree_dict = defaultdict(int)
    total_count = 0

    for tree in trees:
        tree_dict[tree] += 1
        total_count += 1

    for tree in sorted(tree_dict.keys()):
        print(f"{tree} {tree_dict[tree]/total_count*100:.4f}")


data = sys.stdin.read()
trees = data.split("\n")
trees.pop()  # split("\n")에서 마지막 빈 문자열 추가되는 것 제외
solution(trees)