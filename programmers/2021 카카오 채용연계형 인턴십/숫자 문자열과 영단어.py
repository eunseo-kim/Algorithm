def solution(s):
    change = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "ten": "10",
    }

    for old in change.keys():
        s = s.replace(old, change[old])

    return int(s)


result = solution("2three45sixseven")
print(result)
