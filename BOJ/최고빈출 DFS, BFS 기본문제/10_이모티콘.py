# 언어 : Python
# 날짜 : 2021.08.24
# 문제 : BOJ > 이모티콘 (https://www.acmicpc.net/problem/14226)
# 티어 : 골드 5
# 걸린 시간 :
# ======================================================================
from collections import defaultdict


def solution():
    stack = [[1, 0]]  # 이모티콘 개수, 클립보드
    visited = {}
    visited[(1, 0)] = 0  # [이모티콘 개수, 클립보드] = 최소 시간

    while stack:
        cnt, clip = stack.pop(0)

        if cnt == N:
            return visited[(cnt, clip)]

        # 복사
        if (cnt, cnt) not in visited.keys():
            visited[(cnt, cnt)] = visited[(cnt, clip)] + 1
            stack.append([cnt, cnt])
        # 붙여넣기
        if (cnt + clip, clip) not in visited.keys():
            visited[(cnt + clip, clip)] = visited[(cnt, clip)] + 1
            stack.append([cnt + clip, clip])
        # 삭제
        if cnt - 1 > 0 and (cnt - 1, clip) not in visited.keys():
            visited[(cnt - 1, clip)] = visited[(cnt, clip)] + 1
            stack.append([cnt - 1, clip])


N = int(input())
print(solution())