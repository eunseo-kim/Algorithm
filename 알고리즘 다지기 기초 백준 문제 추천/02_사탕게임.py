# 언어 : Python
# 날짜 : 2021.07.20
# 문제 : BOJ > 사탕 게임 (https://www.acmicpc.net/problem/3085)
# 티어 : 실버 4
# ============================================================================
# 소요 시간 : -
# 제출 시도 : -
# 풀이 방법 : [블로그 풀이 참고](https://glowdev.tistory.com/19)
# ============================================================================


def find_max_count(board):
    max_count = 1

    # 행 기준으로 탐색하면서 max_count 구하기
    for row in range(N):
        cur_count = 1
        for col in range(N - 1):
            if board[row][col] == board[row][col + 1]:
                cur_count += 1
            else:
                max_count = max(max_count, cur_count)
                cur_count = 1

        max_count = max(max_count, cur_count)
        if max_count == N:
            return N

    # 열 기준으로 탐색하면서 max_count 구하기
    for col in range(N):
        cur_count = 1
        for row in range(N - 1):
            if board[row][col] == board[row + 1][col]:
                cur_count += 1
            else:
                max_count = max(max_count, cur_count)
                cur_count = 1

        max_count = max(max_count, cur_count)
        if max_count == N:
            return N

    return max_count


def solution(board):
    answer = 1
    # 각 자리 swap 해보면서 find_max_count 구하기
    # 행 내에서 교환
    for row in range(N):
        for col in range(N - 1):
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
            result = find_max_count(board)
            answer = max(answer, result)
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
            if answer == N:
                return answer

    # 열 내에서 교환
    for col in range(N):
        for row in range(N - 1):
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
            result = find_max_count(board)
            answer = max(answer, result)
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
            if answer == N:
                return answer

    return answer


# 입력 및 실행
N = int(input())
board = []
for _ in range(N):
    board.append(list(input()))
print(solution(board))