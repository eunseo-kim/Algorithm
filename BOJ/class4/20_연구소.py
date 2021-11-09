# 언어 : Python
# 날짜 : 2021.11.09
# 문제 : BOJ > 연구소(https://www.acmicpc.net/problem/14502)
# 티어 : 골드 5
# =====================================================================
import copy

move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
max_safe_count = 0

# 해결 방법 : 브루트 포스 + 그래프
def dfs(cnt):  # 현재 board, 현재 row/col, 지금까지 사용한 벽의 개수
    global max_safe_count
    global board
    global visited

    if cnt == 0:
        safe_count = solution(board)
        max_safe_count = max(max_safe_count, safe_count)
    else:
        for r in range(row):
            for c in range(col):
                if not visited[r][c] and board[r][c] == 0:
                    board[r][c] = 1
                    visited[r][c] = True
                    dfs(r, c, cnt - 1)
                    board[r][c] = 0
                    visited[r][c] = False


def solution(board):
    virus = copy.deepcopy(board)  # deepcopy 안해줘서 계속 오류가ㅠㅠㅠ
    for r in range(row):
        for c in range(col):
            # 바이러스 찾으면 BFS로 바이러스 감염시키기
            if virus[r][c] == 2:
                queue = [[r, c]]
                while queue:
                    R, C = queue.pop(0)
                    for mr, mc in move:
                        new_row = R + mr
                        new_col = C + mc
                        if 0 <= new_row < row and 0 <= new_col < col:

                            if virus[new_row][new_col] == 0:
                                virus[new_row][new_col] = 2
                                queue.append([new_row, new_col])
    # 모두 감염시키면 0의 개수 구하기
    safe_count = 0
    for r in range(row):
        for c in range(col):
            if virus[r][c] == 0:
                safe_count += 1

    return safe_count


# 입력 및 실행
row, col = map(int, input().split())
board = []
visited = [[False for _ in range(col)] for _ in range(row)]
for _ in range(row):
    board.append(list(map(int, input().split())))

wall_count = 3
dfs(wall_count)
print(max_safe_count)