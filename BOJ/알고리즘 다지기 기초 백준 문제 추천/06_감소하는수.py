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
        cnt = 9
        number = 10

    while True:
        is_decreasing = True
        str_num = str(number)
        for i in range(1, len(str_num)):
            if int(str_num[i]) < int(str_num[i - 1]):
                continue
            else:
                start = str_num[: i - 1]
                mid = str(int(str_num[i - 1]) + 1)
                end = "0" + str_num[i + 1 :]
                number = int(start + mid + end)
                is_decreasing = False
                break

        if is_decreasing:
            cnt += 1
            if cnt == target:
                return number
            number += 1

    return -1


target = int(input())
if target >= 1023:  # 1022번째 => 9876543210(N은 1,000,000보다 작거나 같은 자연수 또는 0이다.)
    print(-1)
else:
    result = solution()
    print(result)