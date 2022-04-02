## List comprehension
# squares = []
# for n in range(10):
#     squares.append(n**2)
#
# print(squares)
# #
# print([n**2 for n in range(10)])

# s = "Някакъв списък"
# chars = [ch.upper() for ch in s]
# print(chars)

# Set comprehension
# s = "Някакъв друг по-дълъг текст на на"
# # print(set(s)) # s is iterable
# unique_chars = {ch.lower() for ch in s}
# print(unique_chars)

# # Dict comprehension
#
# number_to_square = {n: n**2 for n in range(10)}
# print(number_to_square)
# number_to_square = {n: n**2 for n in range(10) if n%2 == 0}
# print(number_to_square)
import random

a = (n**2 for n in range(10) if n % 2 == 0)
print(a)
print(next(a))
print(next(a))
print(next(a))

print(sorted(filter(lambda x: x % 2 != 0, [random.randint(5, 56) for _ in range(10)])))
