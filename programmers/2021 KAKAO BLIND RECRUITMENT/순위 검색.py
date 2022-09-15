def solution(infos, queries):
    # get all cases
    all_cases = {}
    for info in infos:
        info = info.split(" ")
        for t1 in [info[0], "-"]:
            for t2 in [info[1], "-"]:
                for t3 in [info[2], "-"]:
                    for t4 in [info[3], "-"]:
                        if t1 + t2 + t3 + t4 in all_cases:
                            all_cases[t1 + t2 + t3 + t4].append(int(info[4]))
                        else:
                            all_cases[t1 + t2 + t3 + t4] = [int(info[4])]

    # 점수 내림차순 정렬시키기
    for case in all_cases.keys():
        all_cases[case].sort()

    def lower_bound(arr, key):  # 점수보다 작거나 같은 값이 가장 처음으로 등장하는 지점을 구합니다.
        left, right = 0, len(arr)
        while left < right:
            mid = (left + right) // 2
            if key <= arr[mid]:
                right = mid
            else:
                left = mid + 1

        return left

    # x점 이상 받은 지원자의 수 구하기
    answer = []
    for query in queries:
        query = query.replace(" and", "").split(" ")
        t1, t2, t3, t4, s = query
        if t1 + t2 + t3 + t4 not in all_cases:
            answer.append(0)
            continue

        lb = lower_bound(all_cases[t1 + t2 + t3 + t4], int(s))
        answer.append(len(all_cases[t1 + t2 + t3 + t4]) - lb)

    return answer


result = solution(
    [
        "java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50",
    ],
    [
        "java and backend and junior and pizza 100",
        "python and frontend and senior and chicken 200",
        "cpp and - and senior and pizza 250",
        "- and backend and senior and - 150",
        "- and - and - and chicken 100",
        "- and - and - and - 150",
    ],
)
print(result)
