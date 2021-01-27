import os 

class Config():
  SECRETKEY = os.urandom(64)

  TESTING = True
  DEBUG = True

class ProdConfig(Config):
  TESTING = False
  DEBUG = False
