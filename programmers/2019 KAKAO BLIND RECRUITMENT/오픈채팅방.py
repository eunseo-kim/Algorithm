def message(type, name):
    if type == "Leave":
        return f"{name}님이 나갔습니다."
    return f"{name}님이 들어왔습니다."


def solution(records):
    answer = []

    names = {}
    for record in records:
        record = record.split(" ")

        if record[0] != "Leave":
            _, uid, name = record
            names[uid] = name

    for record in records:
        record = record.split(" ")

        if record[0] == "Change":
            continue

        if record[0] == "Enter":
            type, uid, _ = record
        else:
            type, uid = record
        answer.append(message(type, names[uid]))

    return answer


result = solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)
print(result)
