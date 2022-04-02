# Програмата чете от калавиатурата до въвеждане на "стоп" и изписва най-често въведения стринг и колко пъти
import sys

stop = 'stop'

characters = {}

while True:
    ch = input("Enter char (or 'stop'): ")
    if ch == stop or ch == stop.upper():
        break
    else:
        if characters.get(ch) is None:
            characters[ch] = 1
        else:
            if characters.get(ch) == 2:
                print("Limit")
                characters[ch] = characters.get(ch) + 1
                break
            else:
                characters[ch] = characters.get(ch) + 1

max_count = -sys.maxsize
# print(max_count)
for key, count in characters.items():
    if count > max_count:
        max_count = count
        top_char = key


print("Най-често срещаният символ е \'{}\' - {} пъти".format(top_char, max_count))