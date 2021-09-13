# 언어 : Python
# 날짜 : 2021.06.22
# 문제 : Programmers > Lv1 > 신규 아이디 추천
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 개선 방법 : Level3 방법 개선(2가지 방식)
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


# 방법 1 : ".." → "."를 반복하여 ".."를 없앰
def level3(new_id):
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    return new_id


# 방법 2
# def level3(new_id):
#     changed = new_id[0]
#     for letter in new_id[1:]:  # changed 문자열의 끝이 "."이면 "."  추가 X
#         if changed[-1] == "." and letter == ".":
#             pass
#         else:
#             changed += letter
#     return changed


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
