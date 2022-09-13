from collections import defaultdict


def get_all_cases(i, path, order):
    cases = []
    if len(path) > 1:
        cases.append(path)
    for j in range(i + 1, len(order)):
        cases += get_all_cases(j, path + order[j], order)
    return cases


def solution(orders, courses):
    order_count = defaultdict(int)
    menu_sets = defaultdict(set)
    for order in orders:
        cases = get_all_cases(-1, "", sorted(order))
        for case in cases:
            order_count[case] += 1
            menu_sets[len(case)].add(case)

    answer = []
    for course in courses:
        menus = menu_sets[course]
        max_cnt = 0
        result = []
        for menu in menus:
            if order_count[menu] > max_cnt and order_count[menu] >= 2:  # 최소 2명 이상
                max_cnt = order_count[menu]
                result = [menu]
            elif order_count[menu] == max_cnt:
                result.append(menu)
        answer += result
    
    answer.sort()
    return answer


result = solution(["XYZ", "XWY", "WXA"], [2, 3, 4])
print(result)