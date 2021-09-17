# 언어 : Python
# 날짜 : 2021.09.17
# 문제 : KOREATECH JUDGE > 카드 정리(1150번)
# 소요시간: 4' 36"
# ==============================================================


def solution():
    remove_list = ["A", "E", "I", "O", "U"]
    string = input()
    cnt = 0

    for i, s in enumerate(string):
        if s.upper() in remove_list:
            cnt += len(string[i + 1 :])

    return cnt


for _ in range(int(input())):
    print(solution())