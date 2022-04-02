count = 0
sum_prices = 0
sum_min_max = []

stop = 'stop'

while True:
    price = input("Enter prace (or 'stop'): ")
    if price == stop or price == stop.upper():
        break
    else:

        sum_prices += int(price)
        sum_min_max.append(int(price))
        count += 1


average_price = sum_prices / count

print('Min sum is: {}'.format(min(sum_min_max)))
print('Max sum is: {}'.format(max(sum_min_max)))

print('Average price is: {}'.format(average_price))
print("Sum is: {}".format(sum_prices))