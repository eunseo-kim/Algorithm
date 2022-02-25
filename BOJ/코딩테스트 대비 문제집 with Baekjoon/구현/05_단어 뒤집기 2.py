# 언어 : Python
# 날짜 : 2022.2.25
# 문제 : BOJ > 단어 뒤집기 (https://www.acmicpc.net/problem/17413)
# 티어 : 실버 3
# =========================================================================


def solution():
    i = 0
    length = len(string)
    result = []
    word = []

    while i < length:
        if string[i] == "<" or string[i] == " ":
            # 단어 뒤집기 
            if word != []:
                result.append("".join(map(str, word[::-1])))
            word = []
            
            # <...> 태그 구분하기
            if string[i] == "<":
                while string[i] != ">":
                    result.append(string[i])
                    i += 1
            result.append(string[i])
        else:
            word.append(string[i])
        i += 1

    if word != []:
        result.append("".join(map(str, word[::-1])))

    print("".join(map(str, result)))


string = list(input())
solution()