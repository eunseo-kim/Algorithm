# 손 코딩 연습 (4) - 퀵 정렬
# 퀵 정렬이란? 분할정복 알고리즘 / pivot을 기준으로 분할하고 분할한 부분 리스트를 정렬하기


def partition(arr, left, right):
    pivot = arr[left]
    start = left
    end = right

    while start < end:
        while arr[start] < pivot:
            start += 1

        while arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    arr[end], arr[left] = arr[left], arr[end]
    return end


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot)
    quick_sort(arr, pivot + 1, right)


arr = [3, 7, 2, 5, 1, 4, 6, 10, 8, 11, 0, 9, 9, 0]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
