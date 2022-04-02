import random
import sys

my_list = [random.randint(0,100) for _ in range(20)]
print(my_list)
max_number = - sys.maxsize
for number in my_list:
    if number > max_number:
        max_number = number
print(max_number)