my_string = 'Кой е най-често срещания символ?'
print(len(my_string))

my_string = my_string.replace(" ", "")
print(set(my_string))
print(len(set(my_string)))

if len(my_string) < 1:
    print("Invalid format")
    exit()

characters = {}

for ch in my_string:
    if characters.get(ch) is None:
        characters[ch] = 1
    else:
        characters[ch] = characters.get(ch) + 1

print(characters)

max_count = 0
for key, count in characters.items():
    if count > max_count:
        max_count = count
        top_char = key


print("Най-често срещаният символ е \'{}\' - {} пъти".format(top_char, max_count))


