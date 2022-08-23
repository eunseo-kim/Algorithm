from collections import defaultdict


def solution():
    virus_count = 0
    arr = [target]
    visited = set()

    while arr:
        curr = arr.pop()
        if curr not in visited:
            visited.add(curr)
            virus_count += 1

            for e in edges[curr]:
                if e not in visited:
                    arr.append(e)

    return virus_count - 1


N = int(input())
K = int(input())
target = 1
edges = defaultdict(list)
for _ in range(K):
    a, b = map(int, input().split(" "))
    edges[a].append(b)
    edges[b].append(a)
result = solution()
print(result)