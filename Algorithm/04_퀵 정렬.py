# 손 코딩 연습 (4) - 퀵 정렬
# 퀵 정렬이란? 분할정복 알고리즘 / pivot을 기준으로 분할하고 분할한 부분 리스트를 정렬하기

# 시간 복잡도 - (최악)pivot을 항상 최대/최소를 선택한 경우. 즉, 배열이 (역)정렬 되어 있는 경우 => O(n^2)
# ▷           (평균)일반적인 경우에는 O(nlogn) / pivot을 기준으로 분할할수록 정렬해야되는 배열의 크기가 작아짐
# 공간 복잡도 - O(1)


def partition(arr, left, right):
    pivot_index = left
    pivot = arr[left]
    start = left + 1
    end = right

    while start <= end:
        while start <= right and arr[start] < pivot:
            start += 1

        while end >= left and arr[end] > pivot:
            end -= 1

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    arr[end], arr[pivot_index] = arr[pivot_index], arr[end]
    return end


def quick_sort(arr, left, right):
    if left >= right:
        return

    pivot = partition(arr, left, right)

    quick_sort(arr, left, pivot - 1)
    quick_sort(arr, pivot + 1, right)


arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 11, 12, 13, -1, -2, -3]
quick_sort(arr, 0, len(arr) - 1)
print(arr)
