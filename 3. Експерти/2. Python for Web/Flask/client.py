import requests

# response = requests.post("http://127.0.0.1:5000/hello", params={'name': 'Petar'})
response = requests.post("http://127.0.0.1:5000/hello?name=Ivan")

print(response.text)