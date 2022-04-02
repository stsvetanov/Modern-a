import os
from datetime import datetime
from config import db
from models import Person, Note
from security.basic_authentication import generate_password_hash


# Data to initialize database with
PEOPLE = [
    {
        "fname": "Ivan",
        "lname": "Petrov",
        "address": "Sofia 5",
        "email": "ivan@memail.com",
        "phone": "0896584756",
        "password": "secret",
        "notes": [
            ("Cool, an e-commerce application!", "Title1", 23, "2019-01-06 22:17:54", 1, None),
            ("This could be useful", "Title2", 25, "2019-01-08 22:17:54", 1, None)
        ]
    },
    {
        "fname": "Marin",
        "lname": "Georgiev",
        "address": "Sofia 5",
        "email": "marin@memail.com",
        "phone": "+0896584756",
        "password": "secret1",
        "notes": [
            ("Does anyone wont to have Easter eggs?", "Title3", 26, "2019-01-07 22:47:54", 0, "Marin Petrov")
        ]
    }
]

# Delete database file if it exists currently
if os.path.exists("people.db"):
    os.remove("people.db")

# Create the database
db.create_all()

# iterate over the PEOPLE structure and populate the database
for person in PEOPLE:
    p = Person(lname=person.get("lname"),
               fname=person.get("fname"),
               address=person.get("address"),
               email=person.get("email"),
               phone=person.get("phone"),
               password=generate_password_hash(person.get("password"))
               )

    # Add the notes for the person
    for note in person.get("notes"):
        content, title, price, timestamp, is_active, buyer = note
        p.notes.append(
            Note(
                content=content,
                title=title,
                price=price,
                is_active=is_active,
                buyer=buyer,
                timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S"),
            )
        )
    db.session.add(p)

db.session.commit()
