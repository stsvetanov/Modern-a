'''
2. Модифицирайте програмта за определяне на най-често срещан символ, така че да взема данните от файл.
'''

string_f = open("string.txt", encoding="utf-8")
for i in string_f:
    my_string = i
string_f.close()

my_string = my_string.replace(" ", "")
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

print(f"Най-често стрещаният символ е {top_char} - {max_count} пъти")
