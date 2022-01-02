# 언어 : Python
# 날짜 : 2022.1.3
# 문제 : BOJ > 알파벳 (https://www.acmicpc.net/problem/1987)
# 티어 : 골드 4
# 풀이 : dfs
# - 시간초과 왜 났을까 -_-
# 시도 1) path를 매번 인자로 전달해서 복사하는 방법
# => list를 매번 새로 복사해서 너무 느리다.
# 시도 2) ord로 index를 구한 뒤 visited[26]를 False로 초기화해서 검사
# => visited를 boolean으로 판단하는게 빠를 줄 알았는데 ord가 생각보다 느린 듯?
# 시도 3) visited를 set()으로 바꿔봄
# => x in list는 O(N)인데 x in set은 O(1)이라고 한다.
# => 시간초과 해결😀!
# =====================================================================

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def dfs(row, col, count):
    global max_count
    for i in range(4):
        nr, nc = row + move[i][0], col + move[i][1]
        if 0 <= nr < R and 0 <= nc < C and not board[nr][nc] in visited:
            visited.add(board[nr][nc])
            dfs(nr, nc, count + 1)
            visited.remove(board[nr][nc])

    max_count = max(max_count, count)


# 입력 및 실행
R, C = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input()))

start = board[0][0]
max_count = 1
visited = set()
visited.add(start)

dfs(0, 0, 1)
print(max_count)
