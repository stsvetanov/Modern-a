prices = []

error_msg = "Can not be calculated, because the list is empty"

CHOICES = {
    'average': lambda x: sum(x)/len(x) if len(x) > 0 else error_msg,
    'sum': lambda x: sum(x),
    'max': lambda x: max(x) if len(x) > 0 else error_msg,
    'min': lambda x: min(x) if len(x) > 0 else error_msg
}

while True:
    user_input = input("Enter some prices, then calculate: sum, average, min or max. Close with stop: ").lower()
    if user_input == "stop":
        break

    if user_input in CHOICES:
        print(f'The {user_input} of your input is: {CHOICES.get(user_input)(prices)}.')
    else:
        try:
            prices.append(int(user_input))
        except:
            print('Invalid input')
