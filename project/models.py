from project import db

class Student(db.model):
  id = db.Column(db.Integer, primary_key = True, unique = True)
  firstname = db.Column(db.String(30), unique = False, nullable = False)
  lastname = db.Column(db.String(50), unique = False, nullable = False)
  reg = db.Column(db.Integer, unique = False, nullable = False)
  grade = db.Column(db.Integeer, unique = False)