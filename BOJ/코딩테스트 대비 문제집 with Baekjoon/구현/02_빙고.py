# 언어 : Python
# 날짜 : 2022.2.4
# 문제 : BOJ > 빙고 (https://www.acmicpc.net/problem/2578)
# 티어 : 실버 5
# 시간 : 25분
# 시간복잡도
# N = 25 / O(N^2)
# ============================================================================


def solution():
    bingo_board = set()
    for num in numbers:
        bingo_board.add(board[num])

        # check if it's bingo
        bingo_count = 0
        for bingo in bingos:
            is_bingo = True
            for num in bingo:
                if num not in bingo_board:
                    is_bingo = False
                    break
            if is_bingo:
                bingo_count += 1
        if bingo_count >= 3:
            break

    return len(bingo_board)


# 입력 및 실행
board = dict()
for i in range(5):
    numbers = list(map(int, input().split()))
    for j, num in enumerate(numbers):
        location = i * 5 + j
        board[num] = location

numbers = []
for _ in range(5):
    numbers += list(map(int, input().split()))

bingos = [
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24],
    [0, 5, 10, 15, 20],
    [1, 6, 11, 16, 21],
    [2, 7, 12, 17, 22],
    [3, 8, 13, 18, 23],
    [4, 9, 15, 19, 24],
    [0, 6, 12, 18, 24],
    [4, 8, 12, 16, 20],
]

print(solution())