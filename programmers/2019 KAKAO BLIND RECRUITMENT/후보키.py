def solution(relation):
    candidate_keys = []

    # 1. 모든 가능한 키 조합을 구합니다.
    def get_all_combinations(i, N, path, arr):
        cases = []
        if len(path) >= 1:
            cases.append(path)
        for j in range(i + 1, N):
            cases += get_all_combinations(j, N, path + [arr[j]], arr)
        return cases

    all_cases = get_all_combinations(-1, len(relation[0]), [], [i for i in range(len(relation[0]))])
    all_cases.sort(key=lambda x: len(x))

    # 2. 각 키 조합에 대하여 유일성을 만족하는지 체크합니다.
    possible_keys = []
    for keys in sorted(all_cases):  # keys = [1, 2, 3]
        is_unique_key = True
        attributes = set()
        for row in range(len(relation)):
            key = []
            for col in sorted(keys):
                key.append(relation[row][col])
            if "".join(map(str, key)) in attributes:
                is_unique_key = False
                break
            attributes.add("".join(map(str, key)))
        if is_unique_key:
            possible_keys.append(sorted(keys))

    # 3. 최소성을 만족하는지 여부를 체크합니다.
    possible_keys.sort(key=lambda x: len(x))
    for curr_key in possible_keys:
        all_key_combinations = get_all_combinations(-1, len(curr_key), [], curr_key)
        all_key_combinations.sort(key=lambda x: len(x))
        is_candidate_key = True
        for combination in all_key_combinations:
            if sorted(combination) in candidate_keys:
                is_candidate_key = False
                break
        if is_candidate_key:
            candidate_keys.append(sorted(curr_key))

    return len(candidate_keys)


result = solution(
    [
        ["100", "ryan", "music", "2"],
        ["200", "apeach", "math", "2"],
        ["300", "tube", "computer", "3"],
        ["400", "con", "computer", "4"],
        ["500", "muzi", "music", "3"],
        ["600", "apeach", "music", "2"],
    ]
)
print(result)
