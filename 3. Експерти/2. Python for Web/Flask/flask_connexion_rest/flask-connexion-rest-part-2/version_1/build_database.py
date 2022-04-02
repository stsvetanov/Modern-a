import os
from config import db
from models import Person

# Data to initialize database with
# PEOPLE = [
#     {"fname": "Doug", "lname": "Farrell"},
#     {"fname": "Kent", "lname": "Brockman"},
#     {"fname": "Bunny", "lname": "Easter"},
# ]

# Solution
PEOPLE = [
    {"fname": "Doug", "lname": "Farrell", "email": "Doug@td.com"},
    {"fname": "Kent", "lname": "Brockman", "email": "Doug@td.com"},
    {"fname": "Bunny", "lname": "Easter", "email": "Doug@td.com"},
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    # p = Person(lname=person.get("lname"), fname=person.get("fname"))
    p = Person(lname=person.get("lname"), fname=person.get("fname"), email=person.get("email"))
    db.session.add(p)

db.session.commit()
