prices = []

while True:
    price = input("Enter prices, then calculate: sum, average, min or max. Close with stop: ").lower()
    if price == "stop":
        break
    if prices is False:
        if price == "average":
            print(f'The average of your input is {sum(prices)/len(prices)}.')
        elif price == "sum":
            print(f'The sum of your input is {sum(prices)}.')
        elif price == "min":
            print(f'The minimum price in your input is {min(prices)}.')
        elif price == "max":
            print(f'The minimum price in your input is {max(prices)}.')
        else:
            try:
                prices.append(int(price))
            except:
                print('Invalid input')
    else:
        print("Empty list")