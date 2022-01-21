# 언어 : Python
# 날짜 : 2022.1.21
# 문제 : 2020 Kakao Internship > 1. 숫자 문자열과 영단어
# 티어 : Lv.1
# 시간 : 15분
# =========================================================================


def solution(s):
    nums = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }

    number = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    answer = []
    start = 0
    length = len(s)
    for end in range(length):
        if "".join(map(str, s[start : end + 1])) in nums:
            answer.append(nums["".join(map(str, s[start : end + 1]))])
            start = end + 1
        elif s[end] in number:
            answer.append(s[end])
            start = end + 1
    return int("".join(map(str, answer)))


s = "123"
print(solution(s))