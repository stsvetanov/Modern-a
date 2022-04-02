def average_price(*args):
    prices = []

    for i in args:
        prices.append(i)

    sum_prices = 0

    # while True:
    #     price = input("Enter prace (or 'stop'): ")
    #     if price == 'stop':
    #         break
    #     else:
    #         prices.append(price)
    #         sum_prices += int(price)

    if len(prices) < 4:
        print('You need to enter at least 4 prices')
        exit()

    prices.sort()

    # print('Lowest price - {}'. format(prices[0]))
    # print('Highest price - {}'. format(prices[len(prices) -1]))

    sum_prices = sum_prices - (int(prices[0]) + int(prices[len(prices) -1])) # remove values of the highest and lowest praces

    # print('Average prace - {:.2f}'. format(sum_prices/(len(prices) - 2)))
    average_price = sum_prices/(len(prices) - 2)
    return average_price


average_price = average_price(1, 1, 1, 25, 1, 2, 4)
print(average_price)