# 누적 1'30"

from collections import defaultdict


def solution(n, info):
    candidates = defaultdict(list)  # 가능한 후보들을 구합니다.

    def get_cases(case, i, left_turns, apeach, ryan):
        if len(case) == 11:
            # 만약 turn이 남아있으면 다 써야됨
            if left_turns > 0:
                case[10] += left_turns
            if apeach >= ryan:  # 어피치가 이기는 경우
                return
            curr_gap = ryan - apeach
            candidates[curr_gap].append(case[::-1])
            return

        for j in range(i, 11, 1):
            curr_get_score = 0

            # (1) 라이언이 점수 (10-j)에 화살을 쏘지 않는다.
            if info[j] > 0:
                curr_get_score = 10 - j
            get_cases(case + [0], j + 1, left_turns, apeach + curr_get_score, ryan)

            # (2) 라이언이 점수 (10-j)에 화살을 쏜다.
            if info[j] < left_turns:
                curr_get_score = 10 - j
                get_cases(case + [info[j] + 1], j + 1, left_turns - (info[j] + 1), apeach, ryan + curr_get_score)

    get_cases([], 0, n, 0, 0)

    if len(candidates.keys()) == 0:
        return [-1]

    # candidates의 key(=점수 차이)가 가장 큰 요소의 value들 중
    # 가장 낮은 점수를 더 많이 맞힌 경우가 정답
    max_score_gap = max(candidates.keys())
    candidate_answers = sorted(candidates[max_score_gap], reverse=True)
    return candidate_answers[0][::-1]


n = 5
info = [2, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0]
result = solution(n, info)
print(result)