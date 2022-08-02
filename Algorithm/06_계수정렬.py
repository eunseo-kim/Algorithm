# 손 코딩 연습 (5) - 병합정렬
# 병합정렬이란? 하나의 리스트를 두 개의 균등한 크기로 분할하고 분할된 부분 리스트를 정렬한 다음,
# 두 개의 정렬된 부분 리스트를 합하여 전체가 정렬된 리스트가 되게 하는 방법

# 시간 복잡도 - O(n + k) / k = max number of array
# 공간 복잡도 - O(k) / 병합할 결과를 담아 놓을 배열이 추가적으로 필요합니다.


def counting_sort(arr):
    max_num = max(arr)
    count = [0 for _ in range(max_num + 1)]
    answer = [0 for _ in range(len(arr))]

    for num in arr:
        count[num] += 1

    for i in range(1, max_num + 1):
        count[i] = count[i] + count[i - 1]

    for i in range(len(arr)):
        count[arr[i]] -= 1
        answer[count[arr[i]]] = arr[i]

    return answer


print(counting_sort([1, 2, 4, 5, 5, 6, 2, 7, 7, 4, 10, 22, 2, 3, 4]))