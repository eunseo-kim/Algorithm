from collections import defaultdict

menus = defaultdict(int)


def dfs(idx, menu_course, length, order):

    if len(menu_course) == length:
        menu_course = list(menu_course)
        menu_course = sorted(menu_course)
        menu_course = "".join(map(str, menu_course))
        menus[menu_course] += 1

    if idx == len(order):
        return

    for j in range(idx + 1, len(order)):
        dfs(j, menu_course + order[j], length, order)


def solution(orders, course):
    for order in orders:
        for length in course:
            dfs(-1, "", length, order)  # idx, menu_course, length, order

    result = []
    for course_length in course:
        max_cnt = 0
        max_course = []
        for name, cnt in menus.items():
            if len(name) == course_length:
                if cnt > 1:
                    if cnt > max_cnt:
                        max_course = [name]
                        max_cnt = cnt
                    elif cnt == max_cnt:
                        max_course.append(name)

        for c in max_course:
            result.append(c)

    result.sort()

    return result


orders = ["XYZ", "XWY", "WXA"]
course = [2, 3, 4]
print(solution(orders, course))