prices = []

while True:
    price = input("Enter price: ")
    if price == "max" or price == "min" or price == "average" or price == "sum":
        break
    else:
        prices.append(int(price))


sum_prices = sum(prices)
average_price = sum_prices / len(prices)
if price == "max":
    print(f"Максималното число е: {max(prices)}")
elif price == "min":
    print(f"Минималното число е: {min(prices)}")
elif price == "average":
    print(f"Средната стойност на въведените числа е: {average_price:.0f}")
elif price == "sum":
    print(f"Сумата на въведените числата е: {sum_prices:.0f}")