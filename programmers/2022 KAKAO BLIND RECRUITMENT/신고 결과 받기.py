from collections import defaultdict


def solution(id_list, report, k):
    answer = [0 for _ in range(len(id_list))]

    # [1] id별 신고자 명단 저장
    reported_id_list = defaultdict(set)

    # [2] 각 사람이 신고한 id list 저장
    report_user_list = defaultdict(set)

    for input in report:
        user, id = input.split(" ")
        reported_id_list[id].add(user)  # [1]
        report_user_list[user].add(id)  # [2]

    # [3] id_list의 유저별 처리결과 메일 회신 횟수
    for index, id in enumerate(id_list):
        reported_users = report_user_list[id]
        for reported_id in list(reported_users):
            if len(reported_id_list[reported_id]) >= k:
                answer[index] += 1

    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"]
result = solution(id_list, report, 2)
print(result)