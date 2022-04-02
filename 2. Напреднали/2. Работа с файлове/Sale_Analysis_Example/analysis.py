# analysis.py
# ---------------------------------------

from iso8601 import iso8601

from Advanced.Lecture_11_Sale_Analysis_Example.catalog import load_catalog
from Advanced.Lecture_11_Sale_Analysis_Example.sales import load_sales, KEY_TS, KEY_PRICE, KEY_ITEM_ID

CATALOG_FILENAME = 'catalog_sample.csv'
SALES_FILENAME = 'sales.csv'


def main():
    catalog = load_catalog(CATALOG_FILENAME)
    sales = load_sales(SALES_FILENAME)
    print("Analysis")
    print_total_stats(sales)
    print_top_by_category(sales, catalog)
    print_top_by_city(sales)
    print_top_by_hour(sales)
    # pprint(sales[:10])


def print_total_stats(sales):
    """

    :param sales:
    :return:
    """

    total_count = 0
    total_amount = 0
    min_timestamp = None
    max_timestamp = None

    for sale in sales:
        total_count += 1
        total_amount += sale[KEY_PRICE]
        ts = sale[KEY_TS]

        if max_timestamp is None or ts > max_timestamp:
            max_timestamp = ts
        if min_timestamp is None or ts < min_timestamp:
            min_timestamp = ts




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
        avegage_price= total_amount / total_count if total_count else None,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))


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


def print_top_by_city(sales):
    """

    :param sales:
    :return:
    """


def print_top_by_hour(sales):
    """

    :param sales:
    :return:
    """
    sale_by_hour = {}
    for sale in sales:
        ts = sale.get(KEY_TS)
        price = sale.get(KEY_PRICE)

        dt = iso8601.parse_date(ts)

        ts_hour = dt.replace(minute=0, second=0, microsecond=0)

        hour = ts_hour.hour

        if sale_by_hour.get(hour) is None:
            sale_by_hour[hour] = price
        else:
            sale_by_hour[hour] = sale_by_hour.get(hour) + price

    amounts_by_hour_sorted = []
    for h, total_amount in sale_by_hour.items():
        amounts_by_hour_sorted.append((total_amount, h))

    amounts_by_hour_sorted.sort(reverse=True)

    print("""
        Сума на продажби по часове
    -----------------------------
    """)

    for total_amount, h in amounts_by_hour_sorted[:3]:
        print("     {}: {:.2f} €".format(h, total_amount))


if __name__ == '__main__':
    main()
