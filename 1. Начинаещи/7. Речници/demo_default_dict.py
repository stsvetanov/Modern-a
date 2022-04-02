from collections import defaultdict
import random

my_list = [(random.randint(1, 5), random.randint(1, 5)) for _ in range(10)]

dates_dict = defaultdict(list)
for key, date in my_list:
    dates_dict[key].append(date)

print(dates_dict)
