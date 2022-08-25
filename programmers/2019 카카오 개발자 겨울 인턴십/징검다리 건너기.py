def solution(stones, k):
    start = 1  # 최소로 지나갈 수 있는 사람 수
    end = max(stones)  # 최대로 지나갈 수 있는 사람 수
    answer = end  # 모두 다 지나갈 수 있는 경우로 초기화

    while start <= end:
        mid = (start + end) // 2

        count = 0
        exceed = False
        for stone in stones:
            if stone - mid < 0:
                count += 1
            else:
                count = 0

            if count >= k:
                exceed = True
                break

        if exceed:  # 지나갈 수 있는 사람이 너무 많음
            end = mid - 1
        else:  # 지나갈 수 있는 경우. 그러나 현재의 case가 과연 최솟값인지 검사해봐야 됨
            answer = mid
            start = mid + 1

    return answer


stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
result = solution(stones, k)
print(result)