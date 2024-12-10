a = list(map(int, input().split()))
n = len(a)
lowest_buy_in = float('inf')
max_profit = float('-inf')
for i in range(0, n-1):
    if a[i] < lowest_buy_in:
        lowest_buy_in = a[i]
    else:
        continue
    for j in range(i, n):
        if a[j] - a[i] > max_profit:
            max_profit = a[j] - a[i]
print(max_profit)

# 题解
# a = list(map(int, input().split()))
# lowest_buy_in = float('inf')
# max_profit = 0
# for price in a:
#     lowest_buy_in = min(lowest_buy_in, price)
#     max_profit = max(max_profit, price - lowest_buy_in)
# print(max_profit)
