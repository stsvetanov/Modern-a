import datetime as dt
from marshmallow import pprint, post_load
from marshmallow import Schema, fields


class User:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        self.created_at = dt.datetime.now()

    def __repr__(self):
        return "<User(lname={self.lname!r})>".format(self=self)


class UserSchema(Schema):
    fname = fields.Str()
    lname = fields.Str()
    created_at = fields.DateTime()

    @post_load
    def make_user(self, data, **kwargs):
        return User(**data)

# Serializing Objects (“Dumping”)
user = User(fname="Monty", lname="Pen")
schema = UserSchema()
result = schema.dump(user)
pprint(result)

# Deserializing Objects (“Loading”)
# # user_data = {
# #     "created_at": "2014-08-11T05:26:03.869245",
# #     "email": "ken@yahoo.com",
# #     "name": "Ken",
# # }

# user_data = result
user_data = {"fname": "Ronnie", "lname": "Ronniev"}
schema = UserSchema()
result = schema.load(user_data)
print(type(result))
pprint(result)