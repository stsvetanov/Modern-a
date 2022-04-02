# analysis.py
# ---------------------------------------

from Advanced.Lecture_11_Sale_Analysis_Example.sales import load_sales

# CATALOG_FILENAME = 'catalog_sample.csv'
SALES_FILENAME = 'sales.csv'


def main():
    # catalog = load_catalog(CATALOG_FILENAME)
    # print(catalog)
    sales = load_sales(SALES_FILENAME)
    print("Analysis")
    print_total_stats(sales)
    # print_top_by_category(sales)
    # print_top_by_city(sales)
    # print_top_by_hour(sales)
    # pprint(sales[:10])


def print_total_stats(sales):
    """

    :param sales:
    :return:
    """
    total_count = len(sales)
    total_amount = 0

    min_timestamp = None
    max_timestamp = None

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


def print_top_by_category(sales, catalog):
    """

    :param sales:
    :return:
    """

    amounts_by_category = {}  # key : category name  ,  value : accumulated sum of sales

    # Code goes here

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


if __name__ == '__main__':
    main()
