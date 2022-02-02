# 언어 : Python
# 날짜 : 2022.2.2
# 문제 : BOJ > 단어 정렬 (https://www.acmicpc.net/problem/1181)
# 티어 : 실버 5
# 시간 : 4분
# 시간복잡도
# 1 ≤ N ≤ 20,000
# set(or dictionary) in => Average: O(1) / Worst: O(N)
# python sort => O(nlogn)
# ============================================================================

words = []
memory = set()
for _ in range(int(input())):
    word = input()
    if word not in memory:
        memory.add(word)
        words.append([len(word), word])

words.sort()
for word in words:
    print(word[1])