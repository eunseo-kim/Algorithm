# 언어 : Python
# 날짜 : 2022.2.11
# 문제 : BOJ > 완전 이진 트리 (https://www.acmicpc.net/problem/9934)
# 티어 : 실버 1
# =========================================================================


def solution(left, mid, right, depth):
    if mid >= length or depth >= K:
        return
    
    answer[depth].append(nodes[mid])

    solution(left, left + (mid - left) // 2, mid - 1, depth + 1)
    solution(mid + 1, mid + 1 + ((right - mid - 1) // 2), right, depth + 1)


K = int(input())
nodes = list(map(int, input().split()))
length = len(nodes)

if length == 1:
    print(nodes[0])
else:
    answer = [[] for _ in range(K)]
    mid = length // 2
    solution(0, mid, length - 1, 0)
    for node in answer:
        print(" ".join(map(str, node)))