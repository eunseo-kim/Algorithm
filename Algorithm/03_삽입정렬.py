# 손 코딩 연습 (3) - 삽입정렬
# 삽입정렬이란? 2번째 원소부터 시작하여 그 앞(왼쪽)의 원소들과 비교하여 삽입할 위치를 지정한 후,
# 원소를 뒤로 옮기고 지정된 자리에 자료를 삽입 하여 정렬하는 알고리즘

# 시간 복잡도 - (최악) (n-1) + (n-2) ... + 1 = n(n-1)/2 = O(n^2) / (최선) O(n)
# 공간 복잡도 - 길이가 n인 배열 내에서 swap = O(1)


def insertion_sort(arr):
    N = len(arr)

    for i in range(1, N):
        for j in range(i, 0, -1):
            if arr[j] >= arr[j - 1]:
                break
            arr[j], arr[j - 1] = arr[j - 1], arr[j]

    return arr


result = insertion_sort([3, 7, 2, 5, 1, 4, 6])
print(result)