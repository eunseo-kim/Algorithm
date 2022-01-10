# 언어 : Python
# 날짜 : 2022.1.10
# 문제 : BOJ > Strahler 순서(https://www.acmicpc.net/problem/9470)
# 티어 : 골드 3
# ================================================================

from collections import defaultdict
from collections import Counter


def Strahler():
    # [1] 강의 근원 노드 찾기
    is_root = [True for _ in range(M + 1)]
    is_root[0] = False  # 노드 번호는 1부터 시작
    for key in graph:
        for value in graph[key]:
            is_root[value] = False

    strahler = [[0] for _ in range(M + 1)]  # [들어오는 모든 강]
    roots = []
    for i, root in enumerate(is_root):
        if root:
            roots.append([1, i + 1])
            strahler[i] = [1]

    visited = [False for _ in range(M + 1)]

    # [2] 강의 근원 노드로부터 차례대로 들어오는 강 계산
    queue = roots[:]
    while queue:
        num, node = queue.pop(0)
        if not visited[node]:
            visited[node] = True

            # 현재 node의 순서 계산하기
            strahler[node].sort()
            counter = Counter(strahler[node])
            num = max(strahler[node])
            if counter[strahler[node][-1]] >= 2:
                num += 1
            strahler[node] = [num]

            # 다음 노드 탐색
            next_nodes = graph[node]
            for next in next_nodes:
                strahler[next].append(num)

            # 탐색 완료된 근원 노드 삭제하기
            graph[node] = []
            for key in graph:
                for value in graph[key]:
                    if value == node:
                        graph[key].remove(node)

            print("graph:", graph)

            is_root = [True for _ in range(M + 1)]
            is_root[0] = False  # 노드 번호는 1부터 시작
            for key in graph:
                for value in graph[key]:
                    is_root[value] = False

            print("IS_ROOT:", is_root)
            for i, root in enumerate(is_root):
                print(i, root)
                if root and not visited[root]:
                    queue.append([num, i + 1])

            print(node, ">", strahler)
            print("VISITED:", visited)
            print("QUEUE:", queue)
            print()

    # [3] strahler 순서 계산하기
    strahler[M].sort()
    counter = Counter(strahler[M])
    if counter[strahler[M][-1]] >= 2:
        return strahler[M][-1] + 1
    else:
        return strahler[M][-1]


T = int(input())
for _ in range(T):
    graph = defaultdict(list)
    K, M, P = map(int, input().split())
    for _ in range(P):
        A, B = map(int, input().split())
        graph[A].append(B)

    result = Strahler()
    print(K, result)
