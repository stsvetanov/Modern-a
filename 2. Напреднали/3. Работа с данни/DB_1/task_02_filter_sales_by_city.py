import sqlite3

DB_FILENAME = 'sales-database.db'

city_name = input("Enter City: ")
order_by = "sale_timestamp"


def main():
    with sqlite3.connect(DB_FILENAME, isolation_level=None) as connection:
        print("Connection opened")
        cursor = connection.cursor()
        cursor.execute("""
            select
                item_id,
                sale_timestamp,
                price
            from
                 sale
            where
                city_name = ?
            order by
                --sale_timestamp
                ?
            """, [city_name, order_by])
        rows = cursor.fetchall()

        for row in rows:
            print(row)


if __name__ == '__main__':
    main()


