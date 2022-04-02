# def print_temperature(temp):
#     print(temp, 'C')
#
#
# temp = 22
# print_temperature(temp)
# print("hi")

import math

result = math.cos(math.acos(1))
print(result)


def convert_fahrenheit_to_celsius(deg_f):
    return (deg_f - 32) / 1.8


deg_f = 100
deg_c = convert_fahrenheit_to_celsius(deg_f)
print(deg_c)


# Return Type
# def div_mod(number, divisor):   # по някаква причина вградената функция divmod не ни харесва :о)
#     result = number // divisor
#     modulus = number % divisor
#     return result, modulus    # връщаме tuple ;    може да се запише и без скобите - return result, modulus
#
#
# neshto = div_mod(13, 3)
#
# print(type(neshto))
# print(neshto)  # отпечатва върнатия tuple   -  (4, 1)
# print(neshto[0])
#
# #
# # # по-удобно
# r, m = div_mod(13, 3)
# print(r)   # отпечатва 4
# print(m)  # отпечатва 1


# # Default values
# def bigger(param1, param2=25):
#     if param1 > param2:
#         return param1
#     return param2
#
#
# # print(bigger(100, 22)) #  резултатът ще е 100, защото param2 ще е със стойност 22
# print(bigger(100)) #  резултатът ще е 100, защото param2 ще е със стойност 22


# # Named arguments
# def function(param1, param2, param3=30):
#     print(param1)  #  param1 е 33, нищо че е подаден като 2-ри параметър
#     print(param2)  #  param2 е 10, нищо че е подаден като 1-ви параметър
#
#
# function(param2=10, param1=33)


# # Var numbers of arguments
# def sum_numbers(*args):   # args ще бъде tuple, който ще съдържа стойностите на всички подадени позиционни параметри
#     total = 0
#     count = 0
#     for n in args:
#         total += n
#         count += 1
#     return total, count
#
# # ... и да - знаем, че в Python има много по-кратък начин да свършим същата работа :о)
#
#
# print(sum_numbers())
# print(sum_numbers(4, 25))
# print(sum_numbers(5, 1, 49, 26, 45, 34, 3, 81))


# # Scope
# def convert_fahrenheit_to_celsius(degrees_f):
#     degrees_c = (degrees_f - 32) / 1.8
#     return degrees_c
#
# print(convert_fahrenheit_to_celsius(32))
# print(degrees_c)  # грешка - променливата degrees_c е дефинирана във функцията, и тук не съществува
# print(degrees_f)  # грешка - degrees_f е параметър на функцията, и тук не съществува


# # Global Variables
# C_TO_F_DIFFERENCE = 32
# C_TO_F_DIVISOR = 1.8
#
#
# def print_F():
#     print(C_TO_F_DIFFERENCE)
#
#
# print_F()
#
#
# def convert_fahrenheit_to_celsius(degrees_f):
#     degrees_c = (degrees_f - C_TO_F_DIFFERENCE) / C_TO_F_DIVISOR
#     return degrees_c
#
#
# degrees_c = 10
# print(convert_fahrenheit_to_celsius(85))


# # ###############################
# number_of_calculations_performed = 10  # глобална променлива
#
# def calculate():
#     ...
#     number_of_calculations_performed = 1
#     ...
#     number_of_calculations_performed = number_of_calculations_performed + 1
#     print("Value within the calculate function: ", number_of_calculations_performed)
#
# print("Value before calling calculate: ", number_of_calculations_performed)
# calculate()
# print("Value after calling calculate: ", number_of_calculations_performed)


################################


# def calculate(parameter1, parameter2):
#     global number_of_calculations_performed   # достъп за писане до глобалната променлива
#     ...
#     number_of_calculations_performed = number_of_calculations_performed + 1
#     print("Value within the calculate function: ", number_of_calculations_performed)
#
#
# number_of_calculations_performed = 10  # глобална променлива
# print("Value before calling calculate: ", number_of_calculations_performed)
# calculate(4, 5)
# print("Value after calling calculate: ", number_of_calculations_performed)
#
