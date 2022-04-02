def average(x):
    return sum(x)/len(x)


prices = []

CHOICES = {
    'average': average,
    'sum': sum,
    'max': max,
    'min': min
}

while True:
    user_input = input("Enter prices, then calculate: sum, average, min or max. Close with stop: ").lower()
    if user_input == "stop":
        break

    if user_input in CHOICES:
        print(f'The {user_input} of your input is {CHOICES.get(user_input)(prices)}.')
    else:
        try:
            prices.append(int(user_input))
        except:
            print('Invalid input')
