# 언어 : Python
# 날짜 : 2021.06.26
# 문제 : Programinuteers > Lv3 > 광고 삽입
# 출처 : 2021 KAKAO BLIND RECRUITMENT
# =====================================================
# 소요 시간 : -
# 제출 시도 : Failed
# =====================================================
import re


def time_to_seconds(time):
    hour, minute, second = map(int, re.sub(":", " ", time).split())
    return hour * 60 * 60 + minute * 60 + second


def seconds_to_time(seconds):
    second = seconds % 60
    seconds //= 60
    minute = seconds % 60
    seconds //= 60
    hour = seconds

    return str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2)


def solution(play_time, adv_time, logs):
    total_play_sec = time_to_seconds(play_time)
    total_adv_sec = time_to_seconds(adv_time)
    time_log = [0 for _ in range(total_play_sec + 1)]

    for log in logs:
        start, end = re.sub("-", " ", log).split()
        start_sec = time_to_seconds(start)
        end_sec = time_to_seconds(end)
        time_log[start_sec] += 1
        time_log[end_sec] -= 1

    for i in range(1, total_play_sec):
        time_log[i] = time_log[i] + time_log[i - 1]

    for i in range(1, total_play_sec + 1):
        time_log[i] = time_log[i] + time_log[i - 1]

    max_view = time_log[total_adv_sec - 1] - time_log[0]
    max_view_start = 0

    for i in range(total_adv_sec, total_play_sec):
        if max_view < time_log[i] - time_log[i - total_adv_sec]:
            max_view = time_log[i] - time_log[i - total_adv_sec]
            max_view_start = i - total_adv_sec + 1

    return seconds_to_time(max_view_start)


play_time = "99:59:59"
adv_time = "25:00:00"
logs = ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"]
print(solution(play_time, adv_time, logs))