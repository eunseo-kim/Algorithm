# 언어 : Python
# 날짜 : 2022.1.13
# 문제 : BOJ > LCD Test (https://www.acmicpc.net/problem/2290)
# 티어 : 실버 2
# =========================================================================


def LCD():
    cur_row = 0
    cur_col = 0
    nums = str(n)
    test_monitor = [[" " for _ in range((col + 1) * len(nums))] for _ in range(row)]

    for num in nums:
        for segment in number[int(num)]:
            draw, (loc_r, loc_c) = seven_segment[segment]
            if draw == "-":
                r = loc_r
                for c in range(cur_col + loc_c, cur_col + loc_c + s):
                    test_monitor[r][c] = draw
            else:
                c = cur_col + loc_c
                for r in range(loc_r, loc_r + s):
                    test_monitor[r][c] = draw

        cur_col += col + 1

    for t in test_monitor:
        print("".join(map(str, t)))


s, n = map(int, input().split())
row, col = 2 * s + 3, s + 2

seven_segment = dict()
seven_segment[1] = ["-", (0, 1)]  # 글자, 시작 위치(+curr_row, curr_col)
seven_segment[2] = ["|", (1, 0)]
seven_segment[3] = ["|", (1, col - 1)]
seven_segment[4] = ["-", (row // 2, 1)]
seven_segment[5] = ["|", (row // 2 + 1, 0)]
seven_segment[6] = ["|", (row // 2 + 1, col - 1)]
seven_segment[7] = ["-", (row - 1, 1)]

number = dict()
number[1] = [3, 6]
number[2] = [1, 3, 4, 5, 7]
number[3] = [1, 3, 4, 6, 7]
number[4] = [2, 3, 4, 6]
number[5] = [1, 2, 4, 6, 7]
number[6] = [1, 2, 4, 5, 6, 7]
number[7] = [1, 3, 6]
number[8] = [1, 2, 3, 4, 5, 6, 7]
number[9] = [1, 2, 3, 4, 6, 7]
number[0] = [1, 2, 3, 5, 6, 7]

LCD()
