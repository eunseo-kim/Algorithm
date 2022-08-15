# 언어 : Python
# 날짜 : 2022.8.15
# 문제 : BOJ > 수들의 합 4 (https://www.acmicpc.net/problem/2015)
# 티어 : 골드 4
# 고민 : 숫자에 음수도 포함되어 있어서 투포인터로 풀기 어려운 문제인 것 같다.
# 누적합의 성질을 이용해서 풀 수 있는 문제
# =========================================================================

from collections import defaultdict
import sys

input = sys.stdin.readline


def solution():
    answer = 0

    # [1] 누적합을 구합니다.
    prefix_sum = [0 for _ in range(N + 1)]
    prefix_dict = defaultdict(int)

    for i in range(N):
        prefix_sum[i] = prefix_sum[i - 1] + A[i]

        # [2] 누적합에서 prefix_sum[i]=K(0~i까지의 부분합이 K)라면 정답입니다.
        if prefix_sum[i] == K:
            answer += 1

        # [3] 만약 prefix_sum[i]-K를 key로 갖는 prefix_dict가 존재하면 prefix_dict[prefix_sum[i]-K]의 value만큼도 정답입니다.
        # 왜냐하면 이는 j(=누적합이 prefix_sum[i]-K를 만족하는 인덱스)부터 i(=현재 인덱스)까지의 부분합이 K가 된다는 의미이기 때문이에요.
        answer += prefix_dict[prefix_sum[i] - K]

        prefix_dict[prefix_sum[i]] += 1

    return answer


N, K = map(int, input().split(" "))
A = list(map(int, input().split(" ")))
result = solution()
print(result)
