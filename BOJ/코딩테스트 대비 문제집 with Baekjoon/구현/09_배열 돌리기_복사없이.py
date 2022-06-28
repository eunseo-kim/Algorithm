# 배열 돌리기를 "복사 없이" 풀어보자.


def solution(n, d, arr):
    rotate_number = ((d + 360) % 360) // 45
    m = n // 2

    for _ in range(rotate_number):
        for gap in range(1, m + 1):
            s, e = m - gap, m + gap

            tmp = arr[s][s]
            arr[s][s] = arr[m][s]
            arr[m][s] = arr[e][s]
            arr[e][s] = arr[e][m]
            arr[e][m] = arr[e][e]
            arr[e][e] = arr[m][e]
            arr[m][e] = arr[s][e]
            arr[s][e] = arr[s][m]
            arr[s][m] = tmp

    return arr


def print_array(arr):
    for row in arr:
        print(" ".join(map(str, row)))


T = int(input())
for _ in range(T):
    n, d = map(int, input().split())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().split(" "))))
    result = solution(n, d, arr)
    print_array(result)