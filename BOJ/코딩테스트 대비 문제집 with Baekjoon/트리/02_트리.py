# 언어 : Python
# 날짜 : 2022.2.21
# 문제 : BOJ > 트리 (https://www.acmicpc.net/problem/1068)
# 티어 : 골드 5
# =========================================================================

from collections import defaultdict


def make_tree():
    tree = defaultdict(list)
    for node in range(-1, N):
        tree[node] = []

    for node, root in enumerate(roots):
        tree[root].append(node)

    return tree


def solution():
    tree = make_tree()

    # 트리 노드 제거
    queue = [delete_node]
    while queue:
        node = queue.pop(0)
        root = roots[node]
        tree[root].remove(node)
        tree[node] = []
        for leaf in tree[node]:
            queue.append(leaf)

    # 예외 처리 / 트리가 없음
    root = -1
    if tree[root] == []:
        return 0

    # leaf 노드 개수 세기
    cnt = 0
    queue = [root]
    while queue:
        node = queue.pop(0)
        if tree[node] == []:
            cnt += 1
        else:
            for child in tree[node]:
                queue.append(child)

    return cnt


N = int(input())  # 노드의 개수
roots = list(map(int, input().split()))
delete_node = int(input())
result = solution()
print(result)