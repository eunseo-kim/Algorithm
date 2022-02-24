# 언어 : Python
# 날짜 : 2022.2.24
# 문제 : BOJ > 문자열 집합 (https://www.acmicpc.net/problem/11425)
# 티어 : 실버 3
# 풀이 : defaultdict로 trie 간접적으로 구현해보기
# =========================================================================

from collections import defaultdict


def make_trie():
    trie = defaultdict(set)
    word_dict = defaultdict(set)

    for word in word_set:
        length = len(word)
        for i in range(length - 1):
            trie[word[i]].add(word[i + 1])  # letter, word
        word_dict[word[length - 1]].add(word)

    return trie, word_dict


def solution():
    trie, word_dict = make_trie()
    cnt = 0

    for word in words:
        is_set = True
        length = len(word)
        for i in range(length - 1):
            parent, child = word[i], word[i + 1]
            if child not in trie[parent]:
                is_set = False
                continue
        if is_set and word in word_dict[word[length - 1]]:
            cnt += 1

    print(cnt)


# 입출력
N, M = map(int, input().split())

word_set = []
for _ in range(N):
    word_set.append(input())

words = []
for _ in range(M):
    words.append(input())

solution()