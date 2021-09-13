# 언어 : Python
# 날짜 : 2021.06.22
# 문제 : Programmers > Lv1 > 신규 아이디 추천
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 소요 시간 : 40분
# 제출 시도 : 1회
# ================================================


def solution(new_id):
    answer = level7(level6(level5(level4(level3(level2(level1(new_id)))))))
    return answer


def level1(new_id):
    return new_id.lower()


def level2(new_id):
    changed = ""
    for letter in new_id:
        if letter not in "~!@#$%^&*()=+[{]}:?,<>/":
            changed += letter
    return changed


def level3(new_id):
    idx, dots = 0, 0
    changed = ""
    while new_id and idx < len(new_id):
        if new_id[idx] == ".":
            dots += 1
            if idx == len(new_id) - 1:
                changed += new_id[idx]
        else:
            if dots >= 1:
                changed += "."
                dots = 0
            changed += new_id[idx]
        idx += 1

    return changed

    if idx >= 2:
        return "." + new_id[idx:]
    return new_id


def level4(new_id):
    if new_id:
        if new_id[0] == ".":
            new_id = new_id[1:]
    if new_id:
        if new_id[-1] == ".":
            new_id = new_id[:-1]

    return new_id


def level5(new_id):
    if not new_id:
        return "a"
    return new_id


def level6(new_id):
    if len(new_id) >= 15:
        new_id = new_id[:15]
    if new_id[-1] == ".":
        return new_id[:-1]
    return new_id


def level7(new_id):
    letter = new_id[-1]
    while len(new_id) < 3:
        new_id += letter
    return new_id


# Test
new_id = "...!@BaT#*..y.abcdefghijklm"

new_id = "z-+.^."
print(solution(new_id))

new_id = "=.="
print(solution(new_id))

new_id = "123_.def"
print(solution(new_id))

new_id = "abcdefghijklmn.p"
print(solution(new_id))
