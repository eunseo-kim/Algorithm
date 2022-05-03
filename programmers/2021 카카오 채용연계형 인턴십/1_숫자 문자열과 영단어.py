import re


def solution(s):
    pattern = "[0-9]"
    alpha = {
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "zero": 0,
    }

    answer = []
    while s != "":
        if re.match(pattern, s[0]):
            answer.append(int(s[0]))
            s = re.sub(s[0], "", s, 1)
        else:
            for a in alpha:
                if re.match(a, s):
                    s = re.sub(a, "", s, 1)
                    answer.append(alpha[a])

    return int("".join(map(str, answer)))


s = "12352onetwothree"
result = solution(s)
print(result)
