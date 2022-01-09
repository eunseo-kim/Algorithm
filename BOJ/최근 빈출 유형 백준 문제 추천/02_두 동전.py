# 언어 : Python
# 날짜 : 2022.1.8
# 문제 : BOJ > 두 동전(https://www.acmicpc.net/problem/16197)
# 티어 : 골드 4
# 삽질 이유
# - 동전 2개의 조합의 중복여부를 왜 체크해야 하는가?
# - 동전 2개의 조합이 이전의 경우와 중복된다는 것은 '최소' 조건에 위배되는 것!
# - 따라서 조합이 중복 되지 않는 동전조합을 board(4차원 배열)로 체크해야 된다.
# - 단순히 시간초과의 문제만이 아니라 답의 정확성에도 영향을 미치므로 무조건 체크!
# ====================================================================================

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)] 


def is_out(row, col):
    if 0 <= row < R and 0 <= col < C:
        return False
    return True


def solution():
    c1, c2 = coins
    board = [[[[-1 for _ in range(C)] for _ in range(R)] for _ in range(C)] for _ in range(R)]
    board[c1[0]][c1[1]][c2[0]][c2[1]] = 1
    queue = [[c1[0], c1[1], c2[0], c2[1]]]

    while queue:
        r1, c1, r2, c2 = queue.pop(0)

        if board[r1][c1][r2][c2] > 10:
            return -1

        for r, c in moves:
            new_r1 = r1 + r
            new_c1 = c1 + c
            new_r2 = r2 + r
            new_c2 = c2 + c
            out_num = 0

            if is_out(new_r1, new_c1):
                out_num += 1
            else:
                if graph[new_r1][new_c1] == "#":
                    new_r1 = r1
                    new_c1 = c1

            if is_out(new_r2, new_c2):
                out_num += 1
            else:
                if graph[new_r2][new_c2] == "#":
                    new_r2 = r2
                    new_c2 = c2

            if out_num == 1:
                return board[r1][c1][r2][c2]
            elif out_num == 2:
                continue
            elif board[new_r1][new_c1][new_r2][new_c2] == -1:
                board[new_r1][new_c1][new_r2][new_c2] = board[r1][c1][r2][c2] + 1
                queue.append([new_r1, new_c1, new_r2, new_c2])

    return -1


##
R, C = map(int, input().split())
graph = [[] for _ in range(R)]
coins = []
for row in range(R):
    for col, s in enumerate(list(input())):
        graph[row].append(s)
        if s == "o":
            coins.append([row, col])

print(solution())