# 언어 : Python
# 날짜 : 2022.06.30
# 문제 : Programmers > 순위
# 티어 : Lv 3
# ==============================================================


from collections import defaultdict


def solution(n, computers):
    # [1] 그래프를 만듭니다.
    graph = defaultdict(list)
    for row in range(n):
        for col in range(n):
            if row != col and computers[row][col] == 1:
                graph[row].append(col)
                graph[col].append(row)

    # [2] 연결된 네트워크 개수를 구합니다.
    networks = 0
    visited = [False for _ in range(n)]  # 이미 다른 네트워크에 속한 컴퓨터인지 visited로 판별합니다.

    for computer in range(n):
        if not visited[computer]:
            networks += 1  # 현재 시작 지점이 방문하지 않은 컴퓨터라면 여기에서부터 현재 컴퓨터와 연결된 네트워크를 구해봅니다.
            stack = [computer]

            while stack:
                node = stack.pop()
                if not visited[node]:
                    visited[node] = True

                    children = graph[node]
                    for child in children:
                        if not visited[child]:
                            stack.append(child)

    return networks


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
result = solution(n, computers)
print(result)