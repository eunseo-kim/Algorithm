def solution(s):
    s = s[2:-2]
    s = s.split("},{")

    nums = set()
    answer = []
    group = []
    for string in s:
        group.append(string.split(","))

    group.sort(key=len)
    for letters in group:
        for letter in letters:
            num = int(letter)
            if num not in nums:
                nums.add(num)
                answer.append(num)
                break

    return answer


s = [
    "{{2},{2,1},{2,1,3},{2,1,3,4}}",
    "{{1,2,3},{2,1},{1,2,4,3},{2}}",
    "{{20,111},{111}}",
    "{{123}}",
    "{{4,2,3},{3},{2,3,4,1},{2,3}}",
]
for ss in s:
    result = solution(ss)
    print(result)
