# 언어 : Python
# 날짜 : 2021.07.13
# 문제 : BOJ > 지능형 기차2
# 티어 : 브론즈 3
# =====================================================
# 소요 시간 : 7'
# 제출 시도 : 1
# 오답 이유 : -
# =====================================================


def solution():
    max_count = float("-inf")
    cur_count = 0
    for _ in range(10):
        count_out, count_in = map(int, input().split())
        cur_count += count_in - count_out
        max_count = max(max_count, cur_count)

    print(max_count)


solution()