import requests
import sqlite3


def create_connection(db_file):
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except ConnectionError as e:
        print(e)
        return None


def get_category_from_url(target_url):
    response = requests.get(target_url)
    response_json = response.json()
    tags = response_json.get('tags')

    # categories = [d.get('name', 'None').replace('\'', '') for d in tags]

    categories = []
    for data in tags:
        category = {
            "name": data.get('name', 'None').replace('\'', ''),
            "id": data.get('id'),
            "url": data.get('url')
        }
        categories.append(category)

    return categories


def put_data_into_db(connection, items):
    for category_idx, category in enumerate(items):
        cursor = connection.cursor()
        cursor.execute(
            'INSERT INTO category (name, category_id, url) values (?, ?, ?)',
            [
                category.get('name'),
                category.get('id'),
                category.get('url')
            ]
        )
        connection.commit()
        cursor.close()
        if category_idx > 10:
            break
