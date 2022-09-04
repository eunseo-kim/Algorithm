from collections import defaultdict
import math


IN = "IN"
OUT = "OUT"
FINAL_OUT_TIME = "23:59"

IN_cars = {}
used_time_records = defaultdict(int)  # 차량 번호 : 사용 시간


def record_IN_cars(car_number, IN_time):
    IN_cars[car_number] = IN_time


def time_in_minutes(time):
    hour, minutes = map(int, time.split(":"))
    return hour * 60 + minutes


def get_total_fee(used_time, fees):
    default_time, default_fee, additional_time, additional_fee = fees
    if used_time <= default_time:
        return default_fee

    additional_used_time = used_time - default_time
    additional_used_fee = math.ceil(additional_used_time / additional_time) * additional_fee
    return default_fee + additional_used_fee


def solution(fees, records):
    cars = set()

    # [1] 차량별 입차 시간 기록
    for record in records:
        time, car_number, option = record.split(" ")
        cars.add(car_number)
        time = time_in_minutes(time)
        if option == IN:
            record_IN_cars(car_number, time)
        else:
            # [2] 차량별 출차 시간에 따른 사용 시간 기록
            used_time = time - IN_cars[car_number]
            used_time_records[car_number] += used_time
            # [3] 차량 입차 시간 삭제
            IN_cars.pop(car_number)

    # [4] 출차 하지 않은 차들 출차 처리
    out_time = time_in_minutes(FINAL_OUT_TIME)
    for car_number in IN_cars.keys():
        if IN_cars[car_number] >= 0:
            used_time = out_time - IN_cars[car_number]
            used_time_records[car_number] += used_time

    # [5] 차량별 요금 계산
    answer = []
    cars = sorted(cars)
    for car_number in cars:
        total_used_time = used_time_records[car_number]
        total_used_fee = get_total_fee(total_used_time, fees)
        answer.append(total_used_fee)

    return answer


fees = [1, 461, 1, 10]
records = ["00:00 1234 IN"]
result = solution(fees, records)
print(result)