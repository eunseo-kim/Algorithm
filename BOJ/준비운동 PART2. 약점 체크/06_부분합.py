# 언어 : Python
# 날짜 : 2021.07.15
# 문제 : BOJ > 부분합 (https://www.acmicpc.net/problem/1806)
# 티어 : 골드 4
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 오답 원인 : if cur_sum >= S or right == N - 1:에서 right == N-1일 때
# left를 N-1까지 +1해서 비교하는 과정을 빼먹었다.
# 그래서 자꾸 right ==N-1일때 right += 1로 가서 런타임 에러가 뜨거나
# 이걸 고쳐놓으면 while문이 무한반복 된다던지.. 마지막 원소를 빼먹는 문제가 생겼다.
# ============================================================================


def solution():
    left, right = 0, 0
    shortest_length = float("inf")
    cur_sum = nums[0]
    while left < N:
        if cur_sum >= S:
            cur_sum -= nums[left]
            left += 1
        else:
            right += 1
            cur_sum += nums[right]

        if cur_sum >= S:
            shortest_length = min(shortest_length, right - left + 1)

    if shortest_length == float("inf"):
        return 0
    return shortest_length


N, S = map(int, input().split())
nums = list(map(int, input().split()))
print(solution())