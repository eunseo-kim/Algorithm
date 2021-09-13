# 언어 : Python
# 날짜 : 2021.07.15
# 문제 : BOJ > 멀티탭 스케줄링 (https://www.acmicpc.net/problem/1700)
# 티어 : 골드 1
# ================================================================
# 소요 시간 : -
# 제출 시도 : -
# 오답 원인 : if idx >= N:으로 잘못 작성했다.
# 꼭 idx가 N을 넘었다고 멀티탭이 다 차는 건 아니다.
# ================================================================


def solution():
    multitap = []
    unplug_count = 0
    for idx, plug in enumerate(plugs):
        if plug not in multitap:
            if len(multitap) >= N:
                unplug = unplug_from_multitap(multitap[:], plugs[idx:])
                multitap.remove(unplug)
                unplug_count += 1
            multitap.append(plug)
    return unplug_count


def unplug_from_multitap(multitap, plugs):  # 남아있는 플러그 = 최근에 필요하지 않을 플러그 남은 것들
    for plug in plugs:
        if plug in multitap:
            multitap.remove(plug)
        if len(multitap) == 1:
            break
    return multitap[0]  # 남아있는 플러그들 중 맨 앞에 것 빼기


# 입력 및 실행
N, K = map(int, input().split())
plugs = list(map(int, input().split()))
answer = solution()
print(answer)