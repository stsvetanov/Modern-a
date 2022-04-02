list_price = []


def avg(*p):
    avg_p = sum(p) / len(p)
    return avg_p


while True:
    price = input("Въведи цена: ")
    if price == "":
        break
    else:
        list_price.append(float(price))

print(f"Средната стойност на въведените цени е: {avg(*list_price):.2f}")