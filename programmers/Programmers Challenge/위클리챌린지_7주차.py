from collections import defaultdict


def solution(enter, leave):
    result = defaultdict(set)
    for l in leave:
        i = enter.index(l)
        meet = enter[: i + 1]
        for p in meet:
            result[p].update(set(meet))
        enter.pop(i)

    answer = []
    for key in sorted(result.keys()):
        answer.append(len(result[key]) - 1)
    return answer


enter = [1, 4, 2, 3]
leave = [2, 1, 4, 3]
result = solution(enter, leave)
print(result)