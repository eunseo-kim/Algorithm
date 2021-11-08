# 언어 : Python
# 날짜 : 2021.11.08
# 문제 : BOJ > 이진 검색 트리 (https://www.acmicpc.net/problem/5639)
# 티어 : 실버 1
# =====================================================================
import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(arr):
    length = len(arr)

    if length <= 1:
        return arr

    curr = arr[0]
    for i in range(1, length):
        if arr[i] > curr:
            return dfs(arr[1:i]) + dfs(arr[i:]) + [curr]  # right tree 존재하는 경우

    return dfs(arr[1:]) + [curr]  # 전부 left tree인 경우


# 입력 및 실행
arr = []
while True:
    try:
        arr.append(int(input()))
    except:
        break

arr = dfs(arr)
for n in arr:
    print(n)