# 언어 : Python
# 날짜 : 2021.07.17
# 문제 : BOJ > 줄 세우기 (https://www.acmicpc.net/problem/2252)
# 티어 : 골드 2
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : 위상 정렬
# 참고 - https://velog.io/@piopiop/위상정렬Topology-Sort-파이썬
# ============================================================================
# 1. 진입하는 노드를 가지고 있지 않은 (가장자리) 노드들을 stack에 넣는다.
# 2. 진입 차수가 0인 노드가 가리키는 노드(target)로 이동한다.
# target의 진입차수는 1 줄어들고, 이전 간선은 제거한다.
# 만약 target의 진입차수가 0이 되었다면 stack에 다시 넣는다.


def topological_sort():
    # 1
    stack = []
    for node in range(N):
        if degree[node] == 0:
            stack.append(node)

    # 2
    result = []
    while stack:
        target = stack.pop()
        result.append(target + 1)  # -1 한거 원래대로 되돌려 놓기 위해 +1 해줌
        for node in graph[target]:
            degree[node] -= 1
            if degree[node] == 0:
                stack.append(node)

    return result


# 입력 및 실행
N, M = map(int, input().split())
degree = [0 for _ in range(N)]  # 진입 차수
graph = [[] for _ in range(N)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u - 1].append(v - 1)
    degree[v - 1] += 1
answer = topological_sort()
print(" ".join(map(str, answer)))
