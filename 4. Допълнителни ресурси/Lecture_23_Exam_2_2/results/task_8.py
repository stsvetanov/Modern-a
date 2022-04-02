import json
import requests

import sqlite3

response = requests.get('https://en.openfoodfacts.org/categories&json=1')
response_json = json.loads(response.text)
tags = response_json.get('tags')

conn = sqlite3.connect('Data.db')

cur = conn.cursor()

cur.execute('create table if not exists Data(url varchar(200), products varchar(200), name varchar(200));')

for item in tags:
    if item['name'].find('popcorn') != -1:
        print(f'{item["url"]}:  {item["products"]}:  {item["name"]}')
        cur.execute('INSERT INTO Data(url, products, name) VALUES(?, ?, ?)',
                    [
                        item['url'],
                        item['products'],
                        item['name']
                    ])
        conn.commit()

cur.close()
