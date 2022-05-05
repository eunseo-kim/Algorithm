def get_score(apeach, ryan):
    apeach_score, ryan_score = 0, 0

    for i in range(11):
        if apeach[i] == 0 and ryan[i] == 0:
            continue

        if ryan[i] > apeach[i]:
            ryan_score += 10 - i
        else:
            apeach_score += 10 - i

    if apeach_score < ryan_score:
        return apeach_score, ryan_score
    return -1, -1


def solution(n, apeach):
    max_score_gap = -1
    ryan_max_case = None
    ryan_max_score = -1
    ryan = [0 for _ in range(11)]

    # 어피치 마지막 과녁
    for i in range(11):
        if apeach[i] != 0:
            apeach_last = i
    apeach_last += 1

    queue = []
    queue.append([0, n, ryan])  # idx, left_count, score_arr

    while queue:
        idx, left_count, ryan = queue.pop(0)

        if idx == 10 and left_count != 0:
            ryan[idx] = left_count
            left_count = 0

        if idx > 10:
            continue

        if left_count == 0:
            # print("RYAN:", ryan)
            apeach_score, ryan_score = get_score(apeach, ryan)
            if ryan_score != -1:
                curr_score_gap = ryan_score - apeach_score
                if max_score_gap <= curr_score_gap:
                    max_score_gap = curr_score_gap
                    ryan_max_case = ryan
        else:
            if idx < 10:
                apeach_count = apeach[idx]
                if left_count > apeach_count:
                    # 선택한다.
                    ryan[idx] = apeach_count + 1
                    queue.append([idx + 1, left_count - apeach_count - 1, ryan[:]])
                # 선택하지 않는다.
                ryan[idx] = 0
                queue.append([idx + 1, left_count, ryan[:]])

    return [-1] if not ryan_max_case else ryan_max_case


n, info = 6, [0, 0, 1, 1, 2, 1, 0, 0, 0, 0, 0]
result = solution(n, info)
print(result)