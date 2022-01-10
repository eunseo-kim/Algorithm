# 언어 : Python
# 날짜 : 2022.1.10
# 문제 : BOJ > Strahler 순서(https://www.acmicpc.net/problem/9470)
# 티어 : 골드 3
# - 위상정렬 문제 (위상정렬 참고 blog: https://freedeveloper.tistory.com/390)
# - 파이썬 알고리즘 인터뷰 p.417 (단계별 리프 노드 제거) 참고
# =========================================================================

from collections import defaultdict
from collections import Counter


def get_leaves(graph, visited):
    leaves = []
    is_leave = [True for _ in range(M)]
    for key in graph:
        for node in graph[key]:
            is_leave[node] = False

    for leaf, is_leaf in enumerate(is_leave):
        if is_leaf and not visited[leaf]:
            leaves.append(leaf)

    return leaves


def Strahler():
    visited = [False for _ in range(M)]

    # 초기 리프 노드(근원 노드)들 추가
    leaves = get_leaves(graph, visited)
    strahler = [[] for _ in range(M)]
    for leaf in leaves:
        strahler[leaf] = [1]

    while leaves:
        for leaf in leaves:
            if not visited[leaf]:
                visited[leaf] = True

                # 현재 탐색하는 노드의 순서번호 결정하기
                seq_num = max(strahler[leaf])
                counter = Counter(strahler[leaf])
                if counter[seq_num] >= 2:
                    seq_num += 1
                strahler[leaf] = [seq_num]

                # 이웃 노드들에게 현재 탐색 노드의 순서번호 전달하기
                neighbors = graph[leaf]
                for neighbor in neighbors:
                    strahler[neighbor].append(seq_num)
                graph[leaf] = []

        leaves = get_leaves(graph, visited)

    return strahler[M - 1][0]


# 입력 및 실행
T = int(input())
for _ in range(T):
    graph = defaultdict(list)
    K, M, P = map(int, input().split())
    for _ in range(P):
        A, B = map(int, input().split())
        graph[A - 1].append(B - 1)

    result = Strahler()
    print(K, result)