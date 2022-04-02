import requests

response = requests.get('https://fr.openfoodfacts.org/categories&json=1')
response_json = response.json()
tags = response_json.get('tags')

n = 1
for categ in tags[:10]:
    print(str(n)+'.', 'Категория храна:', categ['name'])
    n += 1
