# 언어 : Python
# 날짜 : 2021.06.24
# 문제 : Programmers > Lv2 > 메뉴 리뉴얼
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 소요 시간 : 51분
# 제출 시도 : 1회
# ================================================
from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    order_dict_list = [defaultdict(int) for _ in range(len(course))]

    for order in orders:
        for idx, size in enumerate(course):
            order_combinations = combinations(sorted(order), size)
            for m in order_combinations:
                order_dict_list[idx][m] += 1

    answer = []
    for menu_dict in order_dict_list:
        if menu_dict:
            result = sorted(menu_dict.items(), key=lambda x: x[1], reverse=True)
            most_ordered = result[0][1]
            for other in result:
                if most_ordered > 1 and other[1] == most_ordered:
                    answer.append("".join(other[0]))
                else:
                    break

    return sorted(answer)


# orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
# orders = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"]
orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
answer = solution(orders, course)
print(answer)