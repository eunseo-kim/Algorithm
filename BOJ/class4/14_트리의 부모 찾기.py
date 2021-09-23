# 언어 : Python
# 날짜 : 2021.09.23
# 문제 : BOJ > 파티 (https://www.acmicpc.net/problem/11725)
# 티어 : 실버 2
# 문제 해결 팁
# visited를 사용할 때 [num in visited] 대신 boolean을 사용하자.
# 전체 크기를 알고 있는 경우, visited[num] 을 사용하는게 더 빠르다(시간초과 발생 X)
# =============================================================================

from collections import defaultdict
import sys


def solution():
    roots = [0 for _ in range(N + 1)]  # 0은 버림
    visited = [False for _ in range(N + 1)]
    visited[1] = True
    queue = [1]

    while queue:
        root = queue.pop(0)
        for n in nodes[root]:
            if not visited[n]:
                visited[n] = True
                roots[n] = root
                queue.append(n)

    for i in range(2, N + 1):
        print(roots[i])


N = int(sys.stdin.readline())
nodes = defaultdict(list)

for _ in range(N - 1):
    u, v = map(int, sys.stdin.readline().split())
    nodes[u].append(v)
    nodes[v].append(u)
solution()