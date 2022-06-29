# 언어 : Python
# 날짜 : 2022.06.29
# 문제 : BOJ > 배열 돌리기 2 (https://www.acmicpc.net/problem/16927)
# 티어 : 골드 5
# ===========================================================================

import sys

from collections import deque


def solution(row, col, rotate_count, arr):
    row_gap = row - 1
    col_gap = col - 1

    if row_gap == 0 or col_gap == 0:
        return arr

    s, r, c = 0, row - 1, col - 1
    while row_gap > 0 and col_gap > 0:
        standard_rotate_count = (row_gap + col_gap) * 2
        rotate = rotate_count % standard_rotate_count

        rotate_list = deque()

        # 상 - 우 - 하 - 좌 / 1차원 배열에 담기
        for i in range(s, s + col_gap):
            rotate_list.append(arr[s][i])

        for i in range(s, s + row_gap):
            rotate_list.append(arr[i][c])

        for i in range(s + col_gap, s, -1):
            rotate_list.append(arr[r][i])

        for i in range(s + row_gap, s, -1):
            rotate_list.append(arr[i][s])

        # 1차원 배열 회전 / rotate번 만큼 맨 앞의 숫자를 빼서 맨 뒤에 삽입
        for _ in range(rotate):
            tmp = rotate_list.popleft()
            rotate_list += [tmp]

        # 1차원 배열을 다시 상-우-하-좌 순으로 이차원 배열에 삽입
        for i in range(s, s + col_gap):
            arr[s][i] = rotate_list.popleft()

        for i in range(s, s + row_gap):
            arr[i][c] = rotate_list.popleft()

        for i in range(s + col_gap, s, -1):
            arr[r][i] = rotate_list.popleft()

        for i in range(s + row_gap, s, -1):
            arr[i][s] = rotate_list.popleft()

        row_gap -= 2
        col_gap -= 2
        s += 1
        r -= 1
        c -= 1

    return arr


def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))


row, col, rotate = map(int, sys.stdin.readline().split())
arr = []
for _ in range(row):
    arr.append(list(map(int, sys.stdin.readline().split())))
result = solution(row, col, rotate, arr)
print_array(result)
