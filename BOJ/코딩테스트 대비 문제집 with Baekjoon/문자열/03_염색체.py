# 언어 : Python
# 날짜 : 2022.3.5
# 문제 : BOJ > 염색체 (https://www.acmicpc.net/problem/9342)
# 티어 : 실버 4
# <문제>
# 문자열은 {A, B, C, D, E, F} 중 0개 또는 1개로 시작해야 한다.
# 그 다음에는 A가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 F가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 C가 하나 또는 그 이상 있어야 한다.
# 그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.
# 문제의 규칙을 지키는 문자열인 경우에는  "Infected!"를, 아닌 경우에는 "Good"을 출력한다.
# =============================================================================

# <정규식>
# . : 모든
# * : 반복(0번부터)
# + : 반복(1번부터)
# {m, n} : m~n번까지 반복
# {m} : m번 반복
# ? : 있어도 되고 없어도 된다. == {0, 1}
# ^ : 문자열의 처음
# $ : 문자열의 마지막
# [^] : 반대(not)

import re

check = re.compile("^[A-F]?A+F+C+[A-F]?$")


def solution(string):
    if check.match(string) != None:
        return True
    return False


for _ in range(int(input())):
    result = solution(input())
    if result:
        print("Infected!")
    else:
        print("Good")
