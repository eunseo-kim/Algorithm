import re
from collections import defaultdict

banned_list = set()


def solution(user_id, banned_id):
    if banned_id == []:
        return 0

    banned_dict = defaultdict(set)
    banned_count_dict = defaultdict(int)
    arr = []

    for id in banned_id:
        banned_count_dict[id] += 1

        # 후보군 구하기
        p = "[0-9a-z]{1}"
        new_id = "^" + re.sub("\*", p, id) + "$"
        pattern = re.compile(r"" + new_id)

        for uid in user_id:
            if pattern.match(uid) and uid not in banned_dict:
                banned_dict[id].add(uid)

    # 최종 후보군
    for id in banned_id:
        arr.append(banned_dict[id])
    dfs(len(banned_id), 0, arr, [], 0)

    return len(banned_list)


def dfs(max_idx, idx, arr, path, count):
    global banned_list

    if idx == max_idx:
        banned_list.add(str(sorted(path)))
        return

    for id in arr[idx]:
        if id not in path:
            dfs(max_idx, idx + 1, arr, path + [id], count)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodc"]
banned_id = ["***d*", "*rodo", "******", "*****"]
result = solution(user_id, banned_id)
print(result)