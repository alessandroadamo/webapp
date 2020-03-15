from flask_login import UserMixin
from app import db


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, email, name, password):
        self.email = email
        self.name = name
        self.password = password
