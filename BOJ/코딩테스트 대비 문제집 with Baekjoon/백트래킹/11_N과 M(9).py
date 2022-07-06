# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (9) (https://www.acmicpc.net/problem/15663)
# 티어 : 실버 2
# =================================================================


def dfs(path):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    # Q. 주어진 배열에서 중복되는 값이 존재할 때, '각 수열들 간의 중복'은 어떻게 고려할 수 있을까요?

    # last_called는 백트래킹되어 다시 부모로 돌아왔을때, 이전에 방문한 자식 '값'과 앞으로 방문할 자식 '값'을 비교하여
    # 이전에 방문한 자식 경로와 똑같은 경로를 또 다시 방문하지 않도록 중복을 막아줍니다.

    # 단, last_called는 수열 내 중복되는 값이 있을때만 의미가 있습니다.
    # 예를 들어서 M = 3, 배열이 [1, 2, 3, 4]라면 굳이 last_called 조건을 추가하지 않아도 괜찮습니다.
    
    # 하지만, [1, 1, 1, 1] 과 같은 경우, last_called를 추가하지 않으면 수열들 간의 중복을 검사할 수 없게 됩니다.
    last_called = None

    for i in range(N):
        if not visited[i] and last_called != arr[i]:
            last_called = arr[i]
            visited[i] = True
            dfs(path + [arr[i]])
            visited[i] = False


N, M = map(int, input().split(" "))
visited = [False for _ in range(N)]
arr = sorted(list(map(int, input().split(" "))))
dfs([])
