# 언어 : Python
# 날짜 : 2022.3.10
# 문제 : 정렬된 리스트 3개가 주어졌을때 리스트에 존재하는 값을 찾아 출력하기
# 티어 : 실버 3
# ===========================================================================


def solution():
    idx1, idx2, idx3 = 0, 0, 0
    answer = []
    while True:
        if list1[idx1] == None or list2[idx2] == None or list3[idx3] == None:
            break

        if list1[idx1] == list2[idx2] == list3[idx3]:
            answer.append(list1[idx1])
            idx1 += 1
            idx2 += 1
            idx3 += 1
        else:
            min_num = min(list1[idx1], list2[idx2], list3[idx3])
            if list1[idx1] == min_num:
                idx1 += 1
            if list2[idx2] == min_num:
                idx2 += 1
            if list3[idx3] == min_num:
                idx3 += 1

    print(answer)


list1 = list(map(int, input().split())) + [None]
list2 = list(map(int, input().split())) + [None]
list3 = list(map(int, input().split())) + [None]
solution()