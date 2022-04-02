import json

import requests

# response = requests.get('http://api.fixer.io/latest', timeout=2.5)
# response = requests.get('http://www.omdbapi.com/?apikey=cfdf5a02&t=Terminator', timeout=2.5)


response = requests.get('http://www.omdbapi.com',
                        params={'apikey': 'cfdf5a02',
                                "t": "Terminator"})

print(type(response.text))
print(response.text)
response_json = json.loads(response.text)
print(type(response_json))
print(response_json)

print(response_json["Year"])
print(response_json["Ratings"])
print(response_json["Ratings"].pop()["Source"])

