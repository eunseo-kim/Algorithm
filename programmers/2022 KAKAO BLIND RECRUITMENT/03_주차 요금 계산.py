from collections import defaultdict
import math


def time_to_minute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)


def solution(fees, records):
    car_list = set()

    in_cars_stack = defaultdict(list)
    total_time_dict = defaultdict(int)

    for record in records:
        time_stamp, car_number, in_or_out = record.split(" ")

        car_list.add(car_number)

        minutes = time_to_minute(time_stamp)  # int

        if in_or_out == "IN":
            in_cars_stack[car_number].append(minutes)
        else:
            in_time = in_cars_stack[car_number].pop()
            out_time = minutes
            total_used_time = out_time - in_time
            total_time_dict[car_number] += total_used_time

    # 출차 하지 않은 차량의 total time 추가하기
    final_out_time = time_to_minute("23:59")
    for car_number, in_time_stack in in_cars_stack.items():
        if in_time_stack != []:
            in_time = in_time_stack.pop()
            total_used_time = final_out_time - in_time
            total_time_dict[car_number] += total_used_time

    # 차량번호 작은 순서대로 요금 계산하기
    car_list = list(car_list)
    car_list.sort()

    answer = []

    default_time, default_fee, per_time, per_fee = fees
    for car_number in car_list:
        used_time = total_time_dict[car_number]

        if used_time <= default_time:
            answer.append(default_fee)
        else:
            over_time = used_time - default_time
            over_fee = math.ceil(over_time / per_time) * per_fee
            total_fee = default_fee + over_fee
            answer.append(total_fee)

    return answer


fees = [180, 5000, 10, 600]
records = [
    "05:34 5961 IN",
    "06:00 0000 IN",
    "06:34 0000 OUT",
    "07:59 5961 OUT",
    "07:59 0148 IN",
    "18:59 0000 IN",
    "19:09 0148 OUT",
    "22:59 5961 IN",
    "23:00 5961 OUT",
]
result = solution(fees, records)
print(result)