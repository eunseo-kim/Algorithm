# 언어 : Python
# 날짜 : 2021.07.26
# 문제 : BOJ > 감소하는수 (https://www.acmicpc.net/problem/1038)
# 티어 : 실버 1
# ======================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : -
# ======================================================================


def solution():
    if target < 10:
        return target
    else:
        number = 9
        cnt = 10

    while cnt <= target:
        # print("=========\n", cnt, number)
        str_num = str(number)
        cur_num = int(str_num[0])
        is_decreasing = True
        for s in str_num[1:]:
            # print("s:", s)
            if cur_num <= int(s):
                is_decreasing = False
                break
            cur_num = int(s)
        if is_decreasing:
            cnt += 1
        number += 1

    return number


target = int(input())
result = solution()
print(result)