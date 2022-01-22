# 언어 : Python
# 날짜 : 2022.1.21
# 문제 : 2020 Kakao Internship > 3. 표 편집
# 티어 : Lv.3
# =========================================================================


def solution(n, k, cmd):
    board = []
    for i in range(n):
        board.append(i)
    back_stack = []
    loc = k
    total_count = n - 1

    for inputs in cmd:
        c = inputs[0]
        if c == "U":
            loc -= int(inputs[2:])
        elif c == "D":
            loc += int(inputs[2:])
        elif c == "C":
            back_stack.append([loc, board[loc]])

            board[total_count] = None
            if loc == total_count:
                loc -= 1
            else:
                board = board[:loc] + board[loc + 1 :]
            total_count -= 1
        else:
            idx, num = back_stack.pop()

            if board[idx] == None:
                board[idx] = num
            else:
                board = board[:idx] + [num] + board[idx : n - 1]
                if loc >= idx:
                    loc += 1
            total_count += 1

    answer = ["X" for _ in range(n)]
    for num in board:
        if num != None:
            answer[num] = "O"

    return "".join(map(str, answer))


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]
print(solution(n, k, cmd))
