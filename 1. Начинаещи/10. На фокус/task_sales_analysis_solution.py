import csv
import iso8601

CATALOG_FILENAME = 'catalog_sample.csv'
SALES_FILENAME = 'sales.csv'

COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4

KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'

COLUMN_ITEM_ID = 0
COLUMN_CATEGORY = 5


def main():
    catalog = load_catalog(CATALOG_FILENAME)
    print("Analysis")

    total_count = 0
    total_amount = 0
    min_timestamp = None
    max_timestamp = None

    load_sales_generator_object = load_sales(SALES_FILENAME)
    for sale in load_sales_generator_object:
        total_amount += sale[KEY_PRICE]
        total_count += 1
        ts = sale[KEY_TS]

        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts
        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts

    print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {avegage_price} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
""".format(
        total_count=total_count,
        total_amount=total_amount,
        avegage_price=total_amount / total_count if total_count else None,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))

    print_top_by_category(load_sales(SALES_FILENAME), catalog)


def load_catalog(filename: str) -> dict:
    """
    Expected columns in catalog file:

    1. Идентификационен номер на артикула;
    2. Наименование на артикула;
    3. Цветове, в които артикулът е наличен;
    4. Група на артикула;
    5. Спорт, за който е предназначен артикулът;
    6. Категория
    7. Подкатегория
    8. Пол, за който е предназначен артикула - мъже, жени, unisex, деца, бебета

    Result:
        {
            # item_id : category name
            "J11328": "SHOES",
            ...
        }

    """
    result = {}
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            item_id = row[COLUMN_ITEM_ID]
            category = row[COLUMN_CATEGORY]
            result[item_id] = category
    return result


def load_sales(filename: str) -> dict:
    """
    Expected columns in catalog file:
        1. Идентификационен номер на артикула;
        2. Държава, в която е била извършена продажбата (ISO code)
        3. Име на град, в която е била извършена продажбата;
        4. Дата/час на продажбата с timezone, във формат ISO8601;
        5. Цена на продажбата (цените на един и същ артикул в различните държави са различни)


    Result:

        [
            {
                "item_id": "561712",
                "country": "ES",
                "city": "Murcia",
                "ts": datetime(2015, 12, 11, 17, 14, 05, tz=+01:00),
                "price": 43.21
            },
            {
                ...
            }
            ..
        ]
    """
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            yield sale


def print_top_by_category(sales, catalog):
    """

    :param sales:
    :return:
    """

    amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales

    for sale in sales:
        item_id = sale[KEY_ITEM_ID]
        price = sale[KEY_PRICE]
        category_name = catalog.get(item_id, None)
        if category_name not in amounts_by_category:
            amounts_by_category[category_name] = 0
        amounts_by_category[category_name] += price

    amounts_by_category_sorted = []
    for category_name, total_amount in amounts_by_category.items():
        amounts_by_category_sorted.append((total_amount, category_name))

    amounts_by_category_sorted.sort(reverse=True)


    print("""
    Сума на продажби по категории (top 5)
-----------------------------
""")
    for total_amount, category_name in amounts_by_category_sorted[:5]:
        print("     {}: {:.2f} €".format(category_name, total_amount))


if __name__ == '__main__':
    main()