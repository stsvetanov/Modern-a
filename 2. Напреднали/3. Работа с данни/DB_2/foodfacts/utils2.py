import json
import sqlite3

import requests


def create_connection(db_file_name):
    try:
        conn = sqlite3.connect(db_file_name)
        return conn
    except ConnectionError as e:
        print(e)

    return None


def get_category_from_url(target_url):
    response = requests.get(target_url)
    response_json = json.loads(response.text)

    categories = []

    for item in response_json['tags']:
        # if item['name'] != 'Snacks':
        #     continue
        category = {
            'id': item['id'],
            'url': item['url'],
            'products': item['products'],
            'name': item['name']
        }
        categories.append(category)

    return categories


def put_data_into_db(connection, items):
    cur = connection.cursor()
    cur.execute("""
            create table if not exists categories (
                id varchar(200),
                url varchar(200),
                products varchar(200),
                name varchar(200)
            );
        """)
    cur.close()

    for item in items:
        cur = connection.cursor()
        cur.execute('insert into categories (id, url, products, name) VALUES (?, ?, ?, ?)',
                    [
                        item['id'],
                        item['url'],
                        item['products'],
                        item['name'],
                    ]
                    )
        connection.commit()
        cur.close()
