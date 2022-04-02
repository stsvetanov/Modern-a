# sales.py
# ------------------------------------------------------------------------------------

import csv
import iso8601

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
        for line in reader:
            sale = {
                KEY_ITEM_ID: line[COLUMN_ITEM_ID],
                KEY_COUNTRY: line[COLUMN_COUNTRY],
                KEY_CITY: line[COLUMN_CITY],
                KEY_TS: line[COLUMN_TS],
                KEY_PRICE: float(line[COLUMN_PRICE])
            }
            result.append(sale)

    return result
