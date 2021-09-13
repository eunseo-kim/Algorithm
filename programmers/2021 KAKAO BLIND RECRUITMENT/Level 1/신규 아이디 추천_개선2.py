# 언어 : Python
# 날짜 : 2021.06.22
# 문제 : Programmers > Lv1 > 신규 아이디 추천
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# ================================================
# 개선 방법 : 정규식 사용
# re.sub('패턴', '바꿀문자열', '문자열', 바꿀횟수)
# ================================================

import re


def solution(new_id):
    answer = new_id
    # 1단계 : 모두 소문자로 치환
    answer = answer.lower()

    # 2단계 : 알파벳, 숫자, -, _, .를 제외한([^]) 모든 문제를 ""으로 치환
    answer = re.sub("[^a-z0-9\-\_\.]", "", answer)

    # 3단계 : 마침표가 1개 이상(+)이면 하나로 치환
    answer = re.sub("\.+", ".", answer)

    # 4단계 : 마침표가 처음(^)/끝($)이라면 제거
    answer = re.sub("^[.]|[.]$", "", answer)

    # 5단계 : 빈 문자열이면 "a"
    if not answer:
        answer = "a"

    # 6단계 : 16자 이상이면 앞의 15개만
    if len(answer) > 15:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]

    # 7단계 : 길이가 2자 이하면 맨 마지막 문자를 3이 될때까지 반복
    if len(answer) <= 2:
        answer += answer[-1] * (3 - len(answer))

    return answer
