def solution(dartResult):
    # [0] initialize
    score_type = {
        "S": 1,
        "D": 2,
        "T": 3,
    }

    score_option = {
        "*": 2,
        "#": -1,
    }

    # [1] 숫자를 기준으로 입력을 나누기
    inputs = []
    curr = []
    for char in dartResult:
        if not char.isdigit():
            curr.append(char)
            continue

        # char이 숫자인 경우
        if len(curr) == 0:  # 첫번째 숫자인 경우
            curr = [int(char)]
            continue

        # 현재 숫자가 10인 경우
        if curr[-1] == 1:
            curr.pop()
            curr = [10]
            continue

        inputs.append(curr)
        curr = [int(char)]
    inputs.append(curr)

    # [2] 점수 계산하기
    total_score = [0 for _ in range(3)]
    for i, input in enumerate(inputs):
        score, type = input[0], input[1]
        curr_score = score ** score_type[type]
        if len(input) == 3:
            option = input[-1]
            curr_score *= score_option[option]

            # '*'인 경우 직전 점수도 2배
            if option == "*" and i > 0:
                total_score[i - 1] *= 2

        total_score[i] = curr_score

    return sum(total_score)


result = solution("1S2D*3T")
print(result)
