def time_to_sec(time):
    h, m, s = time.split(":")
    sec = int(h) * 3600 + int(m) * 60 + int(s)
    return sec


def sec_to_time(sec):
    h = str(sec // 3600).zfill(2)
    sec %= 3600
    m = str(sec // 60).zfill(2)
    sec %= 60
    s = str(sec).zfill(2)
    return f"{h}:{m}:{s}"


def solution(play_time, adv_time, logs):
    log_in_seconds = []

    # 1. 해당 시간에서의 동시 접속자 수 구하기
    end_time = time_to_sec(play_time)
    adv_time = time_to_sec(adv_time)

    p_sum = [0 for _ in range(end_time + 1)]
    for log in logs:
        start, end = log.split("-")
        start = time_to_sec(start)
        end = time_to_sec(end)
        log_in_seconds.append(start)
        p_sum[start] += 1
        if end + 1 > end_time:
            continue
        p_sum[end] -= 1

    for i in range(2, end_time + 1):
        p_sum[i] += p_sum[i - 1]

    # 2. 누적 접속자수 구하기
    for i in range(2, end_time + 1):
        p_sum[i] += p_sum[i - 1]

    # 3. 동시 접속자가 가장 많은 구간 탐색
    result = 0
    max_play_time = p_sum[adv_time - 1]
    log_in_seconds.sort()

    for i in range(end_time):
        if i + adv_time <= end_time:
            curr_play_time = p_sum[i + adv_time] - p_sum[i]
            if max_play_time < curr_play_time:
                max_play_time = curr_play_time
                result = i + 1

    return sec_to_time(result)


result = solution(
    "02:03:55",
    "00:14:15",
    [
        "01:20:15-01:45:14",
        "00:25:50-00:48:29",
        "00:40:31-01:00:00",
        "01:37:44-02:02:30",
        "01:30:59-01:53:29",
    ],
)
print(result)
