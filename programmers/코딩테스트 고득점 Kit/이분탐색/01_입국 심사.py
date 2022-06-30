# 언어 : Python
# 날짜 : 2022.06.30
# 문제 : Programmers > 입국 심사
# 티어 : Lv 3
# ==============================================================


def lower_bound(min_time, max_time, times, target):
    while min_time < max_time:
        mid_time = (min_time + max_time) // 2

        # [1] mid_time동안 처리할 수 있는 사람 수
        available = 0
        for time in times:
            available += mid_time // time

        # [2] move to left side
        if available >= target:
            max_time = mid_time

        # [3] move to right side
        else:
            min_time = mid_time + 1

    return min_time


def solution(n, times):
    # [1] 이분탐색의 범위 : '모든 입국 심사를 다 마치는데 걸리는 시간' => 시간은 언제나 정렬된 상태이므로 이분 탐색을 하기에 적합합니다.
    left = 0
    right = 10 ** 21

    # [2] 이분 탐색의 조건 : n명을 모두 심사할 수 있는 최소 시간(lower bound)을 찾는 것
    answer = lower_bound(left, right, times, n)

    return answer


n = 6
times = [7, 10]
result = solution(n, times)
print(result)