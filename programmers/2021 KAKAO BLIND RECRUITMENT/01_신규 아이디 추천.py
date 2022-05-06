import re


def solution(new_id):
    new_id = new_id.lower()

    pattern = "[^a-z0-9\-\_\.]"
    new_id = re.sub(pattern, "", new_id)

    pattern = "\.{2,}"
    new_id = re.sub(pattern, ".", new_id)

    pattern = "^\.{1,}"
    new_id = re.sub(pattern, "", new_id)

    pattern = "\.{1,}$"
    new_id = re.sub(pattern, "", new_id)

    if len(new_id) == 0:
        new_id = "a"

    if len(new_id) >= 16:
        new_id = new_id[0:15]

    pattern = "^[.]{1,}"
    new_id = re.sub(pattern, "", new_id)

    pattern = "[.]{1,}$"
    new_id = re.sub(pattern, "", new_id)

    if len(new_id) == 1:
        new_id += new_id[-1] * 2
    elif len(new_id) == 2:
        new_id += new_id[-1]

    return new_id


new_id = "abcdefghijklmn.p"
print(solution(new_id))