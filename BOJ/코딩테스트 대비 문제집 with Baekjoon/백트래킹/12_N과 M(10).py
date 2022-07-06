# 언어 : Python
# 날짜 : 2022.7.6
# 문제 : BOJ > N과 M (10) (https://www.acmicpc.net/problem/15664)
# 티어 : 실버 2
# 참고 : N과 M(9)와 풀이 방법이 거의 비슷합니다. last_called를 사용해야 합니다.
# =========================================================================


def dfs(path, i):
    if len(path) == M:
        print(" ".join(map(str, path)))
        return

    last_called = None

    for idx in range(i, N):
        if not visited[idx] and last_called != arr[idx]:
            last_called = arr[idx]
            visited[idx] = True
            dfs(path + [arr[idx]], idx)
            visited[idx] = False


N, M = map(int, input().split(" "))
visited = [False for _ in range(N)]
arr = sorted(list(map(int, input().split(" "))))
dfs([], 0)