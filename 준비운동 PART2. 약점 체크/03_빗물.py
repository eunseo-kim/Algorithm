# 언어 : Python
# 날짜 : 2021.07.14
# 문제 : BOJ > 빗물 (https://www.acmicpc.net/problem/14719)
# 티어 : 골드 5
# ================================================================
# 소요 시간 : -
# 제출 시도 : -
# 오답 이유 : 힌트 보고 풀었음😎 (각 칸에서 양쪽의 최댓값 비교)
# ================================================================


def solution(blocks):
    max_height = [0]
    for idx in range(1, len(blocks) - 1):
        max_height.append(min(max(blocks[:idx]), max(blocks[idx + 1 :])))
    max_height.append(0)

    rainwater = 0
    for idx, block_height in enumerate(blocks):
        if max_height[idx] > block_height:
            rainwater += max_height[idx] - block_height
    return rainwater


row, col = map(int, input().split())
blocks = list(map(int, input().split()))
print(solution(blocks))
