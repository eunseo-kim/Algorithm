# 손 코딩 연습 (5) - 병합정렬
# 병합정렬이란? 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음,
# 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법

# 시간 복잡도 - 항상 배열을 쪼갤 수 없을때까지 쪼갠 후 합치는 과정을 거침 - O(nlogn)
# 공간 복잡도 - O(n) / 병합할 결과를 담아 놓을 배열이 추가적으로 필요합니다.


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    result = []
    i, j = 0, 0
    L, R = len(left), len(right)

    while i < L and j < R:
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < L:
        result.append(left[i])
        i += 1

    while j < R:
        result.append(right[j])
        j += 1

    return result


arr = [1, 4, 2, 5, 6, 3, 7, 8, 9, 10, 11, -1, -2, -3, 7]
answer = merge_sort(arr)
print(answer)