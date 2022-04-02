from utils2 import create_connection, get_category_from_url, put_data_into_db

DB_FILENAME = 'foods.db'
TARGET_URL = 'https://en.openfoodfacts.org/categories&json=1'


def main():
    connection = create_connection(DB_FILENAME)

    items = get_category_from_url(TARGET_URL)
    print(len(items))
    for item in items:
        print(item['name'])

    # put_data_into_db(connection, items)


if __name__ == '__main__':
    main()
