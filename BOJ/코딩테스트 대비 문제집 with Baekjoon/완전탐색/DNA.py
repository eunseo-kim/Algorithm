# 언어 : Python
# 날짜 : 2022.2.1
# 문제 : BOJ > DNA (https://www.acmicpc.net/problem/1969)
# 티어 : 실버 5
# 시간 : 25분 (ㅠㅠ)
# ① HOW - 완전탐색 / 사전순 정렬은 Counter & for문으로 구함
# ② NEW - Counter(iterable)
# - counter.most_common() => (값, 개수)를 most common 순의 리스트로 반환 (단, 사전 순서 X)
# - counter.most_common(1) => 위의 리스트 중 첫번째꺼 리턴 (단, 사전 순서 고려 X)
# ③ 시간복잡도
# - Counter의 most_common => O(nlogn)
# - Counter(iterable) => O(n)
# =========================================================================================

from collections import Counter


def solution():
    result = []
    for i in range(M):
        temp = []
        for dna in dnas:
            temp.append(dna[i])
        counter = Counter(temp)
        common = counter.most_common()
        # 사전순
        common_word = common[0][0]
        max_cnt = common[0][1]
        for key, value in common:
            if max_cnt <= value and key <= common_word:
                common_word = key
                max_cnt = value
        result.append(common_word)
    answer = "".join(map(str, result))

    # calculate hamming distance
    hamming_distance = 0
    for dna in dnas:
        for i in range(M):
            if answer[i] != dna[i]:
                hamming_distance += 1

    return answer, hamming_distance


N, M = map(int, input().split())
dnas = []
for _ in range(N):
    dnas.append(list(input()))
answer, hamming_distance = solution()
print(answer)
print(hamming_distance)