def average(x):
    return sum(x)/len(x)


prices = []

while True:
    user_input = input("Enter prices, then calculate: sum, average, min or max. Close with stop: ").lower()
    if user_input == "stop":
        break

    if user_input == "average":
        print(f'The average of your input is {average(prices)}.')
    elif user_input == "sum":
        print(f'The sum of your input is {sum(prices)}.')
    elif user_input == "min":
        print(f'The minimum price in your input is {min(prices)}.')
    elif user_input == "max":
        print(f'The minimum price in your input is {max(prices)}.')
    else:
        try:
            prices.append(int(user_input))
        except:
            print('Invalid input')
