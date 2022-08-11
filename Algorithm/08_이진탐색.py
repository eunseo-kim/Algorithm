def binary_search(arr, key):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == key:
            return mid

        if arr[mid] > key:
            right = mid - 1
        else:
            left = mid + 1

    return "None!"


result = binary_search([1, 2, 4, 5, 7, 8, 9, 11, 13, 15], 13)
print(result)


def lower_bound(arr, key):  # 최소 위치를 찾기
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] >= key:  # key보다 크거나 같으면 '얘가 과연 최소 위치'인지 재 검증
            right = mid
        else:
            left = mid + 1

    return left


def upper_bound(arr, key):  # 최대 위치를 찾기
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        if arr[mid] <= key:  # key보다 작거나 같은 것은 필요 없음. 처음으로 초과하는 위치
            left = mid + 1
        else:
            right = mid

    return left


result = lower_bound([1, 2, 4, 5, 7, 8, 9, 11, 13, 13, 13, 13, 15], 13)
print(result)

result = upper_bound([1, 2, 4, 5, 7, 8, 9, 11, 13, 13, 13, 13, 15], 13)
print(result)
