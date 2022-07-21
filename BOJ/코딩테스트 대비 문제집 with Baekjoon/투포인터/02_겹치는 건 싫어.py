# 언어 : Python
# 날짜 : 2022.7.21
# 문제 : BOJ > 겹치는 건 싫어 (https://www.acmicpc.net/problem/20922)
# 티어 : 실버 1
# =========================================================================


def get_number_count():
    number_count = dict()
    for number in range(1, 200001):
        number_count[number] = 0

    return number_count


def solution():
    number_count = get_number_count()

    max_length = 0
    curr_length = 0

    left, right = 0, 0
    while right < N:
        number = arr[right]

        if number_count[number] >= K:
            # left를 한칸 오른쪽으로
            number_count[arr[left]] -= 1
            left += 1
            curr_length -= 1
        else:
            number_count[arr[right]] += 1
            curr_length += 1
            right += 1

        max_length = max(max_length, curr_length)

    return max_length


N, K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
result = solution()
print(result)