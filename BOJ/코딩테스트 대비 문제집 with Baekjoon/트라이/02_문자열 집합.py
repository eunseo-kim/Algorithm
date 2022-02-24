# 언어 : Python
# 날짜 : 2022.2.24
# 문제 : BOJ > 문자열 집합 (https://www.acmicpc.net/problem/11425)
# 티어 : 실버 3
# 풀이 : Trie 클래스 직접 구현하기!
# (근데 python으로는 시간초과가 뜬다. pypy로만 통과됨)
# =========================================================================


class Node:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.children = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, word):
        curr = self.head
        for letter in list(word):
            if letter not in curr.children.keys():
                curr.children[letter] = Node(letter)
            curr = curr.children[letter]
        curr.data = word

    def search(self, word):
        curr = self.head
        for letter in list(word):
            if letter not in curr.children.keys():
                return False
            curr = curr.children[letter]

        if curr.data == word:
            return True


# 입출력
N, M = map(int, input().split())
trie = Trie()

for _ in range(N):
    trie.insert(input())

cnt = 0
for _ in range(M):
    if trie.search(input()):
        cnt += 1

print(cnt)
