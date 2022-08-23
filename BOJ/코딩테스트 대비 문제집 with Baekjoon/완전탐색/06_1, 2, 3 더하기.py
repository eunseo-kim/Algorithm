def solution(number):
    global count

    if number == 0:
        count += 1
        return

    for i in range(1, 4):
        if number >= i:
            solution(number - i)


N = int(input())
for _ in range(N):
    count = 0
    solution(int(input()))
    print(count)