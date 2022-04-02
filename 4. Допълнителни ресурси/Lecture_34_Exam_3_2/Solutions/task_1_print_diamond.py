def print_diamond(symbol, size):
    for n in range(1, size + 1):
        print(" " * (size - n) + symbol + " " * 2 * (n - 1) + symbol)
    for n in range(size, 0, -1):
        print(" " * (size - n) + symbol + " " * 2 * (n - 1) + symbol)


symbol = input("What symbol would you like? ")
size = int(input("What size would you like? "))
print_diamond(symbol, size)
while True:
    want_another = input("Would you like another one? ")
    if want_another != "Yes":
        print("Bye bye!")
        break
    symbol = input("What symbol would you like? ")
    size = int(input("What size would you like? "))
    print_diamond(symbol, size)