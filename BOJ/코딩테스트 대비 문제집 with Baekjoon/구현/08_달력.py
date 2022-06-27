# 언어 : Python
# 날짜 : 2022.06.27
# 문제 : BOJ > 달력 (https://www.acmicpc.net/problem/20207)
# 티어 : 실버 1
# ===========================================================================


def solution(todos):
    calendar = dict()

    for day in range(1, 366):
        calendar[day] = 0

    for start, end in todos:
        for day in range(start, end + 1):
            calendar[day] += 1

    row, col = 0, 0
    area = 0
    for day in range(1, 366):
        if calendar[day] == 0:
            area += row * col
            row, col = 0, 0
        else:
            col += 1
            row = max(row, calendar[day])
    area += row * col

    return area


# 입력 및 실행
N = int(input())
todos = []
for _ in range(N):
    todos.append(list(map(int, input().split(" "))))

answer = solution(todos)
print(answer)