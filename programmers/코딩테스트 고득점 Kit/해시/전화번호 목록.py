# 언어 : Python
# 날짜 : 2022.1.7
# 문제 : programmers > 전화번호 목록
# 티어 : Level 2
# =====================================================================


# 정렬
# - sort를 쓰면 인접한 애들만 검사해도 됨(abc 순으로 정렬됨)
def solution(phone_book):
    phone_book.sort()

    for p1, p2 in zip(phone_book[:-1], phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True
