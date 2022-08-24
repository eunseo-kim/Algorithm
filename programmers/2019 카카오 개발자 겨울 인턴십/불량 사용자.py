def solution(user_id, banned_id):
    banned_id_lists = []
    for bid in banned_id:
        temp = []
        for uid in user_id:
            possible = True
            if len(uid) != len(bid):
                continue
            for i in range(len(bid)):
                if bid[i] == "*":
                    continue
                if bid[i] != uid[i]:
                    possible = False
                    break

            if possible:
                temp.append(uid)
        banned_id_lists.append(temp)

    def dfs(path, index):
        if len(path) == len(banned_id_lists):
            if str(set(sorted(path))) not in answer:
                answer.add(str(set(sorted(path))))
            return

        for i in range(index + 1, len(banned_id_lists)):
            for id in banned_id_lists[i]:
                if id not in path:
                    path.append(id)
                    dfs(path, i)
                    path.remove(id)

    answer = set()
    dfs([], -1)
    return len(answer)


user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["*rodo", "*rodo", "******"]
result = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(result)