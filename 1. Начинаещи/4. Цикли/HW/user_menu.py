# Модифицирайте следната програма, така че:
# при въвеждане на max да притира масималния елемент
# при въвеждане на min да притира минималния елемент
# при въвеждане на average да притира средна стойност
# при въвеждане на sum да притира сумата

sum_prices = 0
while True:
    price = input("Enter prace (or 'stop'): ")
    if price == "stop":
        break
    else:
        # sum_prices = sum_prices + int(price)
        sum_prices += int(price)

print(f"Sum is: {sum_prices}")