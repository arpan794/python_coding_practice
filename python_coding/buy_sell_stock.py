# prices = [7,1,5,3,6,4]

# max_profit = 0

# for i in range(len(prices)):
#     for j in range(i+1, len(prices)):
#         profit = prices[j] - prices[i]
#         max_profit = max(max_profit, profit)

# print(max_profit)



prices = [7,1,5,3,6,4]

left = 0
max_profit = 0

for right in range(1, len(prices)):

    if prices[right] < prices[left]:
        left = right
    else:
        profit = prices[right] - prices[left]
        max_profit = max(max_profit, profit)

print(max_profit)