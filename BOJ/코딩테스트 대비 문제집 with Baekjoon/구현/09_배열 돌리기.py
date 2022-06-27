# 언어 : Python
# 날짜 : 2022.06.27
# 문제 : BOJ > 배열 돌리기 (https://www.acmicpc.net/problem/17276)
# 티어 : 실버 1
# ===========================================================================

from copy import deepcopy


def rotate_45(n, array):
    new_array = deepcopy(array)
    mid = n // 2

    # 주 대각선을 가운데 열로
    for i in range(n):
        new_array[i][mid] = array[i][i]

    # 가운데 열을 부 대각선으로
    for i in range(n):
        new_array[i][n - i - 1] = array[i][mid]

    # 부 대각선을 가운데 행으로
    for i in range(n):
        new_array[mid][n - i - 1] = array[i][n - i - 1]

    # 가운데 행을 주 대각선으로
    for i in range(n):
        new_array[i][i] = array[mid][i]

    return new_array


def solution(n, rotate_number, array):
    if rotate_number == 0:
        return array

    for _ in range(rotate_number):
        array = rotate_45(n, deepcopy(array))

    return array[:]


def print_array(array):
    for row in array:
        print(" ".join(map(str, row)))


for _ in range(int(input())):
    n, d = map(int, input().split(" "))
    rotate_number = ((d + 360) % 360) // 45
    array = []
    for _ in range(n):
        array.append(list(map(int, input().split(" "))))

    answer = solution(n, rotate_number, array)
    print_array(answer)