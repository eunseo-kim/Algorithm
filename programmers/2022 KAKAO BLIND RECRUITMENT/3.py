import re
import math
from collections import defaultdict


def solution(fees, records):
    MAX_TIME = time_to_min("23:59")
    IN_list = {}
    parking_time = defaultdict(int)
    parking_fee = defaultdict(int)
    for record in records:
        time, car_num, in_or_out = re.split(" ", record)
        time = time_to_min(time)
        if in_or_out == "IN":
            IN_list[car_num] = time
        else:
            parking_time[car_num] += time - IN_list[car_num]
            IN_list[car_num] = None

    for car_num, pf in IN_list.items():
        if pf != None:
            parking_time[car_num] += MAX_TIME - IN_list[car_num]

    answer = []
    for cn, pt in sorted(parking_time.items()):
        answer.append(calculate_fee(pt, fees))

    return answer


def time_to_min(time):  # 10:24 => min
    hour, min = list(map(int, re.split(":", time)))
    return hour * 60 + min


def calculate_fee(parking_time, fees):
    if parking_time <= fees[0]:
        return fees[1]
    return fees[1] + math.ceil((parking_time - fees[0]) / fees[2]) * fees[3]


# fees = [180, 5000, 10, 600]
# records = [
#     "05:34 5961 IN",
#     "06:00 0000 IN",
#     "06:34 0000 OUT",
#     "07:59 5961 OUT",
#     "07:59 0148 IN",
#     "18:59 0000 IN",
#     "19:09 0148 OUT",
#     "22:59 5961 IN",
#     "23:00 5961 OUT",
# ]


# fees = [120, 0, 60, 591]
# records = ["16:00 3961 IN", "16:00 0202 IN", "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"]
# print(time_to_min("05:34"))

fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]

solution(fees, records)


# t: 2'