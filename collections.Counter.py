from collections import Counter

def raghu_earnings(shop_shoes, n):
    earnings = 0
    available_shoes = Counter(shop_shoes)
    for desired_size, price in customers:
        if available_shoes[desired_size] > 0:
            earnings += price
            available_shoes[desired_size] -= 1
    return earnings
    
x = int(input())
shop_shoes = list(map(int, input().split()))
n = int(input())
customers = []
for _ in range(n):
    desired_size, price = map(int, input().split())
    customers.append([desired_size, price])
earnings = raghu_earnings(shop_shoes, n)
print(earnings)
