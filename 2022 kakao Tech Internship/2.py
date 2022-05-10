from collections import deque


def solution(queue1, queue2):
    # [1] 큐 원소들의 합 구하기
    target = sum(queue1) + sum(queue2)

    if target % 2 != 0:  # 단, 만약 짝수가 아니면 -1 리턴
        return -1

    target = target // 2

    # [2] 효율성을 위해 deque로 선언
    q1 = deque(queue1)
    q2 = deque(queue2)

    # [3] 만약 처음부터 target 상태라면 return 0
    q1_sum = sum(q1)
    if q1_sum == target:
        return 0

    # [4] queue1, queue2를 pop 하면서 만족하는 경우 찾기
    cnt = 0
    total_turn = 0

    N = len(queue1) + len(queue2)

    # 만약 total_turn이 queue1, queue2 전부 다 돌았는데도 만족하는 경우가 없으면 return -1
    while total_turn <= 2*N:
        # 가장 처음 찾은 경우가 최소 cnt임
        if q1_sum == target:
            return cnt

        elif q1_sum > target: # q1_sum이 target보다 크면 q1에서 pop 해서 q2로 append
            num = q1.popleft()
            q2.append(num)
            q1_sum -= num
        else: # q1_sum이 target보다 작으면 q2에서 pop 해서 q1로 append
            num = q2.popleft() 
            q1.append(num)
            q1_sum += num

        cnt += 1
        total_turn += 1

    return -1


queue1, queue2 = [1, 1, 5], [1, 1, 1]
result = solution(queue1, queue2)
print(result)