def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solution(numbers, hand):
    answer = ""

    keyboard = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    }

    left = [3, 0]
    right = [3, 2]

    for number in numbers:
        key = keyboard[number]

        if number in [1, 4, 7]:
            answer += "L"
            left = key
            continue

        if number in [3, 6, 9]:
            answer += "R"
            right = key
            continue

        left_distance = get_distance(left[0], left[1], key[0], key[1])
        right_distance = get_distance(right[0], right[1], key[0], key[1])

        if left_distance == right_distance:
            if hand == "right":
                answer += "R"
                right = key
            else:
                answer += "L"
                left = key
            continue

        if left_distance < right_distance:
            answer += "L"
            left = key
        else:
            answer += "R"
            right = key

    return answer


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers, hand)
print(result)