from collections import defaultdict


def solution(id_list, report, k):
    # reports
    report_name = defaultdict(set)
    for case in report:
        from_name, to_name = case.split(" ")
        report_name[to_name].add(from_name)

    # mail
    mail = defaultdict(set)
    for id in id_list:
        if len(report_name[id]) >= k:
            for name in report_name[id]:
                mail[name].add(id)

    answer = []
    for id in id_list:
        answer.append(len(mail[id]))

    return answer