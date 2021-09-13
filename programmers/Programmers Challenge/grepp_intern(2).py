# 2번 : 1/10 통과...ㅋㅋ

# ===================== 틀린 이유 =====================
# re.match로 입력 형태의 유효성을 먼저 검사해주지 않았다ㅠㅠㅠ
# ex = "3285-3764-9934-2453"
# case1 = re.match(r"\d\d\d\d\d\d\d\d\d\d\d\d", ex)
# case2 = re.match(r"\d\d\d\d\-\d\d\d\d\-\d\d\d\d\-\d\d\d\d", ex)
# print(bool(case1), bool(case2))


import re


def calculate_sum(numbers):
    nums_length = len(numbers)
    mark = [0 for _ in range(nums_length)]

    idx = 0
    while idx < nums_length:
        # 홀수번째
        if idx % 2 == 0:
            mark[idx] = numbers[idx]
        else:  # 짝수 번째
            add_num = numbers[idx] * 2
            if numbers[idx] * 2 >= 10:
                add_num = sum(list(map(int, str(numbers[idx] * 2))))
            mark[idx] = add_num

        idx += 1

    return sum(mark)


def solution(card_numbers):
    answer = []
    for card in card_numbers:
        # 1. 입력 형태의 유효성 검사(이부분 빼먹음)
        check1 = re.match(r"\d\d\d\d\d\d\d\d\d\d\d\d", card)
        check2 = re.match(r"\d\d\d\d\-\d\d\d\d\-\d\d\d\d\-\d\d\d\d", card)
        if not check1 and not check2:
            answer.append(0)
            continue
        else:  # 2. (1) + (2)의 합 유효성 검사
            numbers = []
            for num in str(card):
                if num != "-":
                    numbers.append(int(num))
            sum = calculate_sum(numbers[::-1])

            answer.append(int(sum % 10 == 0))

    return answer


# test case
card_numbers = [
    "3285-3764-9934-2453",
    "3285376499342453",
    "3285-3764-99342453",
    "328537649934245",
    "3285376499342459",
    "3285-3764-9934-2452",
]
print(solution(card_numbers))
