def solution(bracket):
    temp = []
    while bracket:
        string = bracket.pop()
        
        if string == ")":
            temp.append(string)
        else:
            if len(temp) == 0:
                return "NO"
            temp.pop()
    
    if len(temp) > 0:
        return "NO"

    return "YES"


for _ in range(int(input())):
    result = solution(list(input()))
    print(result)