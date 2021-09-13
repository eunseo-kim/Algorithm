# 언어 : Python
# 날짜 : 2021.09.09
# 문제 : BOJ > 스티커 (https://www.acmicpc.net/problem/9465)
# 티어 : 실버 2
# 풀이 : 현재 칸까지의 최댓값 = 대각선 방향의 이전 칸까지의 최댓값 + 현재 칸
# ===========================================================================

T = int(input())

for _ in range(T):
    N = int(input())

    arr = []
    for _ in range(2):
        arr.append(list(map(int, input().split())))

    if N == 1:
        print(max(arr)[0])
        continue

    arr[0][1] = arr[0][1] + arr[1][0]
    arr[1][1] = arr[1][1] + arr[0][0]

    for k in range(2, N):
        arr[0][k] += max(arr[1][k - 1], arr[1][k - 2])
        arr[1][k] += max(arr[0][k - 1], arr[0][k - 2])

    answer = max(arr[0][N - 1], arr[1][N - 1])
    print(answer)