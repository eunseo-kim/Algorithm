# 손 코딩 연습 (2) - 선택정렬
# 선택 정렬이란? 주어진 리스트 중에 최소값을 선택하여 교체한다.

# 시간 복잡도 - n + (n-1) + (n-2) ... + 1 = n(n-1)/2 = O(n^2)
# 공간 복잡도 - 길이가 n인 배열 내에서 swap = O(1)


def selection_sort(arr):
    N = len(arr)
    for i in range(0, N):
        min_index = i
        for j in range(i, N):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


arr = [5, 4, 3, 2, 1, 10, 6, 8, 7, 9]
result = selection_sort(arr)
print(result)