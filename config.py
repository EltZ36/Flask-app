import os 

class Config():
  SECRETKEY = os.urandom(64)

  TESTING = True
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or 'sqlite:///project.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = False
  SQLALCHEMY_COMMIT_ON_TEARDOWN = True 

