prices = [2,1,2,1,0,1,2]
prices = [7,1,5,3,6,3]

def twopointersway(prices):
    l = 0
    r = 1
    n = len(prices)
    is_bought = False
    sell = 0

    while r < n:
        buy_price = prices[l]
        next_price = prices[r]

        profit = next_price - buy_price

        # If profit is in negative I move the price
        if profit < 0:
            l = r
            is_bought = True
        else:
            sell = max(profit, sell)
        r += 1

    return sell

def striverway(prices):
    if not prices:
        return 0

    mini = prices[0]
    max_profit = 0

    for i in range(1, len(prices)-1):
        mini = min(mini, prices[i])
        next_day_price = prices[i+1]
        profit = next_day_price - mini
        max_profit = max(max_profit, profit)

    return max_profit

print(striverway(prices))
