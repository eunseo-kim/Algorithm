def solution(n, apeach):
    dp = [[] for i in range(11)]
    dp[0] = [[n - (apeach[0] + 1), [apeach[0] + 1]], [n, [0]]]

    for i in range(1, 10):
        for d in dp[i - 1]:
            turn_left, ryan = d
            dp[i].append([turn_left - (apeach[i] + 1), ryan + [apeach[i] + 1]])
            dp[i].append([turn_left, ryan + [0]])

    result = []
    max_subscore = 0

    for d in dp[9]:
        turn_left, ryan = d

        if turn_left >= 0:
            ryan = ryan + [turn_left]
            subscore = get_score(apeach, ryan)

            if subscore > 0:
                if subscore > max_subscore:
                    result = [ryan[::-1]]
                    max_subscore = subscore
                elif subscore == max_subscore:
                    result.append(ryan[::-1])

    if result == []:
        return [-1]

    result = sorted(result, reverse=True)
    return result[0][::-1]


def get_score(apeach, ryan):
    apeach_score = 0
    ryan_score = 0
    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue
        if apeach[i] >= ryan[i]:
            apeach_score += 10 - i
        elif apeach[i] < ryan[i]:
            ryan_score += 10 - i

    return ryan_score - apeach_score


# n = 5
# apeach = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
n = 10
apeach = [0, 0, 0, 0, 0, 0, 0, 0, 3, 4, 3]
# n = 9
# apeach = [0, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1]
print(solution(n, apeach))

# re = [[0, 0, 2, 3, 4, 1, 0, 0, 0, 0, 0], [9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0]]
# result = []
# for r in re:
#     result.append(r[::-1])

# print(result)
# result.sort()
# print(result)

# for r in result:
#     print(r[::-1])

# 4' 55"