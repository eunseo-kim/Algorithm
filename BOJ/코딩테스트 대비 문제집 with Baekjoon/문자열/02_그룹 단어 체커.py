# 언어 : Python
# 날짜 : 2022.2.10
# 문제 : BOJ > 그룹 단어 체커 (https://www.acmicpc.net/problem/1316)
# 티어 : 실버 5
# =========================================================================


def is_group(word):
    words = set()
    length = len(word)
    if length <= 2:
        return 1

    for i in range(length - 1):
        if word[i] != word[i + 1]:
            if word[i] in words or word[i + 1] in words:
                return 0
            words.add(word[i])

    return 1


answer = 0
for _ in range(int(input())):
    answer += is_group(input())
print(answer)