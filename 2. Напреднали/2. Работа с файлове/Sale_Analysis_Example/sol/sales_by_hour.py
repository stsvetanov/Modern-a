# analysis.py
from iso8601 import iso8601

from Advanced.Lecture_11_Sale_Analysis_Example.sales import load_sales, KEY_PRICE, KEY_TS, KEY_CITY
from Advanced.Lecture_11_Sale_Analysis_Example.catalog import load_catalog

CATALOG_FILENAME = '../catalog_sample.csv'
SALES_FILENAME = '../sales.csv'


def main():
    catalog = load_catalog(CATALOG_FILENAME)
#    print(catalog)
    sales = load_sales(SALES_FILENAME)
    print("Analysis")
    print_total_stats(sales)
    print_top_by_category(sales, catalog)
    print_top_by_city(sales)
    print_top_by_hour(sales)
#    print(sales[:10])


def print_total_stats(sales):
    """

    :param sales:
    :return:
    """
    total_count = len(sales)
    total_amount = 0

    min_timestamp = None
    max_timestamp = None

    for sale in sales:
        total_amount = total_amount + sale[KEY_PRICE]
        time_stam = sale[KEY_TS]

        if min_timestamp is None or time_stam < min_timestamp:
            min_timestamp = time_stam
        if max_timestamp is None or time_stam > max_timestamp:
            max_timestamp = time_stam
    # Code goes here

    # if total_count > 0:
    #     average_price = total_amount / total_count
    # else:
    #     average_price = None

    print("""
Обобщение
---------
    Общ брой продажби: {total_count}
    Общо сума продажби: {total_amount:.2f} €
    Средна цена на продажба: {average_price} €
    Начало на период на данните: {min_ts}
    Край на период на данните: {max_ts}
""".format(
        total_count=total_count,
        total_amount=total_amount,
        average_price=total_amount / total_count if total_count else None,
        min_ts=min_timestamp,
        max_ts=max_timestamp,
    ))


def print_top_by_category(sales, catalog):
    """

    :param catalog:
    :param sales:
    :return:
    """

#    amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales
    # Code goes here
#    for sale in sales:
#        item_id = sales[KEY_ITEM_ID]
#        price = sales[KEY_PRICE]
#        category_name = catalog.get(item_id, None)
#        if category_name not in amounts_by_category:
#            amounts_by_category[category_name] = 0
#        amounts_by_category[category_name] = amounts_by_category[category_name] + price

#    amounts_by_category_sorted = []
#    for category_name, total_amount in amounts_by_category.items():
#        amounts_by_category_sorted.append((total_amount, category_name))

#    amounts_by_category_sorted.sort(reverse=True)

#    print("""
#    Сума на продажби по категории (top 5)
#-----------------------------
#""")

#    for total_amount, category_name in amounts_by_category_sorted[:5]:
#        print("     {}: {:.2f} €".format(category_name, total_amount))


def print_top_by_city(sales):
    """

    :param sales:
    :return:
    """

    amounts_by_city = {}
    # Code goes here

    for sale in sales:
        city_id = sale[KEY_CITY]
        price = sale[KEY_PRICE]
        if city_id not in amounts_by_city:
            amounts_by_city[city_id] = 0
        amounts_by_city[city_id] = amounts_by_city[city_id] + price

    amounts_by_city_sorted = []
    for city_id, total_amount in amounts_by_city.items():
        amounts_by_city_sorted.append((total_amount, city_id))

    amounts_by_city_sorted.sort(reverse=True)

    print("""
    Сума на продажби по градове (top 5)
-----------------------------
""")

    for total_amount, city_id in amounts_by_city_sorted[:5]:
        print("     {}: {:.2f} €".format(city_id, total_amount))


def print_top_by_hour(sales):
    """

    :param sales:
    :return:
    """

    amounts_by_time = {}
    # Code goes here

    for sale in sales:
        ts = iso8601.parse_date(sale[KEY_TS])
        ts_hour = ts.replace(minute=0, second=0, microsecond=0)
        hour = ts_hour.hour
        price = sale[KEY_PRICE]
        if hour not in amounts_by_time:      # slagame gi
            amounts_by_time[hour] = price        # v rechnika
        else:
            amounts_by_time[hour] = amounts_by_time.get(hour) + price       # uvelichava se cenata

    amounts_by_time_sorted = []
    for ts, total_amount in amounts_by_time.items():
        amounts_by_time_sorted.append((total_amount, ts))

    amounts_by_time_sorted.sort(reverse=True)

    print("""
    Сума на продажби по часове (top 5)
-----------------------------
""")

    for total_amount, ts in amounts_by_time_sorted[:5]:
        print("     {}: {:.2f} €".format(ts, total_amount))


if __name__ == '__main__':
    main()