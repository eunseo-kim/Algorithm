# 언어 : Python
# 날짜 : 2022.2.21
# 문제 : BOJ > A와 B 2 (https://www.acmicpc.net/problem/12919)
# 티어 : 골드 5
# =========================================================================


def solution():
    queue = [T]
    while queue:
        string = queue.pop(0)
        if string == []:
            break

        if string == S:
            return 1

        if string[-1] == "A":
            queue.append(string[:-1])
        if string[0] == "B":
            new_string = string[::-1]
            queue.append(new_string[:-1])

    return 0


S = list(input())
T = list(input())
result = solution()
print(result)
