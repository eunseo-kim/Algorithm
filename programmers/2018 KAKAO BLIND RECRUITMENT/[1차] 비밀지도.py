def solution(n, arr1, arr2):
    map1, map2 = [], []

    for num in arr1:
        binary = bin(num)[2:].zfill(n)
        map1.append(binary)

    for num in arr2:
        binary = bin(num)[2:].zfill(n)
        map2.append(binary)

    result = [[" " for _ in range(n)] for _ in range(n)]
    for r in range(n):
        for c in range(n):
            if map1[r][c] == "1" or map2[r][c] == "1":
                result[r][c] = "#"

    answer = []
    for re in result:
        answer.append("".join(map(str, re)))

    return answer


result = solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
print(result)
