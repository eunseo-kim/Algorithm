# 언어 : Python
# 날짜 : 2022.07.01
# 문제 : Programmers > 체육복🏃🏻‍♀️
# 티어 : Lv 1
# ==============================================================


def solution(n, lost, reserve):
    # [1] 학생별 count(체육복 개수) 초기화 합니다.
    count = {}
    for student in range(1, n + 1):
        count[student] = 1

    # [2] 학생별 여벌의 체육복 개수를 설정합니다.
    for res in reserve:
        count[res] += 1

    # [3] 학생별 잃어버린 체육복 개수를 설정합니다.
    for los in lost:
        count[los] -= 1

    # [4] 체육복이 없는 학생은 [앞의 학생 => 뒤의 학생] 순으로 체육복을 빌립니다. 앞에서부터 차례대로 빌릴거니까요. (=> 그리디)
    total_count = 0

    for i in range(1, n + 1):
        if count[i] == 0:
            if i - 1 > 0 and count[i - 1] == 2:
                count[i - 1] -= 1
                count[i] = 1
            elif i + 1 <= n and count[i + 1] == 2:
                count[i + 1] -= 1
                count[i] = 1

        # 만약 현재 학생이 체육복이 있으면(빌려서 생겼든 원래 있었든) total_count를 1 추가합니다.
        if count[i] > 0:
            total_count += 1

    return total_count


result = solution(5, [2, 4], [1, 3, 5])
print(result)
