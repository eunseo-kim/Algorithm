# 언어 : Python
# 날짜 : 2022.06.29
# 문제 : BOJ > 배열 돌리기 1 (https://www.acmicpc.net/problem/16926)
# 티어 : 실버 1
# ===========================================================================


def solution(row, col, r, arr):
    rotate = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for _ in range(r):
        s = 0
        row_gap = row - 1
        col_gap = col - 1
        rotate_idx = 0

        r, c = 0, 0

        while row_gap > 0 and col_gap > 0:
            tmp = arr[s][s]

            for _ in range(2):
                for _ in range(col_gap):
                    new_r, new_c = r + rotate[rotate_idx][0], c + rotate[rotate_idx][1]

                    arr[r][c] = arr[new_r][new_c]
                    r = new_r
                    c = new_c
                rotate_idx += 1

                for _ in range(row_gap):
                    new_r, new_c = r + rotate[rotate_idx][0], c + rotate[rotate_idx][1]
                    arr[r][c] = arr[new_r][new_c]

                    r = new_r
                    c = new_c
                rotate_idx += 1

            arr[r + 1][c] = tmp
            row_gap -= 2
            col_gap -= 2
            r = s + 1
            c = s + 1
            s += 1
            rotate_idx = 0

    return arr


def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))


row, col, r = map(int, input().split())
arr = []
for _ in range(row):
    arr.append(list(map(int, input().split())))
result = solution(row, col, r, arr)
print_array(result)