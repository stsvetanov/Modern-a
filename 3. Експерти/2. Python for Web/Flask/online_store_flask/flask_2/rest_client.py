import requests
import json

USER_URL = "http://127.0.0.1:5000/api/users"
POST_URL = "http://127.0.0.1:5000/api/posts"


def delete_user(name):
    requests.delete(f"{USER_URL}{name}")


def create_user(user):
    response = requests.post(USER_URL, json=user)
    if response.ok is True:
        print(response.text)
    else:
        print(response.text)


def update_user(name):
    path = f'/{name[1]}'
    person = {"fname": name[0], "lname": name[1]}
    response = requests.put(USER_URL + path, json=person)
    if response.ok is True:
        print(f'Person {name} updated successfully')
    else:
        response_json = json.loads(response.text)
        print(response_json.get("detail"))


def get_user(name):
    response = requests.get(f"{USER_URL}{name}")
    print(response.text)


def get_all_users():
    response = requests.get(USER_URL)
    response_json = json.loads(response.text)
    for person in response_json:
        for key, value in person.items():
            print(key, value)


def create_post(authentication, payload):
    response = requests.post(POST_URL, auth=authentication, json=payload)
    if response.ok is True:
        print(response.text)
    else:
        print(response.text)


user_to_create = {
    "username": "Marina",
    "password": "4d8sdf4d4",
    "email": "mari@faf.com",
    "address": "Sofia 32",
    "phone": "434893994"
}

post_to_create = {
    "title": "Porsche 911",
    "content": "The Carrera is powered by a 355 PS (261 kW; 350 hp) 3.4-litre engine.",
    "price": "250000"
}
auth = ('Marina', '4d8sdf4d4')

# create_user(user_to_create)
create_post(auth, post_to_create)
# get_all()
# name_to_update = "Marin", "Yordanov"
# update(name_to_update)
