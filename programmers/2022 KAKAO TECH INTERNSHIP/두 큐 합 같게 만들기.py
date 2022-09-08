# 17"
from collections import deque


def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)

    len1, len2 = len(queue1), len(queue2)
    sum1, sum2 = sum(queue1), sum(queue2)

    # 예외처리
    if (sum1 + sum2) % 2 != 0:
        return -1

    move_count = 0
    while move_count < (len1 + len2) * 2:
        if sum1 == sum2:
            return move_count  # 정답

        if sum1 > sum2:
            num = queue1.popleft()
            queue2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = queue2.popleft()
            queue1.append(num)
            sum2 -= num
            sum1 += num

        move_count += 1

    return -1


result = solution([1, 1], [1, 5])
print(result)