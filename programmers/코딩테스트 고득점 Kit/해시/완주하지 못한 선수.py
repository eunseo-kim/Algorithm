# 언어 : Python
# 날짜 : 2022.1.7
# 문제 : programmers > 완주하지 못한 선수
# 티어 : Level 1
# =====================================================================

def solution(participant, completion):
    names = dict()
    hash_sum = 0

    for name in participant:
        names[hash(name)] = name
        hash_sum += int(hash(name))

    for name in completion:
        hash_sum -= int(hash(name))
        
    return names[hash_sum]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
ans = solution(participant, completion)
print(ans)