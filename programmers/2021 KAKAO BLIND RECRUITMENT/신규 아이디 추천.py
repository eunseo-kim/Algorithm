import re


def solution(new_id):
    # level 1
    new_id = new_id.lower()

    # level 2
    new_id = "".join(re.findall("[a-z|0-9|\-|\_|\.]", new_id))

    # level 3
    new_id = re.sub("\.{2,}", ".", new_id)

    # level 4
    new_id = re.sub("^\.|\.$", "", new_id)

    # level 5
    new_id = "a" if len(new_id) == 0 else new_id

    # level 6
    new_id = "".join(new_id[:15]) if len(new_id) >= 16 else new_id
    new_id = re.sub("\.$", "", new_id)

    # level 7
    new_id = (new_id + new_id[-1] * 2)[:3] if len(new_id) <= 2 else new_id
    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm..."))
