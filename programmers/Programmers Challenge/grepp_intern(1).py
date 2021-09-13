# 1번 : solved(통과함)
from collections import defaultdict


def solution(arr):
    answer = 0
    nums = defaultdict(int)

    for a in arr:
        nums[a] += 1

    keys = []
    values = []
    for key, value in sorted(nums.items()):
        keys.append(key)
        values.append(value)

    diff = float("inf")

    for i in range(1, len(keys)):
        new_diff = abs(sum(values[:i]) - sum(values[i:]))
        if new_diff < diff:
            answer = keys[i - 1] + 1
            diff = new_diff

    return answer


# test case
arr1 = [0, 0, 255, 255, 0, 0, 255, 255, 255]
print(solution(arr1))