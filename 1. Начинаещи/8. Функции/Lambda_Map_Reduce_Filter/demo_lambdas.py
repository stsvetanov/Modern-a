import math
import random
import dis


# def identity(x):
#     return x
#
# print(identity(5))
#
# my_identity = lambda x: x
# print(my_identity(10))
#
# squares = lambda x: x**2
# print(squares(5))

# #
# # Taken literally, an anonymous function is a function without a name.
#
# (lambda x: x + 1)(2)
# print((lambda x: x + 1)(2))
# #
# add_one = lambda x: x + 1
# print(add_one(2))

# print((lambda x: math.sin(x))(60))
#
# # Lambda function with 2 arguments
# print((lambda x, y: x + y)(2, 3))
# my_sum = lambda x, y: x + y
# print(my_sum(5, 7))
#
# # Using Lambda with higher-order functions
# high_ord_func = lambda x, func: x + func(x)
# print(high_ord_func(2, lambda x: x * x))
# print(high_ord_func(2, lambda x: x + 3))

# # # Using Lambda with higher-order functions
# def high_ord(x, func):
#     return x + func(x)
#
# def func2(x):
#     return x + 3
#
# func = lambda x: x + 3
# print(func(2))
# print(high_ord(2, func))
# print(high_ord(2, func2))

# # Python code to illustrate cube of a number showing difference between def() and lambda().
# def cube(y):
#     return y * y * y;
#
#
# g = lambda x: x * x * x
# print(g(5))
# print(cube(5))
#
#
# func = lambda a: a + 10
# print(func(5))
#
# foo = lambda x: x*x
# print(foo(10))
#
# # ##############################
# def myfunc(n):
#     return lambda a: a * n
#
#
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# myf = myfunc(4)
# print(mydoubler(11))
# print(mytripler(11))
# print(myf(11))
#
# Map
# Python code to illustrate map() with lambda() to get double of a list.

# my_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
# print(my_list)
# final_list = list(map(lambda x: x**2, my_list))
# generator_object = map(lambda x: x**2, my_list)
# print(final_list)
# print(next(generator_object))

# word = "spam"
# print(list(map(lambda x: chr(ord(x) + 1), word)))
#
# Filter
# Python code to illustrate filter() with lambda()
my_list = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
print(my_list)
final_list = list(filter(lambda x: (x % 2 != 0), my_list))
print(final_list)
#
# Reduce
# Python code to illustrate reduce() with lambda() to get sum of a list
# my_sum = lambda x, y: x + y
# print(my_sum(2, 2))
# my_func = lambda x, y, z: (x + y) * z
# print(my_func(2, 2, 2))
#
# from functools import reduce
# my_list = [5, 8, 10, 20, 50, 100]
# print(my_list)
# sum = reduce((lambda x, y: x + y), my_list)
# print(sum)
#
#
############################################
# numbers = [(n, n % 6) for n in range(10, 20)]
# random.shuffle(numbers)
# print(numbers)
# print(min(numbers))

# #######################
# persons = [('person-{}'.format(n), n % 6) for n in range(10, 20)]
# random.shuffle(persons)
# persons.sort()
# print(persons)
#
# persons_inverted = [(el[1], el[0]) for el in persons]
# print(persons_inverted)
# persons_inverted.sort()
# print(persons_inverted)
#
# # Using Lambdas
# print(min(numbers, key=lambda el: el[1]))
# print(sorted(persons, key=lambda el: el[1]))
#
# lst = [('candy','30','100'), ('apple','10','200'), ('baby','20','300')]
# lst.sort(key=lambda x: x[1])
# print(lst)
#
#
#
# add = lambda x, y: x + y
# type(add)
# dis.dis(add)
#
# def add(x, y): return x + y
# type(add)
# dis.dis(add)
#

