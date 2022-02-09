# 언어 : Python
# 날짜 : 2022.2.9
# 문제 : BOJ > 2422번 (https://www.acmicpc.net/problem/2422)
# 티어 : 실버 5
# 시간복잡도 / 1 ≤ N ≤ 200, 0 ≤ M ≤ 10,000
# =========================================================================

from collections import defaultdict


def dfs(curr, path):
    global cnt

    if len(path) == 3:
        cnt += 1
        return

    for next in range(curr + 1, N + 1):
        is_valid = True
        for num in path:
            if next in arr[num]:
                is_valid = False
        if is_valid:
            dfs(next, path + [next])


cnt = 0
N, M = map(int, input().split())
arr = defaultdict(list)
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, N):
    dfs(i, [i])
print(cnt)