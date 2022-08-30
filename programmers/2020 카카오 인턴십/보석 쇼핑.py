from collections import defaultdict


def solution(gems):
    answer = [0, float("inf")]
    collected = defaultdict(int)
    collected_set = set()
    GEMS_COUNT = len(set(gems))

    left, right = 0, 0
    while right <= len(gems):
        if len(collected_set) == GEMS_COUNT:
            while left <= right:
                if right - left < answer[1] - answer[0]:
                    answer = [left, right]
                removed_gem = gems[left]
                collected[removed_gem] -= 1
                left += 1
                if collected[removed_gem] == 0:
                    collected_set.remove(removed_gem)
                    break

        if right >= len(gems):
            break
        collected[gems[right]] += 1
        collected_set.add(gems[right])
        right += 1

    return [answer[0] + 1, answer[1]]


gems = ["A", "B", "B", "C", "A", "B", "C", "A", "B", "C"]
result = solution(gems)
print(result)
