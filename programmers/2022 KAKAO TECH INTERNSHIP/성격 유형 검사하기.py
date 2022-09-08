# 14"
from collections import defaultdict


def solution(survey, choices):
    score = defaultdict(int)
    TYPES = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    for i, choice in enumerate(choices):
        disagree, agree = survey[i]

        if choice == 4:
            continue

        if choice > 4:  # agree
            score[agree] += choice - 4
        else:  # disagree
            score[disagree] += 4 - choice

    answer = ""
    for type1, type2 in TYPES:
        if score[type1] >= score[type2]:
            answer += type1
        else:
            answer += type2

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = solution(survey, choices)
print(result)