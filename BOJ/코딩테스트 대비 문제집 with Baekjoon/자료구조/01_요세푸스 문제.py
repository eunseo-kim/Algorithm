# 언어 : Python
# 날짜 : 2022.2.2
# 문제 : BOJ > 요세푸스 문제 (https://www.acmicpc.net/problem/1158)
# 티어 : 실버 5
# 시간 : 20분
# 시간복잡도
# 1 ≤ K ≤ N ≤ 5,000
# queue.pop(idx) => O(N)
# ============================================================================


def solution():
    idx = -1
    result = []
    while queue:
        idx += K
        idx %= len(queue)
        result.append(queue[idx])
        queue.pop(idx)
        idx -= 1

    return result


N, K = map(int, input().split())
queue = [i for i in range(1, N + 1)]
answer = solution()
print("<" + ", ".join(map(str, answer)) + ">")
