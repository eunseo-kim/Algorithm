# 17'

from collections import defaultdict


def solution(survey, choices):
    # 유형별 점수 계산하기
    choice_score = defaultdict(int)

    for idx, s in enumerate(survey):
        disagree, agree = s[0], s[1]
        choice = choices[idx]

        if choice < 4:  # 비동의
            choice_score[disagree] += 4 - choice
        elif choice > 4:  # 동의
            choice_score[agree] += choice - 4

    # 성격 유형 판단하기
    personality_type = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]

    answer = ""
    for type1, type2 in personality_type:
        if choice_score[type1] >= choice_score[type2]:  # 같으면 사전순으로 type1 선택
            answer += type1
        elif choice_score[type1] < choice_score[type2]:
            answer += type2

    return answer


survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]
result = solution(survey, choices)
print(result)