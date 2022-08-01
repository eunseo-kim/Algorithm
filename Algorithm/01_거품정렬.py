# 손 코딩 연습 (1) - 거품정렬
# 거품 정렬이란? 서로 인접한 두 원소의 대소를 비교하고
# 조건에 맞지 않다면 자리를 교환하며 정렬하는 알고리즘

# 시간 복잡도 - n + (n-1) + (n-2) + (n-3) ... + 1 = n(n-1)/2 = O(n^2)
# 공간 복잡도 - 길이 n인 배열 내에서 swap을 통해 정렬을 시키므로 O(n)


def bubble_sort(arr):
    N = len(arr)

    for i in range(N - 1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


arr = [5, 4, 3, 2, 1, 10, 6, 8, 7, 9]
result = bubble_sort(arr)
print(result)