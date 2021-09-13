# 언어 : Python
# 날짜 : 2021.06.24 ~ 25
# 문제 : Programmers > Lv2 > 순위 검색
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 소요 시간 : ∞
# 제출 시도 : Failed
# ================================================
import re
from itertools import combinations
from collections import defaultdict


def add_available_cases(info):
    available_cases = defaultdict(list)
    for i in info:
        info_list = i.split()
        for a in (info_list[0], "-"):
            for b in (info_list[1], "-"):
                for c in (info_list[2], "-"):
                    for d in (info_list[3], "-"):
                        key = str(a + b + c + d)
                        available_cases[key].append(int(info_list[-1]))
    return available_cases


def sort_available_cases(available_cases):
    for key, value in available_cases.items():
        available_cases[key] = sorted(value)
    return available_cases


def parse_query(query):
    query_list = list(re.sub("and ", "", query).split())
    return "".join(query_list[:-1]), int(query_list[-1])


def lower_bound(candidate_list, key):
    result = 0
    start, end = 0, len(candidate_list)
    while start < end:
        mid = (start + end) // 2
        if candidate_list[mid] >= key:
            end = mid
        else:
            start = mid + 1

    return len(candidate_list) - end


def solution(info, queries):
    available_cases = add_available_cases(info)
    sorted_cases = sort_available_cases(available_cases)

    answer = []
    for query in queries:
        query_list, query_num = parse_query(query)
        candidate_list = available_cases[query_list]
        answer.append(lower_bound(candidate_list, query_num))
    return answer


info = [
    "java backend junior pizza 150",
    "python frontend senior chicken 210",
    "python frontend senior chicken 150",
    "cpp backend senior pizza 260",
    "java backend junior chicken 80",
    "python backend senior chicken 50",
]
queries = [
    "java and backend and junior and pizza 100",
    "python and frontend and senior and chicken 200",
    "cpp and - and senior and pizza 250",
    "- and backend and senior and - 150",
    "- and - and - and chicken 100",
    "- and - and - and - 150",
]
print(solution(info, queries))