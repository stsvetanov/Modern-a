import requests
import json

url = "http://127.0.0.1:5000/api/people"


def delete(name):
    requests.delete(f"{url}{name}")


def create(name=None):
    person = {"fname": name[0], "lname": name[1]}
    response = requests.post(url, json=person)


def update(name):
    pass


def get(name):
    response = requests.get(f"{url}{name}")
    print(response.text)


def get_all():
    response = requests.get(url)
    response_json = json.loads(response.text)
    for person in response_json:
        print(person.get('fname'))


#
name_to_create = "Marin", "Marinov"
create(name_to_create)
name_to_update = "Marin5", "Marinov6"
update(name_to_update)
