"""
컨베이어 벨트 위의 로봇(https://www.acmicpc.net/problem/20055)
"""


def solution(N, K, belt):
    robots = [False for _ in range(N)]
    grade = 0

    while True:
        grade += 1

        # [1] 벨트와 로봇 모두 한 칸 씩 회전한다.
        last_belt = belt.pop()
        belt = [last_belt] + belt
        last_robot = robots.pop()
        robots = [last_robot] + robots

        robots[-1] = False  # 내리는 칸에 있는 로봇은 무조건 내리기

        # [2] 로봇을 한 칸씩 이동시키기
        for i in range(N - 2, -1, -1):
            if robots[i] and not robots[i + 1] and belt[i + 1] > 0:
                robots[i] = False
                robots[i + 1] = True
                belt[i + 1] -= 1

        robots[-1] = False  # 내리는 칸에 있는 로봇은 무조건 내리기

        # [3] 올리는 칸의 내구도가 0이 아니면 올리기
        if belt[0] > 0 and not robots[0]:
            robots[0] = True
            belt[0] -= 1

        # [4] 만약 내구도가 0인 칸이 K개 이상이면 종료
        cnt = 0
        for b_num in belt:
            if b_num == 0:
                cnt += 1
        if cnt >= K:
            break

    return grade


N, K = map(int, input().split())
A = list(map(int, input().split()))
result = solution(N, K, A)
print(result)
