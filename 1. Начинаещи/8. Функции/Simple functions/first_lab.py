import collections
from collections import defaultdict
from functools import reduce
import operator

f = open("words.txt")
one_string = f.read()
f.close()

# print(one_giant_string[0:25])

word_list = one_string.split()
print(word_list[0:25])


# def my_sum(a, b):
#     return a + b


# ### Task 1
# def avarage_word_len(word_list):
#     out = list(map(len, word_list))
#     # average = reduce(my_sum, out)
#     average = reduce(lambda a, b: a + b, out)
#     return round(average)
#
#
# avg = avarage_word_len(word_list)
# print(avg)
#
#
# ### Task 2
# def does_it_start_y(word):
#     return word.startswith('y')
#
#
# y_words = list(filter(does_it_start_y, word_list))
# ans = avarage_word_len(y_words)
# print(y_words)
# print(ans)

# ### Task 2
letter_to_search = 'y'


