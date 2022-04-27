def solution(gems):
    kinds = set()

    for gem in gems:
        kinds.add(gem)

    gem_count = dict()
    for kind in kinds:
        gem_count[kind] = 0

    left, right = 0, 0
    min_section = float("inf")
    gem_sets = set()

    while left <= right and right < len(gems):
        curr_gem = gems[right]
        gem_count[curr_gem] += 1
        gem_sets.add(curr_gem)

        # collected all gems
        if gem_sets == kinds:
            while left <= right:
                removed_gem = gems[left]
                if gem_count[removed_gem] - 1 == 0:
                    gem_sets.remove(removed_gem)
                    # get the answer left, right
                    curr_section = right - left
                    if curr_section < min_section:
                        min_section = curr_section
                        answer = [left + 1, right + 1]
                    break

                gem_count[removed_gem] -= 1
                left += 1

        right = right + 1

    return answer


gems = [1, 2, 2, 3, 1]
result = solution(gems)
print(result)