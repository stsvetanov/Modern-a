
top_char = {}
while True:
    number = input("Въведете число или stop за край")
    if number == "stop":
        break
    print(f"Вие въведохте: {number}")

    if top_char.get(number) is None:
        top_char[number] = 1
    else:
        top_char[number] = top_char.get(number) + 1


print(f"Най-често срещано: {top_char}")
