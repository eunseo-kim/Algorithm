def solution(s):
    s = s[2:-2].split("},{")
    s.sort(key=len)
    numbers = set()
    answer = []

    for case in s:
        case = case.split(",")
        for n in case:
            if n not in numbers:
                answer.append(int(n))
                numbers.add(n)
                break
    return answer


s = "{{2,3,1,4},{2},{2,3},{3,2,1}}"
result = solution(s)
print(result)