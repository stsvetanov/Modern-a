# List, Dict

elements = []

while True:
    user_input = input("Enter text: ")
    if user_input.lower() == "stop":
        break
    elements.append(user_input) # заменете този ред с кода, който пълни речника (16 до 19)

print(elements)
print(len(elements))

dict_of_elements = {}
for element in elements:
    if dict_of_elements.get(element) is None:
        dict_of_elements[element] = 1
    else:
        dict_of_elements[element] += 1

print(dict_of_elements)

for key, value in dict_of_elements.items():
    print(key)
    print(value)
    # добавете логиката, която намира най-често срещания елемент.

# most_common = ?
# print(f"Most common element is {}")

