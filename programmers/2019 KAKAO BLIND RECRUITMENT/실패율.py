def solution(N, stages):
    reached = [0 for _ in range(N + 2)]
    failures = [0 for _ in range(N + 2)]
    for stage in stages:
        for i in range(1, stage + 1):  # 현재 플레이어는 1~stage 까지 도달했습니다.
            reached[i] += 1
        # 현재 stage에는 도달했지만 통과하지 못했습니다.
        failures[stage] += 1

    rates = []
    for i in range(1, N + 1):
        if reached[i] == 0:
            rate = 0
        else:
            rate = failures[i] / reached[i]
        rates.append([rate, i])
    rates.sort(reverse=True, key=lambda x: x[0])

    answer = []
    for _, i in rates:
        answer.append(i)
    return answer


result = solution(5, [2, 1, 2, 6, 2, 4, 3, 3])
print(result)
