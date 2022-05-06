import re

# '.'이 처음에 나올 수는 없음
x = "....a..bc..de..."
pattern = "^[.]{1,}"
print(re.sub(pattern, "", x))

# 0~5 사이의 숫자는 처음에 올 수 없음
x = "2310827asd1dwdwa02310"
pattern = "^[0-5]+"
print(re.sub(pattern, "", x))

# 0~5 사이의 숫자는 마지막에 올 수 없음
x = "2310827asd1dwdwa02310"
pattern = "[0-5]+$"
print(re.sub(pattern, "", x))
