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
