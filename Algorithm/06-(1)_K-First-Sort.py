# K번째 숫자가 맨 앞으로 오고 나머지 배열을 O(N)에 정렬하여 출력하기


def KFirstSort(arr, k):
    min_num, max_num = min(arr), max(arr)  # O(N)

    number_count = {}
    for num in range(min_num, max_num + 1):
        number_count[num] = 0

    result = []
    for i, num in enumerate(arr):
        if i == k:
            result.append(num)
            continue

        number_count[num] += 1

    for num in range(min_num, max_num + 1):
        for _ in range(number_count[num]):
            result.append(num)

    return result


answer = KFirstSort([1, 3, 5, 2, 4, 6, 7, 8, 5, 3, 4, 1, 10, 2], 1)
print(answer)