# dp

from collections import deque


def solution(money, costs):
    money_dict = {0: 1, 1: 5, 2: 10, 3: 50, 4: 100, 5: 500}
    queue = deque()
    queue.append([money, 0])
    cost_dp = [float("inf") for _ in range(money + 1)]
    cost_dp[money] = 0

    while queue:
        curr_money, curr_cost = queue.popleft()
        for i in range(6):
            new_money = curr_money - money_dict[i]
            new_cost = curr_cost + costs[i]
            if new_money >= 0:
                if cost_dp[new_money] > new_cost:
                    cost_dp[new_money] = new_cost
                    queue.append([new_money, new_cost])

    return cost_dp[0]


money = 100
costs = [1, 4, 99, 35, 50, 1000]
# money = 1999
# costs = [2, 11, 20, 100, 200, 600]
result = solution(money, costs)
print(result)