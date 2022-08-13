# 언어 : Python
# 날짜 : 2022.8.13
# 문제 : BOJ > 생태학 (https://www.acmicpc.net/problem/4358)
# 티어 : 실버 2
# 트라이로 풀어보자.
# =========================================================================

import sys


class Node:
    def __init__(self, letter=''):
        self.letter = letter
        self.word = None
        self.count = 0
        self.children = {}


class Trie:
    def __init__(self):
        self.count = 0
        self.head = Node()

    def insert(self, name):
        self.count += 1
        curr = self.head

        for char in list(name):
            if char not in curr.children:
                curr.children[char] = Node(char)
            curr = curr.children[char]

        curr.count += 1
        curr.word = name

    def search(self, name):
        curr = self.head
        for char in list(name):
            if char not in curr.children:
                return False
            curr = curr.children[char]

        print(f"{curr.word} {curr.count/self.count*100:.4f}")


data = sys.stdin.read()
trees = data.split("\n")
trees.pop()  # split("\n")에서 마지막 빈 문자열 추가되는 것 제외

trie = Trie()
for tree in trees:
    trie.insert(tree)

for tree in sorted(list(set(trees))):
    trie.search(tree)