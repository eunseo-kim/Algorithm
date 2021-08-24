# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 미로 찾기 (https://www.acmicpc.net/problem/16953)
# 티어 : 실버 1
# ======================================================================
import heapq


def solution():
    queue = [[A, 1]]
    count = 0
    while queue:
        node = heapq.heappop(queue)
        cur_num = node[0]
        cur_cnt = node[1]
        if cur_num == B:
            count = cur_cnt
            break
        elif cur_num > B:
            break

        heapq.heappush(queue, [cur_num * 2, cur_cnt + 1])
        heapq.heappush(queue, [int(str(cur_num) + "1"), cur_cnt + 1])

    print(count) if count != 0 else print(-1)


A, B = map(int, input().split())
solution()