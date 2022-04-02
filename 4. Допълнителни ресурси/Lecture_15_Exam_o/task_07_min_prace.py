import csv
import sys


def main():
    # item_id = input()
    # sales_fn = input()
    item_id = "G13130"
    sales_fn = "sales.txt"

    sales = load_sales(sales_fn)

    min_price_city_per_item = {}  # key: city , value: min_price
    for sale in sales:
        sale_item_id, city_name, price = sale
        if sale_item_id != item_id:
            continue
        if city_name not in min_price_city_per_item:
            min_price_city_per_item[city_name] = price
        else:
            if price < min_price_city_per_item[city_name]:
                min_price_city_per_item[city_name] = price

    min_price = sys.maxsize
    
    for key, price in min_price_city_per_item.items():
        if price < min_price:
            max_price = price
            city_name = key


    print(city_name)

    min_prices = list(min_price_city_per_item.items())
    min_prices.sort(key=lambda i: i[1], reverse=True)
    print(min_prices[0][0])

    # -------------------------

    # shorter solution
    sales_filtered = list(filter(lambda sale: sale[0] == item_id, sales))
    sales_filtered.sort(key=lambda i: i[2], reverse=True)
    print(sales_filtered[0][1])


def load_sales(fn: str) -> list:
    result = []
    with open(fn, encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            if not row:
                continue
            if len(row) != 5:
                raise Exception("Invalid row")

            item_id = row[0]
            city_name = row[2]
            price = float(row[-1])

            result.append(
                (item_id, city_name, price)
            )
    return result


if __name__ == '__main__':
    main()