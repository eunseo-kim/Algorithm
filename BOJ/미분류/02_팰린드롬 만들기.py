# 언어 : Python
# 날짜 : 2021.11.11
# 문제 : BOJ > 팰린드롬 만들기(https://www.acmicpc.net/problem/1254)
# 티어 : 실버 1
# 풀이
# ex. abab ↔ baba
# abab
# baba
# ----
# abab
# →baba (한칸 뒤로 미룸) => 일치! => 최종 길이는 (원래길이 + 미룬 칸 수) 4 + 1 = 5
# ==============================================================================
def solution():
    length = len(s)
    reversed_s = s[::-1]
    move_cnt = 0

    while True:
        is_valid = True

        if move_cnt == length:
            break

        for idx in range(move_cnt, length):
            if s[idx] != reversed_s[idx - move_cnt]:
                is_valid = False
                break

        if is_valid:
            break

        move_cnt += 1

    return length + move_cnt


s = input()
print(solution())