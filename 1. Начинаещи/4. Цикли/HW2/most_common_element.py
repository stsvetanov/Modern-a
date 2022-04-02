dict_of_elements = {}
max_elements = {}

while True:
    user_input = input("Enter text: ")
    if user_input.lower() == "stop":
        break
    # Заменен  ред с кода, който пълни речника.
    if dict_of_elements.get(user_input) is None:
        dict_of_elements[user_input] = 1
    else:
        dict_of_elements[user_input] += 1

print(dict_of_elements)

# Добавяне на логиката, която намира най-често срещания елемент.
max_value = (max(list(dict_of_elements.values())))
for key, value in dict_of_elements.items():
    if value == max_value:
        max_elements[key] = value  # Попълва списък от ключовете в речника

# Ако в речника се среща само един елемент най-често.
if len(max_elements) == 1:
    print(f"Най-често срещаният елемент е {list(max_elements.keys()).pop()} = {max_value}.")
else:
    print(f"Най-често срещаните елементи са:", end=" ")
    for key, value in max_elements:
        print(f"{key} = {value}", end=", ")
