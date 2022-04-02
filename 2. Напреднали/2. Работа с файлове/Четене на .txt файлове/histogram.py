from collections import defaultdict

file_name = "../../random_numbers.txt"

with open(file_name) as file_handler:
    # numbers = defaultdict(int)
    numbers = [0 for _ in range(16)]

    for line in file_handler:
        line = int(line.strip('\n'))
        # numbers[line] += 1
        numbers[line] += 1

    print(numbers)

max = max(numbers)
number_of_stars = 20

for number in numbers:
    print(f"group_{1}: ", '*' * int(number/max * number_of_stars))
