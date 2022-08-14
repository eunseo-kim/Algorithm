# 언어 : Python
# 날짜 : 2022.8.14
# 문제 : BOJ > 이중 우선순위 큐 (https://www.acmicpc.net/problem/7662)
# 티어 : 골드 4
# =========================================================================

from collections import defaultdict
import sys
import heapq

input = sys.stdin.readline


class DoublyPriorityQueue:
    def __init__(self):
        self.size = 0
        self.maxheap = []
        self.minheap = []
        self.removed = defaultdict(int)  # maxheap & minheap 동기화 처리

    def get_queue(self):
        if self.size == 0:
            return "EMPTY"

        while self.minheap:
            value = heapq.heappop(self.minheap)
            if self.removed[value] > 0:
                min_num = value
                break

        while self.maxheap:
            value = -(heapq.heappop(self.maxheap))
            if self.removed[value] > 0:
                max_num = value
                break

        return str(max_num) + " " + str(min_num)

    def insert(self, value):
        heapq.heappush(self.minheap, value)
        heapq.heappush(self.maxheap, -1 * value)
        self.removed[value] += 1
        self.size += 1

    def delete(self, code):
        if self.size == 0:
            return

        if code == 1:  # 최솟값 출력
            while self.maxheap:
                value = -1 * heapq.heappop(self.maxheap)
                if self.removed[value] > 0:
                    self.removed[value] -= 1
                    break
        else:  # 최댓값 출력
            while self.minheap:
                value = heapq.heappop(self.minheap)
                if self.removed[value] > 0:
                    self.removed[value] -= 1
                    break
        self.size -= 1


#
for _ in range(int(input())):
    queue = DoublyPriorityQueue()
    for _ in range(int(input())):
        code, number = input().split(" ")
        if code == "I":
            queue.insert(int(number))
        else:
            queue.delete(int(number))
    print(queue.get_queue())