# 언어 : Python
# 날짜 : 2022.3.2
# 문제 : BOJ > 홀수 홀릭 호석 (https://www.acmicpc.net/problem/20164)
# 티어 : 골드 5
# =========================================================================


def count_odd(nums):
    count = 0
    for num in str(nums):
        if int(num) % 2 == 1:
            count += 1

    return count


def solution():
    max_num, min_num = -float("inf"), float("inf")
    queue = [[num, 0]]  # [num], count(홀수의 개수)
    while queue:
        curr, count = queue.pop(0)
        curr_count = count + count_odd(curr)

        if curr < 10:
            max_num = max(max_num, curr_count)
            min_num = min(min_num, curr_count)
        elif curr < 100:
            n1 = curr % 10
            n2 = curr // 10
            queue.append([n1 + n2, curr_count])
        else:
            curr_list = str(curr)
            curr_length = len(curr_list)
            for i in range(1, curr_length - 1):
                for j in range(i + 1, curr_length):
                    next = int("".join(curr_list[:i])) + int("".join(curr_list[i:j])) + int("".join(curr_list[j:]))
                    queue.append([next, curr_count])

    print(min_num)
    print(max_num)


num = int(input())
N = len(str(num))
solution()
