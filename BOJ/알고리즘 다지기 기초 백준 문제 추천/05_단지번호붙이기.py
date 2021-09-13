# 언어 : Python
# 날짜 : 2021.07.26
# 문제 : BOJ > 단지번호붙이기 (https://www.acmicpc.net/problem/2667)
# 티어 : 실버 1
# ======================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : -
# ======================================================================
def dfs(row, col):
    global count
    if row < 0 or row >= N or col < 0 or col >= N:
        return False
    if board[row][col] == "1":
        count += 1
        board[row][col] = "0"
        dfs(row + 1, col)
        dfs(row - 1, col)
        dfs(row, col + 1)
        dfs(row, col - 1)
        return True


def solution():
    global count
    cnt_list = []

    # 1이면 dfs 실행
    for i in range(N):
        for j in range(N):
            if dfs(i, j):
                cnt_list.append(count)
                count = 0

    return cnt_list


count = 0
N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))
answer = solution()
print(len(answer))
print(" ".join(map(str, sorted(answer))))