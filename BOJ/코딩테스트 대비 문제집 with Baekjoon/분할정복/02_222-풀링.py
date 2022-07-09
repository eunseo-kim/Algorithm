# 언어 : Python
# 날짜 : 2022.7.9
# 문제 : BOJ > 222-풀링 (https://www.acmicpc.net/problem/17829)
# 티어 : 실버 2
# =========================================================================


def divide(n, arr):
    # 풀링을 반복하여 크기를 1x1로 만들었을때의 결과를 출력하고 종료합니다.
    if n == 1:
        print(arr[0][0])
        exit(0)

    # 222-풀링을 1회 적용합니다.
    m = n // 2
    # new_arr : 222-풀링을 1회 적용한 후 1/4 크기로 작아진 행렬입니다.
    new_arr = [[0 for _ in range(m)] for _ in range(m)]
    for i in range(0, n, 2):
        for j in range(0, n, 2):
            # 2x2 정사각형에서 2번째로 큰 수만 남깁니다.
            list = []
            for r in range(i, i + 2):
                for c in range(j, j + 2):
                    list.append(arr[r][c])
            list.sort(reverse=True)
            new_arr[i // 2][j // 2] = list[1]

    # 222-풀링을 반복합니다.
    divide(m, new_arr)


N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split(" "))))
divide(N, arr)
