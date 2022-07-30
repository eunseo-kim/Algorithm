# 언어 : Python
# 날짜 : 2022.7.30
# 문제 : BOJ > 가장 긴 짝수 연속한 부분 수열 (small)
# (https://www.acmicpc.net/problem/22857)
# 티어 : 실버 3
# =================================================================


def solution():
    # K개를 삭제한 문자열 중 최대 짝수 문자열의 길이
    # == 홀수를 K개만 포함하고 있는 최대 문자열의 길이

    odd = 0  # 홀수 개수
    size = 0  # 부분 문자열의 길이
    max_size = 0 # 최대 부분 문자열의 길이
    
    left, right = 0, 0

    while left <= right and right < N:
        if odd > K:
            if arr[left] % 2 == 1:
                odd -= 1
            left += 1
            size -= 1

        if arr[right] % 2 == 1:
            odd += 1

        right += 1
        size += 1
        max_size = max(max_size, size - odd)  # → odd를 K만큼 전부 다 안 사용할 수 있음을 유의!

    return max_size


N, K = map(int, input().split(" "))
arr = list(map(int, input().split(" ")))
result = solution()
print(result)