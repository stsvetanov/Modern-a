import numpy as np
import matplotlib.pyplot as plt

# my_list = [np.random.randint(0, 15) for _ in range(100)]
# print(my_list)
#
# randomNums = np.random.normal(scale=8, size=50)
# print(randomNums)

# min_size = 0
# max_size = 15
# mean = 8
# std = 1
#
# norm = [str(np.clip(int(np.random.normal(mean,std)),min_size,max_size)) for _ in range(100000)]

# mu = 10
# sigma = 3
# x = np.random.normal(mu, sigma, size=1000)
# x = x.round().astype(int)
# plt.hist(x, 20)
# plt.show()

# file_name = "random_numbers.txt"
# with open(file_name, "w") as file_handler:
#     for number in x:
#         if not(0 <= number <= 15):
#             continue
#         file_handler.write(str(number))
#         file_handler.write("\n")

# file_name = "random_numbers.txt"
# histogram = [0 for _ in range(16)]
# with open(file_name) as file_handler:
#     for line in file_handler:
#         line = int(line)
#         histogram[line] += line

# max = max(histogram)
# for i in range(len(histogram)):
#     print(f'Group{i + 1}: ' + "*" * int(histogram[i] / max * 30))

