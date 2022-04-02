import requests
import json

url = "http://127.0.0.1:5000"
path = "/api/people"

response = requests.get(url + path)
response_json = json.loads(response.text)

for person in response_json:
    print(person.get('fname'))


endpoint = 'https://httpbin.org/post'
payload = {
        'username': 'Ivan',
        'password': 'Petrov'
}
headers = {'Authorization': 'Bearer something'}

r = requests.post(endpoint, data=payload, headers=headers)
print(r.json())