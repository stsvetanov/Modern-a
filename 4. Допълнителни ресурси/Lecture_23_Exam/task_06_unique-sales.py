import csv
import iso8601
import io
from decimal import Decimal
from datetime import datetime, timezone
from collections import defaultdict



def main():
    try:
        # input_filename = input()
        input_filename = "sales-001.csv"
        sales = load_sales_data(input_filename)
        if len(sales) == 0:
            raise ValueError("Empty input file")

        cities_by_item_id = defaultdict(set)
        for s in sales:
            cities_by_item_id[s.item_id].add(s.city)
            print(cities_by_item_id)

        unique_sales_by_city = defaultdict(list)
        for item_id, city_names in cities_by_item_id.items():
            if len(city_names) == 1:
                city_name = city_names.pop()  # the only element
                unique_sales_by_city[city_name].append(item_id)

        if len(unique_sales_by_city) > 0:
            unique_sales_by_city_flat = [(city_name, list(sorted(item_ids))) for city_name, item_ids in unique_sales_by_city.items()]
            unique_sales_by_city_flat.sort()
            for cn, items in unique_sales_by_city_flat:
                print(",".join([cn] + items))
        else:
            print("NO UNIQUE SALES")
    except Exception:
        print("INVALID INPUT")


# The code below is directly taken from previous lectures and assignments - no need to reimplement this again.


class Item:

    def __init__(self, item_id, country, city, sale_timestamp, price):
        self.item_id = str(item_id)
        self.country = str(country)
        self.city = str(city)

        if not isinstance(sale_timestamp, datetime):
            self.sale_timestamp = iso8601.parse_date(str(sale_timestamp))
        else:
            self.sale_timestamp = sale_timestamp

        # check if sale_timestamp is aware ...
        if self.sale_timestamp.tzinfo is None:
            raise ValueError("Naive datetimes not supported")
        else:
            self.sale_timestamp = self.sale_timestamp.astimezone(timezone.utc)

        if not isinstance(price, Decimal):
            self.price = Decimal(price)
        else:
            self.price = price

    def __repr__(self):
        return "Item: " + str(self.__dict__)


def load_sales_data(filename_sales):
    with io.open(filename_sales) as f:
        sales = [
            Item(
                item_id=sales_row[0],
                country=sales_row[1],
                city=sales_row[2],
                sale_timestamp=sales_row[3],
                price=sales_row[4],
            )
            for sales_row in csv.reader(f)
        ]
        return sales


if __name__ == '__main__':
    main()
