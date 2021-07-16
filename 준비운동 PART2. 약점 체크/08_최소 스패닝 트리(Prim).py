# 언어 : Python
# 날짜 : 2021.07.16
# 문제 : BOJ > 최소 스패닝 트리 (https://www.acmicpc.net/problem/1197)
# 티어 : 골드 4
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : Prim
# ============================================================================
from collections import defaultdict
import heapq


def prim():
    total_weight = 0  # MST 최종 가중치 합
    visited = [False for _ in range(V)]  # 임의로 0번째 node부터 시작
    visited[0] = True
    candidates = edges[0]
    heapq.heapify(candidates)

    while candidates:
        w, u, v = heapq.heappop(candidates)
        if not visited[v]:
            visited[v] = True
            total_weight += w

            for edge in edges[v]:
                if not visited[edge[2]]:
                    heapq.heappush(candidates, edge)
    return total_weight


# 입력 및 실행
V, E = map(int, input().split())
edges = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u - 1].append([w, u - 1, v - 1])
    edges[v - 1].append([w, v - 1, u - 1])
result = prim()
print(result)