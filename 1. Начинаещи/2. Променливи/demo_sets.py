# numbers1 = {1, 2, 3, 'chetiri', 5, 4, 5, 6, 2}
# numbers2 = set((3, 4, 5, 6, 7))
#
# print(numbers1)
# print(numbers2)
#
# print(2 in numbers1)
#
# if 2 in numbers2:
#     print('ima go')
# else:
#     print('niama go')
#
# numbers1.add(77)
# print(numbers1)
#
# numbers1.add(2)
# print(numbers1)
#
text = "Множеството (set) е съвкупност от уникални елементи. При него няма дефинирана подредба, а основната операция е принадлежност на елемент към множествотоооооо :)."

unique_chars = set()

for char in text:
    unique_chars.add(char)

# unique_chars = set(text)

print(unique_chars)
print(len(unique_chars))

print(unique_chars)
print(len(unique_chars))

chars = {'м', 'ц', 'g', 5}
print(chars)
print(unique_chars.intersection(chars))
