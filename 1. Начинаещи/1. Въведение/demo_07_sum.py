total_sum = 0
current_number = None
while current_number is None or current_number > 0:
    current_number_str = input('Enter an integer > ')
    current_number = int(current_number_str)
    total_sum += current_number
print('The sum is', total_sum)
