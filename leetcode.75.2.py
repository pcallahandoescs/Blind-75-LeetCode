#stock prices

prices = input('please enter a list of numbers separated by a space')
prices = list(map(int, prices.split()))

max_profit = 0

for i in range(len(prices)):
    for j in range(i+1, len(prices)):
        if prices[i] - prices[j] > max_profit:
            max_profit = prices[i] - prices[j]
        else:
            max_profit = 0

print(max_profit)
