import sqlite3
import csv
import iso8601

DB_FILENAME = 'sales-database.db'
CATALOG_FILENAME = 'catalog_sample.csv'
SALES_FILENAME = 'sales.csv'

# Define catalog entry
COLUMN_ITEM_ID = 0
COLUMN_NAME = 1
COLUMN_COLOR = 2
COLUMN_GROUP = 3
COLUMN_SPORT = 4
COLUMN_CATEGORY = 5
COLUMN_SUBCATEGORY = 6
COLUMN_GENDER = 7

# keys for catalog table
KEY_ITEM_ID = 'item_id'
KEY_NAME = 'name'
KEY_COLOR = 'color'
KEY_GROUP = 'group_name'
KEY_SPORT = 'sport'
KEY_CATEGORY = 'category'
KEY_SUBCATEGORY = 'subcategory'
KEY_GENDER = 'gender'

# Define salas entry
COLUMN_ITEM_ID = 0
COLUMN_COUNTRY = 1
COLUMN_CITY = 2
COLUMN_TS = 3
COLUMN_PRICE = 4

# keys for sales table
KEY_ITEM_ID = 'item_id'
KEY_COUNTRY = 'country'
KEY_CITY = 'city'
KEY_TS = 'ts'
KEY_PRICE = 'price'


def main():
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        print("Connection opened")
        create_tables(connection)
        print("Tables created")

        import_catalog_into_db(connection, CATALOG_FILENAME)

        print("Catalog imported")

        import_sales_into_db(connection, SALES_FILENAME)

        print("Sales imported")


def create_tables(connection):
    cursor = connection.cursor()
    cursor.execute("""
        create table if not exists sale (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id varchar(200) NOT NULL,
            country varchar(3),
            city_name varchar(60),
            sale_timestamp TEXT,
            price NUMERIC,
            FOREIGN KEY (item_id) REFERENCES catalog (item_id)
        );
    """)

    cursor.execute("""
        create table if not exists catalog (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item_id varchar(200),
            name varchar(200),
            color varchar(200),
            group_name varchar(100),
            sport varchar(200),
            category varchar(200),
            subcategory varchar(200),
            gender varchar(200)
        );
    """)


def load_catalog(filename: str) -> list:
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
        [
            {
                "item_id": "396559",
                "name": "+TG SWERVE DBMI",
                "color": "WHITE/BLACK",
                "group_name": "HARDWARE",
                "sport": "FOOTBALL/SOCCER"
                "category": "BALLS",
                "subcategory": "BALL (MACHINE-STITCHED)",
                "gender": "Men"
            },
            {
                ...
            }
            ..
        ]
    """

    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            catalog = {
                KEY_ITEM_ID: row[COLUMN_ITEM_ID],
                KEY_NAME: row[COLUMN_NAME],
                KEY_COLOR: row[COLUMN_COLOR],
                KEY_GROUP: row[COLUMN_GROUP],
                KEY_SPORT: row[COLUMN_SPORT],
                KEY_CATEGORY: row[COLUMN_CATEGORY],
                KEY_SUBCATEGORY: row[COLUMN_SUBCATEGORY],
                KEY_GENDER: row[COLUMN_GENDER]
            }
            result.append(catalog)
    return result


def import_catalog_into_db(connection, catalog_filename):
    catalog = load_catalog(catalog_filename)
    cursor = connection.cursor()
    for item in catalog:
        # sql = f'''
        #     insert into catalog (item_id, name, color, group_name, sport, category, subcategory, gender)
        #         values(
        #             '{item[KEY_ITEM_ID]}',
        #             '{item[KEY_NAME]}',
        #             '{item[KEY_COLOR]}',
        #             '{item[KEY_GROUP]}',
        #             '{item[KEY_SPORT]}',
        #             '{item[KEY_CATEGORY]}',
        #             '{item[KEY_SUBCATEGORY]}',
        #             '{item[KEY_GENDER]}'
        #         );
        #     '''
        # cursor.execute(sql)

        cursor.execute(
            'insert into catalog (item_id, name, color, group_name, sport, category, subcategory, gender) values (?, ?, ?, ?, ?, ?, ?, ?)',
            [
                item[KEY_ITEM_ID],
                item[KEY_NAME],
                item[KEY_COLOR],
                item[KEY_GROUP],
                item[KEY_SPORT],
                item[KEY_CATEGORY],
                item[KEY_SUBCATEGORY],
                item[KEY_GENDER]
            ]
        )


def load_sales(filename: str) -> list:
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
    result = []
    with open(filename, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            sale = {}
            sale[KEY_ITEM_ID] = row[COLUMN_ITEM_ID]
            sale[KEY_COUNTRY] = row[COLUMN_COUNTRY]
            sale[KEY_CITY] = row[COLUMN_CITY]
            sale[KEY_TS] = iso8601.parse_date(row[COLUMN_TS])
            sale[KEY_PRICE] = float(row[COLUMN_PRICE])
            result.append(sale)
    return result


def import_sales_into_db(connection, sales_filename):
    sales = load_sales(sales_filename)
    cursor = connection.cursor()
    for sale in sales:
        # sale - dict
        sale_timestamp = sale[KEY_TS]

        cursor.execute(
            'insert into sale (item_id, country, city_name, sale_timestamp, price) values (?, ?, ?, ?, ?)',
            [
                sale[KEY_ITEM_ID],
                sale[KEY_COUNTRY],
                sale[KEY_CITY],
                sale_timestamp.isoformat(),
                sale[KEY_PRICE]
            ]
        )


if __name__ == '__main__':
    main()
