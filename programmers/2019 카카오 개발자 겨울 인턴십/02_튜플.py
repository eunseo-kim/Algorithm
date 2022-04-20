from unicodedata import decimal

# {2},{2,1},{2,1,3},{2,1,3,4}
# {20,111},{111}


def solution(s):
    idx = 0
    s = s[1:-1]
    group = []
    length = len(s)
    while idx < length:
        if s[idx] == ",":
            idx += 1
        if s[idx] == "{":
            current_group = []
            idx += 1
            number = 0
            while s[idx] != "}":
                if s[idx] == ",":
                    idx += 1
                    current_group.append(number)
                    number = 0
                    continue
                number = 10 * number + int(s[idx])
                idx += 1
            current_group.append(number)
            group.append(current_group)
            idx += 1

    group.sort(key=len)
    numbers = set()
    answer = []

    for part in group:
        for num in part:
            if num not in numbers:
                numbers.add(num)
                answer.append(num)
                break

    return answer


s = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]
for ss in s:
    result = solution(ss)
    print(result)
