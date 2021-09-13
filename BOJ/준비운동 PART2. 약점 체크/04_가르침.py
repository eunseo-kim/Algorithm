# 언어 : Python
# 날짜 : 2021.07.15
# 문제 : BOJ > 가르침 (https://www.acmicpc.net/problem/1062)
# 티어 : 골드 4
# ================================================================
# 소요 시간 : -
# 제출 시도 : -
# 오답 이유 : 다른 블로그 풀이 참고
# ================================================================


def dfs(idx, cnt, words, candidates, visited):
    global answer
    if cnt == K:  # 최대 K개를 모두 가르친 경우
        cur_count = 0
        for word in words:  # 각 word를 순회하면서 visited에 word의 letter이 모두 있는지 확인
            is_valid = True
            for letter in word:
                if letter not in visited:
                    is_valid = False
                    break
            if is_valid:
                cur_count += 1

        answer = max(answer, cur_count)
        return

    for i in range(idx, len(candidates)):
        if candidates[i] not in visited:
            dfs(i + 1, cnt + 1, words, candidates, visited + [candidates[i]])


def solution():
    global answer

    word_lists = []  # 각 단어별로 필요한 글자
    candidates = set()  # 전체 글자 후보들
    for word in words:
        word_list = set()
        for letter in word:
            if letter not in "antic":
                word_list.add(letter)
                candidates.add(letter)
        word_lists.append(list(word_list))

    # 모든 후보 글자를 다 가르쳐도 되는 경우를 가지치기
    if K >= len(candidates):
        answer = N
        return

    dfs(0, 0, list(word_lists), list(candidates), [])


# 입력 및 실행
N, K = map(int, input().split())
answer = 0
words = []
for _ in range(N):
    words.append(input())
if K < 5:  # "antic"은 무조건 가르쳐야 됨
    print(0)
elif K >= 26:  # 26개 이상이면 모든 알파벳을 다 배울 수 있음
    print(N)
else:
    K -= 5  # "antic"을 제외한 나머지 글자(K-5개) 중 어떤 것을 가르칠 지
    solution()
    print(answer)