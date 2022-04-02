import json

import requests

# response = requests.get('http://dir.bg?query=Времето')

response = requests.get('http://dir.bg',
                        params={'query': 'Времето'})

print(response.json)

# response = requests.get('http://dir.bg')
# print(response.text)

