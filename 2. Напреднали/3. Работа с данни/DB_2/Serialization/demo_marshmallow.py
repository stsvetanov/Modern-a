import datetime as dt
from marshmallow import pprint, post_load
from marshmallow import Schema, fields


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(name={self.name!r})>".format(self=self)


class UserSchema(Schema):
    name = fields.Str()
    email = fields.Email()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# Serializing Objects (“Dumping”)
# user = User(name="Monty", email="monty@python.org")
# schema = UserSchema()
# result = schema.dump(user)
# pprint(result)

# Deserializing Objects (“Loading”)
user_data = {
    "created_at": "2014-08-11T05:26:03.869245",
    "email": "ken@yahoo.com",
    "name": "Ken",
}

user_data = {"name": "Ronnie", "email": "ronnie@stones.com"}
schema = UserSchema()
result = schema.load(user_data)
print(type(result))
pprint(result)
pprint(result.email)