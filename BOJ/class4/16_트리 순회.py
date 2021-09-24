# 언어 : Python
# 날짜 : 2021.09.24
# 문제 : BOJ > 트리 순회 (https://www.acmicpc.net/problem/1991)
# 티어 : 실버 1
# ==========================================================


def preorder(node):
    if node == ".":
        return

    if node not in nodes.keys():
        pre.append(node)
        return

    left, right = nodes[node][0], nodes[node][1]

    pre.append(node)
    preorder(left)
    preorder(right)


def inorder(node):
    if node == ".":
        return

    if node not in nodes.keys():
        ino.append(node)
        return

    left, right = nodes[node][0], nodes[node][1]

    inorder(left)
    ino.append(node)
    inorder(right)


def postorder(node):
    if node == ".":
        return

    if node not in nodes.keys():
        post.append(node)
        return

    left, right = nodes[node][0], nodes[node][1]

    postorder(left)
    postorder(right)
    post.append(node)


N = int(input())
nodes = dict()
for _ in range(N):
    root, left, right = input().split()
    nodes[root] = [left, right]

start = "A"
pre = []
preorder(start)
ino = []
inorder(start)
post = []
postorder(start)

print("".join(map(str, pre)))
print("".join(map(str, ino)))
print("".join(map(str, post)))
