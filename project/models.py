from project import db

from flask_login import UserMixin

class Student(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True, unique=True)
  firstname = db.Column(db.String(30), unique=False, nullable=False)
  lastname = db.Column(db.String(50), unique=False, nullable=False)
  reg = db.Column(db.Integer, unique=False, nullable=False)
  grade = db.Column(db.Integer, unique=False)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(150), unique=False)


from flask_login import UserMixin, login_user
from flask import session
import uuid
from project import client

users_db = client['MyCollection']

class MongoStudent(UserMixin):

    def __init__(self, email, name, password, _id=None):

        self.email = email
        self.name = name
        self.password = password
        self._id = uuid.uuid4().hex if _id is None else _id

    def is_authenticated(self):
        return True
    def is_active(self):
        return True
    def is_anonymous(self):
        return False
    def get_id(self):
        return self._id

    @classmethod
    def query(cls, query):
        data = users_db.users.find_one(query)
        if data is not None:
            return cls(**data)

    @classmethod
    def insert(cls, obj):
        users_db.users.insert_one(obj)

    def insert_user(self):
        users_db.users.insert_one({
            "_id": self._id,
            "email": self.email,
            "name": self.name,
            "password": self.password
            })
