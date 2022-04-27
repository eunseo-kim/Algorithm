def solution(numbers, hand):
    left_numbers = [1, 4, 7]
    right_numbers = [3, 6, 9]
    phone = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        "*": [3, 0],
        0: [3, 1],
        "#": [3, 2],
    }

    left_hand = phone["*"]
    right_hand = phone["#"]
    answer = []

    for number in numbers:
        number_location = phone[number]
        if number in left_numbers:
            answer.append("L")
            left_hand = number_location
        elif number in right_numbers:
            answer.append("R")
            right_hand = number_location
        else:
            left_distance = abs(left_hand[0] - number_location[0]) + abs(left_hand[1] - number_location[1])
            right_distance = abs(right_hand[0] - number_location[0]) + abs(right_hand[1] - number_location[1])
            print(left_distance, right_distance)
            if left_distance == right_distance:
                if hand == "right":
                    right_hand = number_location
                    answer.append("R")
                else:
                    left_hand = number_location
                    answer.append("L")
            elif left_distance > right_distance:
                right_hand = number_location
                answer.append("R")
            else:
                left_hand = number_location
                answer.append("L")

    return "".join(map(str, answer))


numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
result = solution(numbers, hand)
print(result)