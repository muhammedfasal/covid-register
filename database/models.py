from .db import db


class Details(db.Document):
    name = db.StringField(required=True)
    phone_number = db.StringField(required=True)
    number_of_persons = db.StringField(required=True)
