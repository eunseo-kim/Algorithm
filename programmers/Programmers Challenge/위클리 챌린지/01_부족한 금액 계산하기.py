# 언어 : Python
# 날짜 : 2022.06.29
# 문제 : Programmers > 부족한 금액 계산하기
# 티어 : Lv 1
# ==============================================================


def solution(price, money, count):
    total_price = 0

    for current_count in range(1, count + 1):
        total_price += price * current_count
    
    price_need = total_price - money

    if price_need > 0:
        return price_need
    
    return 0


price = 3
money = 20
count = 4
result = solution(price, money, count)
print(result)