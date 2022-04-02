print([n**2 for n in range(10)])

s = "Някакъв списък"
chars = [ch.upper() for ch in s]
print(chars)

# # Set comprehension
# s = "Някакъв друг по-дълъг текст на на"
# # print(set(s)) # s is iterable
# unique_chars = {ch.lower() for ch in s}
# print(unique_chars)

# # Dict comprehension
# unique_numbers = {n for n in range(10)}
# print(unique_numbers)
#
number_to_square = {n: n**2 for n in range(10)}
print(number_to_square)
number_to_square = {n: n**2 for n in range(10) if n % 2 == 0}
print(number_to_square)

# a = (n**2 for n in range(10) if n % 2 == 0)
# print(a)
# print(next(a))
# print(next(a))
# print(next(a))
