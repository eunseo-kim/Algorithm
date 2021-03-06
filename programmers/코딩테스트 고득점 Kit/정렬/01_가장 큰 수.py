# 언어 : Python
# 날짜 : 2022.07.05
# 문제 : Programmers > 가장 큰 수
# 티어 : Lv 2
# ==============================================================


def solution(numbers):
    arr = list(map(str, numbers))

    arr.sort(key=lambda x: x * 3, reverse=True)
    # [문제 해결 방법]
    # 각각의 숫자는 '최소 1자리 ~ 최대 3자리수'입니다.
    # 따라서 각 숫자를 문자열로 바꾸고, 숫자를 연속으로 3번 이어 붙인 결과를 비교합니다.
    # 예를 들어서, '2'& '23' & '211'을 비교해봅시다.
    # 예상 가능한 결과는 '232211'입니다. 이를 도출하기 위해서
    # '222'
    # '232323'
    # '211211211'
    # 이 3가지 경우를 비교합니다.
    # 문자열 비교는 앞에서부터 차례대로 진행되며, 앞의 자리 중 더 큰 값이 있으면 우선적으로 정렬됩니다.
    # 따라서 232323 => 222 => 211211211 이 순서대로 정렬되므로
    # 처음에 예상했던대로 '232211'을 얻을 수 있습니다.

    answer = int("".join(map(str, arr)))

    return str(answer)


print(solution([6, 10, 2]))
