def solution(id_list, report, k):
    n = len(id_list)
    id_dict = {}
    for i, id in enumerate(id_list):
        id_dict[id] = i

    result = [[0 for _ in range(n)] for _ in range(n)]
    for rp in report:
        p1, p2 = rp.split()
        n1, n2 = id_dict[p1], id_dict[p2]
        result[n2][n1] = 1

    warning = []
    for i, re in enumerate(result):
        if sum(re) >= k:
            warning.append(i)

    answer = [0 for _ in range(n)]
    for warn in warning:
        for i in range(n):
            if result[warn][i] != 0:
                answer[i] += 1
    return answer


# id_list = ["muzi", "frodo", "apeach", "neo"]
# report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
# k = 2
id_list = ["con", "ryan"]
report = ["ryan con", "ryan con", "ryan con", "ryan con"]
k = 3

solution(id_list, report, k)

# 시간: 24'