import csv
from collections import defaultdict

ITEM_ID = 0
CITY = 2


def unique_sales():
    file_handler = open('sales_001.csv')
    reader = csv.reader(file_handler)

    city_by_sales = defaultdict(set)
    for line in reader:
        city_by_sales[line[ITEM_ID]].add(line[CITY])

    # city_by_sales = {line[ITEM_ID].(line[CITY]) for line in reader}

    print(city_by_sales)
    unique_sales_by_city = defaultdict(set)

    for item_id, city_names in city_by_sales.items():
        if len(city_names) == 1:
            city_name = city_names.pop()
            unique_sales_by_city[city_name].add(item_id)

    for city_name, items_ids in sorted(unique_sales_by_city.items()):
        print(', '.join([city_name] + sorted(items_ids)))


if __name__ == '__main__':
    import timeit
    print(timeit.timeit("unique_sales()", setup="from __main__ import unique_sales", number=1))
