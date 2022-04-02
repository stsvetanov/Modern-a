print("Въведете чила или стоп за край")

sum = 0
counter = 0
while True:
    number = input()
    if number == "stop":
        break
    print(f"Вие въведохте: {number}")
    sum += float(number)
    counter += 1

print(f"Средно: {sum / counter}")
